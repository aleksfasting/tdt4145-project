from connection import con
import datetime

cursor = con.cursor()

### Finn en rad som har 9 ledige seter
cursor.execute(
"""SELECT S.Område, S.RadNr, COUNT(*) AS AntallLedige
FROM (SeteTilSete NATURAL JOIN RadTilSete NATURAL JOIN OmrådeTilSete) AS S
WHERE (Område, RadNr, SeteNr) NOT IN    (SELECT Område, RadNr, SeteNr
                                        FROM ((BillettOmråde NATURAL JOIN BillettRadNr)
                                        NATURAL JOIN BillettSeteNr)
                                        NATULAR JOIN BillettKjøpForestilling
                                        WHERE Tid = '18:30' AND Dato = '2024-02-03')
GROUP BY Område, RadNr
HAVING AntallLedige >= 9""")

retRow = cursor.fetchall()
dateAndTime = datetime.datetime.now()

if retRow:
    valgtRad = retRow[0]

    ### Sett inn billettkjøp-tabellene
    cursor.execute(
"""INSERT INTO BillettKjøpKunde
VALUES (3, 1)"""
)
    cursor.execute(
"""INSERT INTO BillettKjøpsDato
VALUES (3, ?, ?)""",
(f'{dateAndTime.year}-{dateAndTime.month}-{dateAndTime.day}', f'{dateAndTime.hour}:{dateAndTime.minute}')
)
    cursor.execute(
"""INSERT INTO BillettKjøpForestilling
VALUES (3, '2024-02-03', '18:30')"""
)
    
    ### Finn 9 ledige seter
    cursor.execute(
"""SELECT *
FROM (SeteTilSete NATURAL JOIN RadTilSete NATURAL JOIN OmrådeTilSete) AS S
WHERE ( Område = ? AND RadNr = ? AND
        (Område, RadNr, SeteNr) NOT IN    (SELECT Område, RadNr, SeteNr
                                        FROM ((BillettOmråde NATURAL JOIN BillettRadNr)
                                        NATURAL JOIN BillettSeteNr)
                                        NATULAR JOIN BillettKjøpForestilling
                                        WHERE Tid = '18:30' AND Dato = 2024-02-03))""",
(valgtRad[0], valgtRad[1],))
    seter = cursor.fetchall()

    ### Sett inn de 9 setene som billetter
    for i in range(9):
        cursor.execute(
"""INSERT INTO BillettOmråde
VALUES (3, ?, ?)""",
(i, seter[i][0])
)
        cursor.execute(
"""INSERT INTO BillettRadNr
VALUES (3, ?, ?)""",
(i, seter[i][1])
)
        cursor.execute(
"""INSERT INTO BillettSeteNr
VALUES (3, ?, ?)""",
(i, seter[i][2])
)
        cursor.execute(
"""INSERT INTO BillettType
VALUES (3, ?, 1)""",
(i, )
)
else:
    raise Exception("Not enough Avaiable Seats")

### Lagre
con.commit()
con.close()