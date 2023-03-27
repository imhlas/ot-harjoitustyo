# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjät voivat seurata omia voimassaolevia tilauksiaan eri palveluissa. Käyttäjät näkevät tilauksista myös niiden seuraavan veloituspäivän sekä veloitettavan hinnan. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän.

## Käyttäjät
Sovelluksella on ainoastaan yksi käyttäjärooli eli *normaali käyttäjä*.

## Perusversion tarjoama toiminnallisuus
### Ennen kirjautumista
- Käyttäjä voi luoda käyttäjätunnuksen
- Käyttäjä voi kirjautua järjestelmään
	- Kirjatuminen tapahtuu käyttäjätunnuksen ja salasanan avulla
	- Jos käyttäjää ei ole olemassa, järjestelmä ilmoittaa tästä
	- Jos salasana on väärä, järjestelmä ilmoittaa tästä

### Kirjautumisen jälkeen
- Käyttäjä näkee omat voimassaolevat tilaukset, niiden hinnan sekä seuraavan veloitusajankohdan
- Käyttäjä voi lisätä uuden tilauksen
- Käyttäjä voi merkitä tilauksen päättyväksi
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita
- Voimassaolevien tilausten yhteissumma näkyvissä kirjautumisen jälkeen
- Tilausten jako kategorioihin (suoratoistopalvelut, lehtitilaukset, liikunta ym.)
- Päättyneiden tilausten tarkastelu
- Tilauksiin käytettyjen rahasummien tarkastelu kuukausittain
