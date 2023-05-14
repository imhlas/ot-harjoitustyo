# Subscription Manager App
Sovelluksen avulla käyttäjät voivat seurata voimassaolevia tilauksiaan eri palveluihin. Käyttäjät näkevät profiilistaan voimassaolevista tilauksistaan seuraavat tiedot:
- Tilauksen nimi
- Tilauksen hinta
- Tilauksen seuraava veloitusajankohta
- Tilauksen status (aktiivinen/päättyvä)

Lisäksi käyttäjät näkevät kaikkien aktiivisten tilaustensa yhteissumman. Käyttäjät voivat lisätä profiiliinsa uusia tilauksia sekä merkitä voimassaolevia tilauksia päättyviksi.

## Releases
- [Viikko 5 release](https://github.com/imhlas/ot-harjoitustyo/releases/tag/viikko5)
- [Viikko 6 release](https://github.com/imhlas/ot-harjoitustyo/releases/tag/viikko6)
- [Loppupalautus](https://github.com/imhlas/ot-harjoitustyo/releases/tag/Loppupalautus)


## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/testaus.md)
- [Työaikakirjanpito](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/imhlas/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/changelog.md)

## Asennus
1. Riippuvuuksien asentaminen komennolla:
```bash
poetry install
```
2. Alustustoimenpiteet komennolla:
```bash
poetry run invoke build
```
3. Sovelluksen käynnistys komennolla:
```bash
poetry run invoke start
```

## Komentorivitoiminnot
### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla:
```bash
poetry run invoke start
```
### Testaus
Testit suoritetaan komennolla:
```bash
poetry run invoke test
```
### Testikattavuus
Testikattavuusraportin voi muodostaa komennolla:
```bash
poetry run invoke coverage-report
```
### Pylint
Pylint-tarkistukset voi suorittaa komennolla:
```bash
poetry run invoke lint
```

