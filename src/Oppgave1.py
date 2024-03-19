from connection import con
from brukstilfelle2 import leseDataGS, leseDataHS

def SettInnForestilling():

    con.execute("INSERT INTO Forestilling VALUES ('2024-02-01','19:00')")
    con.execute("INSERT INTO Forestilling VALUES ('2024-02-02','19:00')")
    con.execute("INSERT INTO Forestilling VALUES ('2024-02-03','19:00')")
    con.execute("INSERT INTO Forestilling VALUES ('2024-02-05','19:00')")
    con.execute("INSERT INTO Forestilling VALUES ('2024-02-06','19:00')")
    con.execute("INSERT INTO Forestilling VALUES ('2024-02-03','18:30')")
    con.execute("INSERT INTO Forestilling VALUES ('2024-02-06','18:30')")
    con.execute("INSERT INTO Forestilling VALUES ('2024-02-07','18:30')")
    con.execute("INSERT INTO Forestilling VALUES ('2024-02-12','18:30')")
    con.execute("INSERT INTO Forestilling VALUES ('2024-02-13','18:30')")
    con.execute("INSERT INTO Forestilling VALUES ('2024-02-14','18:30')")
    
    con.commit()
    con.close()

def SettInnStykker():

    con.execute("INSERT INTO TeaterStykke VALUES (1, 'Kongsemnene', 'Henrik Ibsen', 19.00)")
    con.execute("INSERT INTO TeaterStykke VALUES (2, 'Størst av alt er kjærligheten', 'Jonas Corell Petersen', 18.30)")

    con.commit()
    con.close()


def SettInnSal():

    con.execute("INSERT INTO Sal VALUES ('Hovedscenen', 1)")
    con.execute("INSERT INTO Sal VALUES ('Gamle Scene', 2)")

    con.commit()
    con.close()

def SettInnSete():
    cursor = con.cursor()
    #Aleks, do your thing

    seterGS = leseDataGS()
    for område in seterGS.keys():
        for radNr in range(len(seterGS[område])):
            for seteNr in range(len(seterGS[område][radNr])):
                cursor.execute(
"""INSERT INTO Sete
VALUES (?, ?, ?)""",
(område, radNr+1, seteNr + 1)
                )
    
    seterHS = leseDataHS()
    områderHS = ['Parkett', 'Galleri']
    seteNr = 0
    for område in områderHS:
        for radNr in range(len(seterHS[område])):
            for seteIRad in range(len(seterHS[område][radNr])):
                seteNr = seteNr + 1
                print(seteNr)
                cursor.execute(
"""INSERT INTO Sete
VALUES (?, ?, ?)""",
(område, radNr + 1, seteNr)
)
    
    con.commit()
    con.close()



def SettInnAkt():
    
    con.execute("INSERT INTO Akt VALUES (1, 1, NULL)")
    con.execute("INSERT INTO Akt VALUES (1, 2, NULL)")
    con.execute("INSERT INTO Akt VALUES (1, 3, NULL)")
    con.execute("INSERT INTO Akt VALUES (1, 4, NULL)")
    con.execute("INSERT INTO Akt VALUES (1, 5, NULL)")
    con.execute("INSERT INTO Akt VALUES (2, 1, NULL)")
    
    con.commit()
    con.close()
    
def SettInnRolle():
    
    con.execute("INSERT INTO Rolle VALUES (1,'Haakon Haakonssønn')")
    con.execute("INSERT INTO Rolle VALUES (1,'Inga fra Vartejg')")
    con.execute("INSERT INTO Rolle VALUES (1,'Skule Jarl')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Fru Ragnhild')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Margrete')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Sigrid')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Ingebjørg')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Biskop Nikolas')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Gregorius Jonssønn')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Paal Flida')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Trønder')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Baard Bratte')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Jatgeir Skald')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Dagfinn Bonde')")
    con.execute("INSERT INTO Rolle VALUES (1, 'Peter')")

    con.execute("INSERT INTO Rolle VALUES (2,'Sunniva Du Mond Nordal')")
    con.execute("INSERT INTO Rolle VALUES (2,'Jo Sabiernak')")
    con.execute("INSERT INTO Rolle VALUES (2,'Marte M. Steinsholt')")
    con.execute("INSERT INTO Rolle VALUES (2,'Tor Ivar Hagen')")
    con.execute("INSERT INTO Rolle VALUES (2,'Trond-Ove Skrødal')")
    con.execute("INSERT INTO Rolle VALUES (2,'Natalie Grøndahl Tangen')")
    con.execute("INSERT INTO Rolle VALUES (2,'Åsmund Flaten')")

    con.commit()
    con.close()

def SettInnPerson():
    
    con.execute("INSERT INTO Person VALUES (1,'Arturo Scotti','arsc@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (2,'Ingunn Beate Strige Øyen', 'inøy@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (3,'Hans Petter Nilsen', 'hani@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (4,'Madeleine Brandtzæg', 'mabr@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (5,'Synnøve Fossum Eriksen', 'syer@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (6,'Emma Caroline Deichmann', 'emde@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (7,'Thomas Jensen Takyi', 'thta@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (8,'Per Bogstad Gulliksen', 'pegu@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (9, 'Isak Holmen Sørensen', 'issø@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (10,'Fabian Heidelberg Lunde', 'falu@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (11,'Emil Olafsson', 'emol@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (12,'Snorre Ryen Tøndel', 'sntø@gmail.com', 'Freelance')")

    con.execute("INSERT INTO Person VALUES (13,'Yury Butusov','yubu@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (14,'Aleksandr Shishkin-Hokusai','alsh@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (15,'Eivind Myren','eimy@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (16,'Mina Rype Stokke','mist@gmail.com', 'Freelance')")

    con.execute("INSERT INTO Person VALUES (17,'Sunniva Du Mond Nordal','suno@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (18,'Jo Sabiernak','josa@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (19,'Marte M. Steinsholt', 'mast@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (20,'Tor Ivar Hagen', 'toha@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (21,'Trond-Ove Skrødal','trsk@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (22,'Natalie Grøndahl Tangen', 'nata@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (23,'Åsmund Flaten', 'åsfl@gmail.com', 'Freelance')")
    
    con.execute("INSERT INTO Person VALUES (24,'Jonas Corell Petersen','jope@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (25,'David Gehrt', 'dage@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (26,'Gaute Tønder','gatø@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (27,'Magnus Mikaelsen', 'mami@gmail.com', 'Freelance')")
    con.execute("INSERT INTO Person VALUES (28,'Kristoffer Spender', 'krsp@gmail.com', 'Freelance')")

    con.commit()
    con.close()

def SettInnSkuespillere():
    con.execute("INSERT INTO Skuespiller VALUES (1)")
    con.execute("INSERT INTO Skuespiller VALUES (2)")
    con.execute("INSERT INTO Skuespiller VALUES (3)")
    con.execute("INSERT INTO Skuespiller VALUES (4)")
    con.execute("INSERT INTO Skuespiller VALUES (5)")
    con.execute("INSERT INTO Skuespiller VALUES (6)")
    con.execute("INSERT INTO Skuespiller VALUES (7)")
    con.execute("INSERT INTO Skuespiller VALUES (8)")
    con.execute("INSERT INTO Skuespiller VALUES (9)")
    con.execute("INSERT INTO Skuespiller VALUES (10)")
    con.execute("INSERT INTO Skuespiller VALUES (11)")
    con.execute("INSERT INTO Skuespiller VALUES (12)")

    con.execute("INSERT INTO Skuespiller VALUES (17)")
    con.execute("INSERT INTO Skuespiller VALUES (18)")
    con.execute("INSERT INTO Skuespiller VALUES (19)")
    con.execute("INSERT INTO Skuespiller VALUES (20)")
    con.execute("INSERT INTO Skuespiller VALUES (21)")
    con.execute("INSERT INTO Skuespiller VALUES (22)")
    con.execute("INSERT INTO Skuespiller VALUES (23)")
    
    
def SettInnMedvirkende():
    con.execute("INSERT INTO Personell VALUES (13)")
    con.execute("INSERT INTO Personell VALUES (14)")
    con.execute("INSERT INTO Personell VALUES (15)")
    con.execute("INSERT INTO Personell VALUES (16)")

    con.execute("INSERT INTO Personell VALUES (24)")
    con.execute("INSERT INTO Personell VALUES (25)")
    con.execute("INSERT INTO Personell VALUES (26)")
    con.execute("INSERT INTO Personell VALUES (27)")
    con.execute("INSERT INTO Personell VALUES (28)")
    

def SettInnRelasjoner():
    #kongsemnene
    con.execute("INSERT INTO RolleIAkt VALUES(1, 1, 1)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 1, 2)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 1, 3)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 1, 4)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 1, 5)")

    con.execute("INSERT INTO RolleIAkt VALUES(1, 2, 1)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 2, 3)")

    con.execute("INSERT INTO RolleIAkt VALUES(1, 3, 1)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 3, 2)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 3, 3)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 3, 4)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 3, 5)")

    con.execute("INSERT INTO RolleIAkt VALUES(1, 4, 1)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 4, 5)")

    con.execute("INSERT INTO RolleIAkt VALUES(1, 5, 1)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 5, 2)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 5, 3)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 5, 4)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 5, 5)")

    con.execute("INSERT INTO RolleIAkt VALUES(1, 6, 1)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 6, 2)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 6, 5)")

    con.execute("INSERT INTO RolleIAkt VALUES(1, 7, 1)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 7, 2)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 7, 3)")

    con.execute("INSERT INTO RolleIAkt VALUES(1, 8, 1)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 8, 2)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 8, 3)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 8, 4)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 8, 5)")

    con.execute("INSERT INTO RolleIAkt VALUES(1, 9, 1)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 9, 2)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 9, 3)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 9, 4)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 9, 5)")

    con.execute("INSERT INTO RolleIAkt VALUES(1, 10, 1)")

    con.execute("INSERT INTO RolleIAkt VALUES(1, 11, 4)")

    con.execute("INSERT INTO RolleIAkt VALUES(1, 12, 3)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 12, 4)")
    con.execute("INSERT INTO RolleIAkt VALUES(1, 12, 5)")
