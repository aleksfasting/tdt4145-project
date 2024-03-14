from connection import con

def LagTabeller():
     
    cursor = con.cursor()

    cursor.execute(
        '''
        CREATE TABLE Kunde (
            MobilNr INT PRIMARY KEY,
            Navn VARCHAR(50),
            Adresse VARCHAR(50)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE Forestilling (
            Dato DATE,
            Tid TIME,
            PRIMARY KEY (Dato, Tid)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE TeaterStykke (
            SID INT PRIMARY KEY,
            Navn VARCHAR(50),
            Forfatter VARCHAR(50),
            Tid TIME
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE Sal (
            SalNavn VARCHAR(50),
            SID INT NOT NULL,
            PRIMARY KEY (SalNavn), 
            FOREIGN KEY (SID) REFERENCES TeaterStykke(SID)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE Sete (
            Område VARCHAR(50),
            RadNr INT,
            SeteNr INT,
            PRIMARY KEY (Område, RadNr, SeteNr)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE OmrådeISal (
            Område VARCHAR(50),
            SalNavn VARCHAR(50) NOT NULL,
            PRIMARY KEY (Område, SalNavn),
            FOREIGN KEY (SalNavn) REFERENCES Sal(SalNavn)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE Akt (
            SID INT,
            AktNr INT,
            AktNavn VARCHAR(50),
            PRIMARY KEY (SID, AktNr),
            FOREIGN KEY (SID) REFERENCES TeaterStykke(SID)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE Rolle (
            SID INT,
            RolleNavn VARCHAR(50),
            PRIMARY KEY (SID, RolleNavn),
            FOREIGN KEY (SID) REFERENCES TeaterStykke(SID)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE BillettKjøpKunde (
            KjøpID INT PRIMARY KEY,
            MobilNr INT NOT NULL,
            FOREIGN KEY (MobilNr) REFERENCES Kunde(MobilNr)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE BillettKjøpsDato (
            KjøpID INT PRIMARY KEY,
            KjøpsDato DATE,
            KjøpsTid TIME,
            FOREIGN KEY (KjøpID) REFERENCES BillettKjøpKunde(KjøpID)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE BillettKjøpForestilling (
            KjøpID INT PRIMARY KEY,
            Dato DATE NOT NULL,
            Tid TIME NOT NULL,
            FOREIGN KEY (KjøpID) REFERENCES BillettKjøpKunde(KjøpID),
            FOREIGN KEY (Dato, Tid) REFERENCES Forestilling(Dato, Tid)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE Type (
            TypeID INT PRIMARY KEY,
            Navn VARCHAR(50),
            Pris DECIMAL(10, 2)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE Billett (
            KjøpID INT,
            Nummer INT,
            PRIMARY KEY (KjøpID, Nummer),
            FOREIGN KEY (KjøpID) REFERENCES BillettKjøpKunde(KjøpID)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE BillettOmråde (
            KjøpID INT,
            Nummer INT,
            Område VARCHAR(100) NOT NULL,
            PRIMARY KEY (KjøpID, Nummer),
            FOREIGN KEY (KjøpID, Nummer) REFERENCES Billett(KjøpID, Nummer)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE BillettRadNr (
            KjøpID INT,
            Nummer INT,
            RadNr INT NOT NULL,
            PRIMARY KEY (KjøpID, Nummer),
            FOREIGN KEY (KjøpID, Nummer) REFERENCES Billett(KjøpID, Nummer)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE BillettSete (
            KjøpID INT,
            Nummer INT,
            SeteNr INT NOT NULL,
            PRIMARY KEY (KjøpID, Nummer),
            FOREIGN KEY (KjøpID, Nummer) REFERENCES Billett(KjøpID, Nummer)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE RolleIAkt (
            SID INT NOT NULL,
            RolleNavn VARCHAR(50) NOT NULL,
            AktNr INT NOT NULL,
            PRIMARY KEY (SID, RolleNavn, AktNr),
            FOREIGN KEY (SID, RolleNavn) REFERENCES Rolle(SID, RolleNavn),
            FOREIGN KEY (SID, AktNr) REFERENCES Akt(SID, AktNr)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE Person (
            PID INT PRIMARY KEY,
            Navn VARCHAR(50),
            Epost VARCHAR(50),
            Status VARCHAR(50)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE Skuespiller (
            PID INT PRIMARY KEY,
            FOREIGN KEY (PID) REFERENCES Person(PID)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE Personell (
            PID INT PRIMARY KEY,
            FOREIGN KEY (PID) REFERENCES Person(PID)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE SpillerRolle (
            PID INT,
            SID INT,
            RolleNavn VARCHAR(50) NOT NULL,
            PRIMARY KEY (PID, SID, RolleNavn),
            FOREIGN KEY (PID) REFERENCES Skuespiller(PID),
            FOREIGN KEY (SID, RolleNavn) REFERENCES Rolle(SID, RolleNavn)
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE Medvirker (
            PID INT,
            SID INT,
            Jobb VARCHAR(50),
            PRIMARY KEY (PID, SID),
            FOREIGN KEY (PID) REFERENCES Personell(PID),
            FOREIGN KEY (SID) REFERENCES TeaterStykke(SID)
        );
        '''
    )

    con.commit()
    con.close()

LagTabeller()
