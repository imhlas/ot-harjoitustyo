# Arkkitehtuurikuvaus
## Ohjelman rakenne



```mermaid
 classDiagram
      Subscription "*" -- "1" User
      UserRepository "1" -- "*" User
      SubscriptionRepository "1" -- "*" Subscription
      SubscriptionService "1" -- "1" SubscriptionRepository
      SubscriptionService "1" -- "1" UserRepository
      SubscriptionService ..> User
      SubscriptionService ..> Subscription
```
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
      }
      Subscription "*" --> "1" User    
```
Sovelluksen toiminnasta vastaa luokan SubscriptionService olio. Käyttäjien ja tilausten tietojen tallennus tapahtuu SQLite -tietokantaan luokkien UserRepository ja SubscriptionRepository kautta.
