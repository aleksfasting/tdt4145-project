# Oppskrift for å kjøre kode

## oppgaver

#### Setup

For å gjøre klar for resten av brukstilfellene må vi initialisere databasen. Dette kan gjøres ved, å kjøre *python3 setup.py*. Denne koden vil kjøre filene: *connection.py*, som lager en tom database og *create-tables.sql* som vil lage tabellene.

#### Oppgave 1

Oppgave 1 besvarelsen består av 2 filer:

- oppgave1.sql
- oppgave1.py

*oppgave1.py* leser sal-filene som ble gitt, og setter inn stolene i databasen, og *oppgave1.sql* setter inn alle de andre tuplee som oppgave 1 spør om. Disse kan kjøres ved:

```
$ sqlite3 teaterDB.db
sqlite> .read oppgave1.sql
sqlite> .quit
$ python3 oppgave1.py
```

Denne oppgaven har ingen forventet output.

#### Oppgave 2

Oppgave 2 besvarelsen består av filen: *oppgave2.py*. Denne filen vil lese sal-filene og legge inn alle 1-erene som en kjøpt billett.

*oppgave2.py* kan kjøres ved:

```
$ python3 oppgave1.py
```

Denne oppgaven har ingen forventet output.

#### Oppgave 3

Oppgave 3 besvarelsen består av filen: *oppgave3.py*. Denne filen vil finne 9 ledige plasser på en rad og sette dem inn som kjøp.

*oppgave3.py* kan kjøres ved:

```
$ python3 oppgave3.py
```

Denne oppgaven har ingen forventet output.

#### Oppgave 4

Opppgave 4 besvarelsen består av filen: *oppgave4.py*. Filen vil spørre brukeren om en dato, også vise alle forestillinger på den datoen.

*oppgave4.py* kan kjøres ved:

```
$ python3 oppgave4.py
Select date: (yyyy-mm-dd) 2024-02-03
```

Denne filen har foventet output:

```
(1, 'Kongsemnene', '2024-02-03', '19:00', 27)
(2, 'Størst av alt er kjærligheten', '2024-02-03', '18:30', 65)
```

#### Oppgave 5

Oppgave 5 besvarelsen består av filen: *oppgave5.sql*. Den vil printe alle roller, hvilken skuespiller som spiller rollen og hvilket stykke det var i.

*oppgave5.sql* kan kjøres ved:

```
$ sqlite3 teaterDB.db
sqlite> .read oppgave5.sql
sqlite> .quit
```

Forventet output fra denne kjøringen er:

```
Haakon Haakonssonn|Arturo Scotti|Kongsemnene
...
Åsmund Flaten|Åsmund Flaten|Storst av alt er kjærligheten
```

#### Oppgave 6

Oppgave 6 besvarelsen består av filen: *oppgave6.sql*. Den vil printe alle forestillinger og relevant info, sortert etter antall billetter solgt.

*oppgave6.sql* kan kjøres ved

```
$ sqlite3 teaterDB.db
sqlite> .read oppgave5.sql
sqlite> .quit
```

Forventet output fra denne kjøringen er:

```
2|Storst av alt er kjærligheten|2024-02-03|18:30|65
...
2|Storst av alt er kjærligheten|2024-02-14|18:30|0
```

#### Oppgave 7

Oppgave 7 besvarelsen består av filen: *oppgave7.py*. Den vil spørre brukeren om et navn på en skuespiller og returnere navnet på alle skuespillere som har spilt sammen med dem.

*oppgave7.py* kan kjøres ved:

```
$ python3 oppgave7.py
Skuespiller: Arturo Scotti
```

Forventet output fra denne kjøringen er:

```
('Arturo Scotti', 'Ingunn Beate Strige Øyen', 'Kongsemnene')
...
('Arturo Scotti', 'Snorre Ryen Tøndel', 'Kongsemnene')
```

## runner.py

Vi har laget et python program som kjører eksempelkode for alle de 7 brukstilfellene.