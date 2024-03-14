from connection import con

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
    #Aleks, do your thing
    e

def SettInnAkt():
    
    con.execute("INSERT INTO Sal VALUES (1, 1, NULL)")
    con.execute("INSERT INTO Sal VALUES (1, 2, NULL)")
    con.execute("INSERT INTO Sal VALUES (1, 3, NULL)")
    con.execute("INSERT INTO Sal VALUES (2, 1, NULL)")
    
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
    con.execute("INSERT INTO Rolle VALUES (2, 'Jo Sabiernak')")
    con.execute("INSERT INTO Rolle VALUES (2, 'Marte M. Steinsholt')")
    con.execute("INSERT INTO Rolle VALUES (2, 'Tor Ivar Hagen')")
    con.execute("INSERT INTO Rolle VALUES (2, 'Trond-Ove Skrødal')")
    con.execute("INSERT INTO Rolle VALUES (2, 'Natalie Grøndahl Tangen')")
    con.execute("INSERT INTO Rolle VALUES (2, 'Åsmund Flaten')")

    con.commit()
    con.close()

def SettInnPerson()
    
    con.execute("INSERT INTO Person VALUES (1),'Arturo Scotti',")
    con.execute("INSERT INTO Person VALUES (2),'Ingunn Beate Strige Øyen', ")
    con.execute("INSERT INTO Person VALUES (3),'Hans Petter Nilsen',")
    con.execute("INSERT INTO Person VALUES (4),'Madeleine Brandtzæg', ")
    con.execute("INSERT INTO Person VALUES (5),'Synnøve Fossum Eriksen',")
    con.execute("INSERT INTO Person VALUES (6),'Emma Caroline Deichmann',")
    con.execute("INSERT INTO Person VALUES (7),'Thomas Jensen Takyi',")
    con.execute("INSERT INTO Person VALUES (8),'Per Bogstad Gulliksen', ")
    con.execute("INSERT INTO Person VALUES (9), 'Isak Holmen Sørensen', ")
    con.execute("INSERT INTO Person VALUES (10),'Fabian Heidelberg Lunde', ")
    con.execute("INSERT INTO Person VALUES (11),'Emil Olafsson',")
    con.execute("INSERT INTO Person VALUES (12),'Snorre Ryen Tøndel',")

    con.execute("INSERT INTO Person VALUES (13),")
    con.execute("INSERT INTO Person VALUES (14),")
    con.execute("INSERT INTO Person VALUES (15),")
    con.execute("INSERT INTO Person VALUES (16),")

    con.execute("INSERT INTO Person VALUES (17,)")
    con.execute("INSERT INTO Person VALUES (18,)")
    con.execute("INSERT INTO Person VALUES (19,)")
    con.execute("INSERT INTO Person VALUES (20,)")
    con.execute("INSERT INTO Person VALUES (21,)")
    con.execute("INSERT INTO Person VALUES (22,)")
    con.execute("INSERT INTO Person VALUES (23,)")
    
    con.execute("INSERT INTO Person VALUES (24,)")
    con.execute("INSERT INTO Person VALUES (25,)")
    con.execute("INSERT INTO Person VALUES (26,)")
    con.execute("INSERT INTO Person VALUES (27,)")
    con.execute("INSERT INTO Person VALUES (28,)")


    CREATE TABLE Person (
    PID INT PRIMARY KEY,
    Navn VARCHAR(50),
    Epost VARCHAR(50),
    Status VARCHAR(50)
);

