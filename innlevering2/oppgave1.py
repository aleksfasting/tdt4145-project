from connection import con
from oppgave2 import leseDataGS, leseDataHS

def settInnSete():
    cursor = con.cursor()
    seteID = 0

    ### Gamle Scene
    seterGS = leseDataGS()
    for område in seterGS.keys():
        for radNr in range(len(seterGS[område])):
            for seteNr in range(len(seterGS[område][radNr])):
                cursor.execute(
                """INSERT INTO SeteTilSete
                VALUES (?, ?)""",
                (seteID, seteNr)
                )

                cursor.execute(
                """INSERT INTO RadTilSete
                VALUES (?, ?)""",
                (seteID, radNr)
                )

                cursor.execute(
                """INSERT INTO OmrådeTilSete
                VALUES (?, ?)""",
                (seteID, område)
                )

                cursor.execute(
                """INSERT INTO SalTilSete
                VALUES (?, 'Gamle Scene')""",
                (seteID, )
                )
                seteID += 1


    ### Hovedscenen
    seterHS = leseDataHS()
    områderHS = ['Parkett', 'Galleri']
    seteNr = 0
    for område in områderHS:
        for radNr in range(len(seterHS[område])):
            for seteIRad in range(len(seterHS[område][radNr])):
                seteNr += 1
                cursor.execute(
                """INSERT INTO SeteTilSete
                VALUES (?, ?)""",
                (seteID, seteNr)
                )
                
                cursor.execute(
                """INSERT INTO RadTilSete
                VALUES (?, ?)""",
                (seteID, radNr)
                )
                
                cursor.execute(
                """INSERT INTO OmrådeTilSete
                VALUES (?, ?)""",
                (seteID, område)
                )

                cursor.execute(
                """INSERT INTO SalTilSete
                VALUES (?, 'Hovedscenen')""",
                (seteID, )
                )
                seteID += 1

def main():
    global cursor
    cursor = con.cursor()

    settInnSete()

    con.commit()
    con.close()



if __name__ == "__main__":
    main()