from connection import con
import datetime
import sys

def finnOgKjøpSeter():
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

        cursor.execute(
        """SELECT MAX(KjøpID)
        FROM BillettKjøpKunde"""
        )

        kjøpID = cursor.fetchall()[0][0] + 1

        ### Sett inn billettkjøp-tabellene
        cursor.execute(
        """INSERT INTO BillettKjøpKunde
        VALUES (?, 1)""",
        (kjøpID,)
        )
        cursor.execute(
        """INSERT INTO BillettKjøpsDato
        VALUES (?, ?, ?)""",
        (kjøpID,f'{dateAndTime.year}-{dateAndTime.month}-{dateAndTime.day}', f'{dateAndTime.hour}:{dateAndTime.minute}')
        )
        cursor.execute(
        """INSERT INTO BillettKjøpForestilling
        VALUES (?, '2024-02-03', '18:30')""",
        (kjøpID,)
        )
    
        ### Finn 9 ledige seter
        cursor.execute(
        """SELECT Område, RadNr, SeteNr
        FROM (SeteTilSete NATURAL JOIN RadTilSete NATURAL JOIN OmrådeTilSete) AS S
        WHERE   (Område = ? AND RadNr = ? AND
                (Område, RadNr, SeteNr) NOT IN  (SELECT Område, RadNr, SeteNr
                                                FROM ((BillettOmråde NATURAL JOIN BillettRadNr)
                                                NATURAL JOIN BillettSeteNr)
                                                NATULAR JOIN BillettKjøpForestilling
                                                WHERE Tid = '18:30' AND Dato = 2024-02-03))""",
        (valgtRad[0], valgtRad[1],)
        )
        seter = cursor.fetchall()

        ### Sett inn de 9 setene som billetter
        for i in range(9):
            cursor.execute(
            """INSERT INTO BillettOmråde
            VALUES (?, ?, ?)""",
            (kjøpID, i, seter[i][0])
            )
            cursor.execute(
            """INSERT INTO BillettRadNr
            VALUES (?, ?, ?)""",
            (kjøpID, i, seter[i][1])
            )
            cursor.execute(
            """INSERT INTO BillettSeteNr
            VALUES (?, ?, ?)""",
            (kjøpID, i, seter[i][2])
            )
            cursor.execute(
            """INSERT INTO BillettType
            VALUES (?, ?, 1)""",
            (kjøpID, i, )
            )
        return kjøpID
    else:
        raise Exception("Not enough Avaiable Seats")

def printKjøp(ID):
    cursor.execute(
    """SELECT *
    FROM BillettSeteNr NATURAL JOIN BillettOmråde NATURAL JOIN BillettRadNr
    WHERE KjøpID = ?""",
    (ID,)
    )

    result = cursor.fetchall()

    for row in result:
        print(row)

def main():
    global cursor
    cursor = con.cursor()

    kjøpID = finnOgKjøpSeter()

    if len(sys.argv) == 2 and sys.argv[1] == '-f':
        printKjøp(kjøpID)        

    con.commit()
    con.close()

if __name__ == "__main__":
    main()