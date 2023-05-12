# Käyttöohje
## Ohjelman rakenne
Ohjelman rakennetta havainnollistaa seuraava pakkauskaavio:

![](./kuvat/pakkaus.png)

Sovelluksen koodi on organisoitu kerrosarkkitehtuurin periaatteiden mukaisesti:
- Käyttöliittymästä vastaava koodi sijaitsee pakkauksessa [ui](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/src/ui).
- Sovelluslogiikasta vastaava koodi löytyy pakkauksen [services](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/src/servies) sisältä.
- Tietojen pysyväistallennuksesta vastaava koodi sijaitsee pakkauksessa [repositories](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/src/repositories).
- Sovelluksen varsinaisia tietokohteita kuvaavat luokat on säilötty pakkaukseen [entities](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/src/entities).

Pakkausten väliset *riippuvuudet* on merkitty kaavioon katkoviivoilla.

## Käyttöliittymä
Käyttöliittymä sisältää neljä erillistä näkymää:

- Kirjautuminen
- Uuden käyttäjän luominen
- Tilausnäkymä *(sovelluksen päänäkymä)*
- Uuden tilauksen luominen

Kaikki näkymät ovat toteutettu pakkauksen *ui* sisälle omina luokkinaan. Pakkauksesta löytyy myös näkymien vaihtoja hallitseva luokka *(ui)*. Eri näkymien painikkeet joko aktivoivat näitä näkymien vaihtoja ja avaavat uusia toimintoja, tai kutsuvat sovelluslogiikasta vastaavan *SubscriptionService*-luokan metodeja. Näin ollen sovelluksen käyttöliittymä ja sovelluslogiikka toimivat erillään toisistaan.
 
## Sovelluslogiikka
Sovelluslogiikassa ovat käytössä luokat User ja Subscription, jotka kuvaavat käyttäjiä ja heidän aktiivisia tilauksiaan:

```mermaid
classDiagram
      class User {
        username
        password
        user_id
      }
      class Subscription {
        user_id
        name
        price
        end_date
        subscription_id
      }
      Subscription "*" --> "1" User    
```
Sovelluksen toiminnasta vastaa luokan *SubscriptionService* olio. Käyttäjien ja tilausten tietojen tallennus tapahtuu SQLite -tietokantaan luokkien *UserRepository* ja *SubscriptionRepository* kautta. Sovelluslogiikka tarjoaa käyttöliittymälle seuraavat metodit:

- *create_user(username, password)*
- *login(username, password)*
- *create_subscription(name, price, end_date)*
- *get_subscriptions()*
- *get_sum_of_subscriptions()*
- *set_subscription_ending()*
- *logout()*

*SubscriptionService*-oliolla on riippuvuus pakkauksessa *repositories* sijaitseviin luokkiin *UserRepository* ja *SubscriptionRepository*, jotka puolestaan ovat yhteydessä sovelluksen oleellista tietosisältöä edustaviin luokkiin *User* ja *Subscription*.
Sovelluksen luokkien suhteita sekä niiden sijaintia sovelluksen rakenteessa kuvataan alla laajennetulla versiolla pakkauskaaviosta, johon on lisätty myös pakkausten sisällä olevat luokat.

![](./kuvat/pakkauskaavio.PNG)
## Tietojen pysyväistallennus
Pakkauksessa *repositories* sijaitsevat luokat *UserRepository* ja *SubscriptionRepository* vastaavat tietojen tallennuksesta SQLite-tietokantaan. Luokat noudattavat Repository-suunnittelumallia ja ne voidaan tarvittaessa korvata uusilla toteutuksilla. 

Sovelluslogiikan testaamisessa tietoja ei tallenneta lainkaan tietokantaan, vaan testit tallentavat tiedot suoraan keskusmuistiin.

## Päätoiminnallisuudet
Seuraavissa alaluvuissa kuvataan sovelluksen kolme tärkeintä päätoiminnallisuutta sekvenssikaavioiden avulla.
### Käyttäjän luominen
Sovelluksen avausnäkymän *Create user* -painiketta klikkaamalla sovellus siirtyy käyttäjän luomisnäkymään. Luomisnäkymässä syötetään toivottu käyttäjätunnus sekä salasana ja painetaan *Create user* -painiketta, minkä jälkeen sovelluksen kontrolli etenee seuraavasti:
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant SubscriptionService
  participant UserRepository
  participant Testaaja
  User->>UI: click "Create user"
  UI->>UI: handle_create_user_view()
  UI->>SubscriptionService: create_user("testaaja", "testi123")
  SubscriptionService->>UserRepository: get_users()
  SubscriptionService->>SubscriptionService: Check username doesn't exist
  SubscriptionService->>Testaaja: User("testaaja", "testi123")
  SubscriptionService->>UserRepository: create_user(Testaaja)
  UserRepository-->>SubscriptionService: user
  SubscriptionService-->>UI: user
  UI->>UI: show_message("User testaaja created succesfully. Please wait.")
  UI->>UI: show_login_view()
```
*Create user* -painikkeen painaminen aktivoi tapahtumankäsittelijän kutsumaan sovelluslogiikan *SubscriptionService* metodia *create_user* antaen parametreiksi halutun käyttäjätunnuksen ja salasanan. Sovelluslogiikka selvittää *UserRepository*:a hyödyntämällä, onko käyttäjätunnus jo olemassa. Mikäli on, sovelluslogiikka tuottaa *UsernameExistsError*-poikkeuksen.

Mikäli haluttua käyttäjätunnusta ei ole käytössä, sovelluslogiikka luo uuden *User*-olion ja tallentaa lähettämällä kutsun *UserRepository*:n metodille *create_user*. Tapahtumankäsittelijä välittää käyttäjälle viestin käyttäjän onnistuneesta luonnista ja pyytää käyttäjää odottamaan. Tämän jälkeen käyttöliittymän näkymä palaa takaisin *LoginView* -näkymään. Käyttäjää edellytetään kirjautumaan erikseen sisään juuri luomillaan tunnuksilla.
### Käyttäjän kirjautuminen
Käyttäjä voi kirjautua sisään kirjautumisnäkymässä syöttämällä käyttäjätunnuksensa sekä salasanansa ja klikkaamalla *Login* -painiketta. Tämän seurauksena sovelluksen kontrolli toimii näin:
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant SubscriptionService
  participant UserRepository
  User->> UI: click "Login"
  UI->>SubscriptionService: login("testaaja", "testi123")
  SubscriptionService->>UserRepository: find_user("testaaja", "testi123")
  SubscriptionService->>SubscriptionService: Check valid credentials
  UserRepository-->>SubscriptionService: user
  SubscriptionService-->>UI: user
  UI->>UI: show_application_view()
```
*Login* -painike aktivoi tapahtumankäsittelijän kutsumaan sovelluslogiikan *SubscriptionService* metodia *login*, joka sisältää parametrit käyttäjätunnukselle ja salasanalle. *SubscriptionService* puolestaan lähettää kutsun *UserRepository*:n metodille *find_user* antaen parametreiksi samat juuri saamansa käyttäjätunnuksen ja salasanan. 

Mikäli tietokannasta ei löydy kyseistä riviä eli käyttäjää, palautuu None. Tämän seurauksena *SubscriptionService* tuottaa *InvalidCredentialsError*:in.

Jos käyttäjä löytyy, käyttöliittymä vaihtaa näkymäksi *CreateApplicationView*:n, joka avaa käyttäjälle sovelluksen päänäkymän sekä näyttää mahdolliset aiemmin lisätyt tilaukset.
### Uuden tilauksen lisääminen
Sovelluksen päänäkymässä käyttäjä pääsee lisäämään uusia tilauksia klikkaamalla painiketta *Add new subscription*. Käyttöliittymä vaihtuu tällöin *CreateSubscriptionView* -näkymään, jonka jälkeen sovelluksen kontrolli etenee seuraavasti:
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant SubscriptionService
  participant SubscriptionRepository
  participant subscription
  User->>UI: click "Add new subscription"
  UI->>UI: show_create_subscription_view()
  UI->>SubscriptionService: create_subscription("Netflix", 9.90, 27.6.2023)
  SubscriptionService->>subscription: Subscription(testaaja.user_id, "Netflix", 9.90, 27.6.2023)
  SubscriptionService->>SubscriptionRepository: create(subscription)
  SubscriptionRepository-->>SubscriptionService: subscription
  SubscriptionService-->>UI: subscription
  UI->>UI: show_message("New subscription added succesfully.Please wait.")
  UI->>UI: show_application_view()
```
Tapahtumankäsittelijä kutsuu sovelluslogiikan *SubscriptionService* metodia *create_subscription*, jolle annetaan parametrina käyttäjän syöttämät tiedot uudesta tilauksesta. Sovelluslogiikka luo uuden *Subscription* -olion ja tallentaa sen tietokantaan kutsumalla *SubscriptionService*:n metodia *create*. 

Mikäli tiedot tallennetaan tietokantaan onnistuneesti, käyttöliittymä välittää tästä käyttäjälle viestin ja pyytää odottamaan. Tämän jälkeen käyttöliittymä siirtyy takaisin sovelluksen päänäkymään *CreateApplicationView*.

### Muut toiminnallisuudet
Yllä kuvattujen päätoiminnallisuuksien lisäksi sovellus sisältää toiminnallisuuden, jolla käyttäjä voi merkitä aktiivisen tilauksensa päättyväksi. Tämä toimii vastaavalla periaatteella päätoiminnallisuuksien kanssa, eli käyttöliittymän tapahtumankäsittelijä kutsuu sovelluslogiikan metodia, joka päivittää tilauksen tilan aktiivisesta päättyväksi. Käyytöliittymän näkymään päivittyy tämän jälkeen tilauksen vaihtunut tila (aktiivinen->päättyvä).

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä
Sovelluksen graafiseen käyttöliittymään olisi saanut tehtyä käyttäjän käyttömukavuutta tehostavia parannuksia, mutta ne jäivät aikataulullisista syistä toteuttamatta. 
