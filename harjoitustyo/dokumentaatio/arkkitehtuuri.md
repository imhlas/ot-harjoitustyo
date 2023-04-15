# Arkkitehtuurikuvaus
## Ohjelman rakenne



```mermaid
 classDiagram
      Subscription "*" -- "1" User
      UserRepository "1" -- "*" User
      SubscriptionRepository "1" -- "*" Subscription
      SubscriptionService "1" -- "1" SubscriptionRepository
      SubscriptionService "1" -- "1" UserRepository
```
