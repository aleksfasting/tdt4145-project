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
                                        WHERE Tid = 18.30)
GROUP BY Område, RadNr
HAVING AntallLedige > 8""")

ret = cursor.fetchall()
print(ret)

dt = datetime.datetime.now()

if False:
    valgtRad = ret[0]
    cursor.execute(
"""INERT INTO BillettKjøpKunde
VALUES (3, 1)"""
)
    cursor.execute(
"""INSERT INTO BillettKjøpsDato
VALUES (3, ?, ?)""",
(f'{dt.year}-{dt.month}-{dt.day}', f'{dt.hour}:{dt.minute}')
)
    cursor.execute(
"""INSERT INTO BillettKjøpKunde
VALUES (3,1)"""
)

cursor.close()