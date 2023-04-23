# Changelog
## Viikko 3
- Lisätty database_connection -tiedosto, joka luo tietokantayhteyden
- LIsätty initialize_database -tiedosto, joka poistaa entiset tietokantataulut ja luo users -taulun
- Lisätty SubscriptionService -luokka, joka vastaa sovelluslogiikasta
- Lisätty UserRepository -luokka, joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista
- Testattu, että UserRepository -luokka lisää uuden käyttäjän ja palauttaa kaikki käyttäjät

## Viikko 4
- Lisätty ui-hakemisto ja luotu sinne sovelluksen graafisesta käyttöliittymästä vastaavat tiedostot
- Käyttäjä voi käynnistää sovelluksen graafisella käyttöliittymällä
- Käyttäjä voi luoda käyttäjätunnuksen
- Käyttäjä voi kirjautua sisään

## Viikko 5
- Käyttäjä näkee aktiiviset tilaukset
- Käyttäjä voi lisätä uuden tilauksen
- Käyttäjä voi kirjautua ulos
- Lisätty SubscriptionRepository -luokka, joka vastaa tilausten tallennuksesta tietokantaan
- Lisätty graafiseen käyttöliittymään näkymä uusien tilauksien luonnille
