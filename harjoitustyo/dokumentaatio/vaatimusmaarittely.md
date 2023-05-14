# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjät voivat seurata omia voimassaolevia tilauksiaan eri palveluissa. Käyttäjät näkevät yksittäisistä tilauksista niiden seuraavan veloituspäivän, veloitettavan hinnan sekä statuksen (aktiivinen/päättyvä). Käyttäjät voivat merkitä tilauksen päättyväksi, jolloin tilaus poistuu listauksesta pättymispäivän jälkeen. Lisäksi käyttäjät näkevät kaikkien tilauksien yhteissumman. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän.

## Käyttäjät
Sovelluksella on ainoastaan yksi käyttäjärooli eli **normaali käyttäjä**.

## Käyttöliittymä
Sovellusta pystyy käyttämään graafisen käyttöliittymän kautta.
- Näkymä kirjautumissivulle
- Näkymä uuden käyttäjän luomiselle
- Näkymä käyttäjän voimassaolevista tilauksista
- Näkymä uuden tilauksen lisäämiseen

## Perusversion tarjoama toiminnallisuus
### Ennen kirjautumista
- Käyttäjä voi luoda käyttäjätunnuksen 
- Käyttäjä voi kirjautua järjestelmään 
	- Kirjatuminen tapahtuu käyttäjätunnuksen ja salasanan avulla
	- Jos käyttäjää ei ole olemassa, järjestelmä ilmoittaa tästä
	- Jos salasana on väärä, järjestelmä ilmoittaa tästä

### Kirjautumisen jälkeen
- Käyttäjä näkee omat voimassaolevat tilaukset, niiden hinnan, seuraavan veloitusajankohdan sekä statuksen(aktiivinen/päättyvä) 
- Käyttäjä näkee kaikkien tilausten yhteissumman
- Käyttäjä voi lisätä uuden tilauksen
- Käyttäjä voi merkitä tilauksen päättyväksi
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita
- Tilausten jako kategorioihin (suoratoistopalvelut, lehtitilaukset, liikunta ym.)
- Päättyneiden tilausten tarkastelu
- Tilauksiin käytettyjen rahasummien tarkastelu kuukausittain

## Toimintaympäristön rajoitteet
- Ohjelmiston tulee toimia Linux -käyttöjärjestelmällä varustetuissa koneissa
- Sovelluksen tulee toimia Python-versiolla 3.8
- Sovelluksen tiedot talletetaan paikalliselle koneelle SQLite-tietokantaa hyödyntäen
