# Ruokareseptit

## Sovelluksen toiminnot 

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan lisäämiään ruokareseptejä.
* Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät reseptit.
* Käyttäjä pystyy etsimään reseptejä hakusanalla.
* Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä reseptejä.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät reseptit.
* Käyttäjä pystyy valitsemaan reseptille yhden tai useamman luokittelun (esim. vegaaninen, intialainen, jne.)
* Käyttäjä pystyy antamaan reseptille kommentin ja arvosanan. Reseptistä näytetään kommentit ja keskimääräinen arvosana.


# Sovelluksen asennus

Kloona repo:

```bash
git clone git@github.com:MaxikLLM/Ruokareseptit.git
cd Ruokareseptit
```

Asenna `flask`-kirjasto:

```bash
$ pip install flask
```

Luo virtuaaliympäristö:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Luo tietokannan taulut ja lisää alkutiedot:

```bash
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```bash
$ flask run
```
