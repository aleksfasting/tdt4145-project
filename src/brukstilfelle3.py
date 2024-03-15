from connection import con
import datetime

cursor = con.cursor()

cursor.execute(
"""SELECT S.Område, S.RadNr, COUNT(*) AS AntallLedige
FROM Sete AS S
WHERE (Område, RadNr, SeteNr) NOT IN    (SELECT Område, RadNr, SeteNr
                                        FROM ((BillettOmråde NATURAL JOIN BillettRadNr)
                                        NATURAL JOIN BillettSete)
                                        NATULAR JOIN BillettKjøpForestilling
                                        WHERE Tid = 18.30 AND Dato = 2024-02-03)
GROUP BY Område, RadNr
HAVING AntallLedige >= 9""")

ret = cursor.fetchall()

dt = datetime.datetime.now()

if ret:
    valgtRad = ret[0]
    cursor.execute(
"""INSERT INTO BillettKjøpKunde
VALUES (3, 1)"""
)
    cursor.execute(
"""INSERT INTO BillettKjøpsDato
VALUES (3, ?, ?)""",
(f'{dt.year}-{dt.month}-{dt.day}', f'{dt.hour}:{dt.minute}')
)
    cursor.execute(
"""INSERT INTO BillettKjøpForestilling
VALUES (3, '2024-02-03', '18.30')"""
)
    cursor.execute(
"""SELECT *
FROM Sete
WHERE ( Område = ? AND RadNr = ? AND
        (Område, RadNr, SeteNr) NOT IN    (SELECT Område, RadNr, SeteNr
                                        FROM ((BillettOmråde NATURAL JOIN BillettRadNr)
                                        NATURAL JOIN BillettSete)
                                        NATULAR JOIN BillettKjøpForestilling
                                        WHERE Tid = 18.30 AND Dato = 2024-02-03))""",
(valgtRad[0], valgtRad[1],))
    seter = cursor.fetchall()

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
"""INSERT INTO BillettSete
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

con.commit()
con.close()