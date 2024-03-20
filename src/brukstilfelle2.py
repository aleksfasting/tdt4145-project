from connection import con


def kundeInit():
    cursor.execute(
"""INSERT INTO Kunde
VALUES (1, NULL, NULL)"""
)



def settInnKjøpGS():
    cursor.execute(
"""INSERT INTO BillettKjøpKunde
VALUES (1, 1)"""
)

    cursor.execute(
"""INSERT INTO BillettKjøpsDato
VALUES (1, NULL, NULL)"""
)

    cursor.execute(
"""INSERT INTO BillettKjøpForestilling
VALUES (1, '2024-02-03', '19:00')"""
)



def settInnKjøpHS():
    cursor.execute(
"""INSERT INTO BillettKjøpKunde
Values (2, 1)"""
)

    cursor.execute(
"""INSERT INTO BillettKjøpsDato
VALUES (2, NULL, NULL)"""
)

    cursor.execute(
"""INSERT INTO BillettKjøpForestilling
VALUES (2, '2024-02-03', '18:30')"""
)



def leseDataGS():
    ### Hente data fra fil
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
    return seterGS



def settInnBilletterGS(seterGS):
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



def leseDataHS():
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
    return seterHS



def settInnBilletterHS(seterHS):
    num = 0
    områder = ['Parkett', 'Galleri']
    seteNr = 0
    for område in områder:
        for radNr in range(len(seterHS[område])):
            for i in range(len(seterHS[område][radNr])):
                seteNr += 1
                if seterHS[område][radNr][i] == '1':
                    cursor.execute(
"""INSERT INTO BillettOmråde
VALUES (2, ?, ?)""",
(num, område)
                )
                    cursor.execute(
"""INSERT INTO BillettRadNr
VALUES (2, ?, ?)""",
(num, radNr + 1)
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




def main():
    global cursor
    cursor = con.cursor()

    kundeInit()

    settInnKjøpGS()
    settInnKjøpHS()

    seterGS = leseDataGS()
    seterHS = leseDataHS()

    settInnBilletterGS(seterGS)
    settInnBilletterHS(seterHS)

    con.commit()
    con.close()

if __name__ == "__main__":
    main()