from connection import con
import datetime

def checkDate(dateArg):
    """Sjekker at argumentet er en gyldig dato"""
    ### Sjekker at formatet stemmer
    dateList = dateArg.split('-')
    if (len(dateList) != 3 and len(dateList[0]) != 4 and len(dateList[1]) != 2 and len(dateList[2]) != 2):
        raise Exception("Date format must be (yyyy-mm-dd)")

    ### konverterer alle elementer til int  (for datetime.date())
    try:
        for i in range(3):
            dateList[i] = int(dateList[i])
    except:
        raise Exception("Date must be numbers")
    
    ### Sjekker at datoen finnes
    try:
        datetime.date(dateList[0],dateList[1], dateList[2])
    except (ValueError):
        raise Exception("Value of date is out of range")

def finnForestilling(date):
    """Finner alle forestillinger på en gitt dato"""
    cursor.execute(
    """SELECT SID, Navn, F.Dato, F.Tid, COUNT(KjøpID) AS AntallBilletter
    FROM    Forestilling AS F LEFT NATURAL JOIN (
            BillettKjøpForestilling NATURAL JOIN BillettSete)
            NATURAL JOIN TeaterStykke
    WHERE F.Dato = ?
    GROUP BY SID, Navn, F.Dato, F.Tid""",
    (date, )
    )

def printTable(table):
    """Printer tuplene slik at den ser litt bedre ut"""
    for tup in table:
        print(tup)


def main():
    ### Spør bruker om gyldig dato
    date = input("Select date: (yyyy-mm-dd) ")
    print()
    checkDate(date)

    global cursor
    cursor = con.cursor()

    finnForestilling(date)

    result = cursor.fetchall()
    printTable(result)

    con.commit()
    con.close()

if __name__ == "__main__":
    main()