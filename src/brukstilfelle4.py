#from connection import con
import datetime

### Funksjon for å sjekke at datoen er gyldig
def checkDate(dateArg):

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


### Spør bruker om gyldig dato
date = input("Date: (yyyy-mm-dd) ")    
checkDate(date)