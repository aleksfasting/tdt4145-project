#from connection import con
import sqlite3

con = sqlite3.connect("teaterDB.db")

cursor = con.cursor()

cursor.execute(
"""INSERT INTO Kunde
VALUES (1, 'Anonym', 'Adresse')"""
)

# gamle scene

cursor.execute(
"""INSERT INTO BillettKjøpKunde
VALUES (1, 1)"""
)

cursor.execute(
"""INSERT INTO BillettKjøpsDato
VALUES (1, '0-0-0', '00.00')"""
)

cursor.execute(
"""INSERT INTO BillettKjøpForestilling
VALUES (1, '2024-02-03', '19.00')"""
)

fd = open("src/gamle-scene.txt")
dateGS = fd.readline()

område = ''
seterGS = {}
while True:
    rad = fd.readline().strip()
    if len(rad) == 0:
        break
    if ('0' not in rad and '1' not in rad):
        seterGS[rad] = []
        område = rad
        continue
    elif ('0' in rad or '1' in rad):
        seterRad = []
        for i in range(len(rad)):
            seterRad.append(rad[i])
        seterGS[område].append(seterRad)
        continue

num = 0

for område in seterGS.keys():
    for radNr in range(len(seterGS[område])):
        for seteNr in range(len(seterGS[område][radNr])):
            if seterGS[område][radNr][seteNr] == '1':
                cursor.execute(
"""INSERT INTO BillettOmråde
VALUES (1, ?, ?)""",
(num, område)
                )
                cursor.execute(
"""INSERT INTO BillettRadNr
VALUES (1, ?, ?)""",
(num, radNr)
                )
                cursor.execute(
"""INSERT INTO BillettSete
VALUES (1, ?, ?)""",
(num, seteNr)
                )
                cursor.execute(
"""INSERT INTO BillettType
VALUES (1, ?, 1)""",
(num,)
                )
                num += 1





# hovedscenen

cursor.execute(
"""INSERT INTO BillettKjøpKunde
Values (2, 1)"""
)

cursor.execute(
"""INSERT INTO BillettKjøpsDato
VALUES (2, '0-0-0', '00.00')"""
)

cursor.execute(
"""INSERT INTO BillettKjøpForestilling
VALUES (2, '2024-02-03', '18.30')"""
)

fd = open("src/hovedscenen.txt")
dateHS = fd.readline()

område = ''
seterHS = {}
while True:
    rad = fd.readline().strip()
    if len(rad) == 0:
        break
    if ('0' not in rad and '1' not in rad):
        seterHS[rad] = []
        område = rad
        continue
    elif ('0' in rad or '1' in rad):
        seterRad = []
        for i in range(len(rad)):
            seterRad.append(rad[i])
        seterHS[område].append(seterRad)
        continue

num = 0

for område in seterHS.keys():
    for radNr in range(len(seterHS[område])):
        for seteNr in range(len(seterHS[område][radNr])):
            if seterHS[område][radNr][seteNr] == '1':
                cursor.execute(
"""INSERT INTO BillettOmråde
VALUES (2, ?, ?)""",
(num, område)
                )
                cursor.execute(
"""INSERT INTO BillettRadNr
VALUES (2, ?, ?)""",
(num, radNr)
                )
                cursor.execute(
"""INSERT INTO BillettSete
VALUES (2, ?, ?)""",
(num, seteNr)
                )
                cursor.execute(
"""INSERT INTO BillettType
VALUES (2,?, 1)""",
(num,)
                )
                num += 1

con.commit()

con.close()