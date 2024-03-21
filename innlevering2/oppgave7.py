from connection import con

def finnSkuesplillere(navn):
    """SQL Select for å finne skuesplillere som har split sammen med 'navn'"""

    cursor.fetchall()

    cursor.execute(
        """SELECT DISTINCT P1.Navn AS Skuespiller1, P2.Navn AS SKUESPILLER2, TS.Navn AS Skuespill 
FROM    (((Person AS P1 NATURAL JOIN Skuespiller) NATURAL JOIN SpillerRolle AS SR1)
        NATURAL JOIN RolleIAkt AS RIA1)
        INNER JOIN
        (((Person AS P2 NATURAL JOIN Skuespiller) NATURAL JOIN SpillerRolle AS SR2)
        NATURAL JOIN RolleIAkt AS RIA2) ON (RIA1.SID = RIA2.SID AND RIA1.AktNr = RIA2.AktNr)
        INNER JOIN TeaterStykke AS TS ON (RIA1.SID = TS.SID)
        WHERE Skuespiller1 = ? AND NOT Skuespiller2 = ?""",
        (navn, navn)
        )

    return cursor.fetchall()

def printRelasjon(table): ### For å printe litt finere enn vanlig for lister
    for row in table:
        print(row)

def main():
    navn = input("Skuespiller: ")
    
    global cursor
    cursor = con.cursor()

    result = finnSkuesplillere(navn)

    printRelasjon(result)

    con.close()

if __name__ == '__main__':
    main()