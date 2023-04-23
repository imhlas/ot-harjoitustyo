# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjät voivat seurata omia voimassaolevia tilauksiaan eri palveluissa. Käyttäjät näkevät tilauksista myös niiden seuraavan veloituspäivän sekä veloitettavan hinnan. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän.

## Käyttäjät
Sovelluksella on ainoastaan yksi käyttäjärooli eli **normaali käyttäjä**.

## Käyttöliittymä
Sovellusta pystyy käyttämään graafisen käyttöliittymän kautta.
- Näkymä kirjautumissivulle **(tehty)**
- Näkymä uuden käyttäjän luomiselle **(tehty)**
- Näkymä käytäjän voimassaolevista tilauksista **(tehty)**
- Näkymä uuden tilauksen lisäämiseen **(tehty)**
- Näkymä menneisiin tilauksiin ja niiden kustannuksiin *(tämä jos jää aikaa)*

## Perusversion tarjoama toiminnallisuus
### Ennen kirjautumista
- Käyttäjä voi luoda käyttäjätunnuksen **(tehty)**
- Käyttäjä voi kirjautua järjestelmään **(tehty)**
	- Kirjatuminen tapahtuu käyttäjätunnuksen ja salasanan avulla
	- Jos käyttäjää ei ole olemassa, järjestelmä ilmoittaa tästä
	- Jos salasana on väärä, järjestelmä ilmoittaa tästä

### Kirjautumisen jälkeen
- Käyttäjä näkee omat voimassaolevat tilaukset, niiden hinnan sekä seuraavan veloitusajankohdan **(tehty)**
- Käyttäjä voi lisätä uuden tilauksen **(tehty)**
- Käyttäjä voi merkitä tilauksen päättyväksi
- Käyttäjä voi kirjautua ulos järjestelmästä **(tehty)**

## Jatkokehitysideoita
- Voimassaolevien tilausten yhteissumma näkyvissä kirjautumisen jälkeen
- Tilausten jako kategorioihin (suoratoistopalvelut, lehtitilaukset, liikunta ym.)
- Päättyneiden tilausten tarkastelu
- Tilauksiin käytettyjen rahasummien tarkastelu kuukausittain

## Toimintaympäristön rajoitteet
- Ohjelmiston tulee toimia Linux -käyttöjärjestelmällä varustetuissa koneissa
- Sovelluksen tulee toimia Python-versiolla 3.8
- Sovelluksen tiedot talletetaan paikalliselle koneelle SQLite-tietokantaa hyödyntäen
