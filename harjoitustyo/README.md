# Subscription Manager App
Sovelluksen avulla käyttäjät voivat seurata voimassaolevia tilauksiaan eri palveluihin. Käyttäjät näkevät profiilistaan voimassaolevat tilaukset, niiden hinnan sekä seuraavan veloitusajankohdan.

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/changelog.md)

## Komentorivitoiminnot
### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla:
```bash
poetry run invoke start

### Testaus
Testit suoritetaan komennolla:
```bash
poetry run invoke test

### Testikattavuus
Testikattavuusraportin voi muodostaa komennolla:
```bash
poetry run invoke coverage-report
