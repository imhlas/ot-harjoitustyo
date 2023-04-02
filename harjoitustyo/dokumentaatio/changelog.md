# Changelog
## Viikko 3
- Lisätty database_connection -tiedosto, joka luo tietokantayhteyden
- LIsätty initialize_database -tiedosto, joka poistaa entiset tietokantataulut ja luo users -taulun
- Lisätty SubscriptionService -luokka, joka vastaa sovelluslogiikasta
- Lisätty UserRepository -luokka, joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista
- Testattu, että UserRepository -luokka lisää uuden käyttäjän ja palauttaa kaikki käyttäjät
