-- Active: 1709895968576@@127.0.0.1@3306@prosjekt

CREATE TABLE Kunde (
    MobilNr INT PRIMARY KEY,
    Navn VARCHAR(50),
    Adresse VARCHAR(50)
);

CREATE TABLE Forestilling (
    Dato DATE,
    Tid TIME,
    PRIMARY KEY (Dato, Tid)
);

CREATE TABLE TeaterStykke (
    SID INT PRIMARY KEY,
    Navn VARCHAR(50),
    Forfatter VARCHAR(50),
    Tid TIME
);

CREATE TABLE Sal (
    SalNavn VARCHAR(50),
    SID INT NOT NULL,
    PRIMARY KEY (SalNavn), 
    FOREIGN KEY (SID) REFERENCES TeaterStykke(SID)
);

CREATE TABLE SeteTilSete (
    SeteID INT NOT NULL,
    SeteNR INT,
    PRIMARY KEY (SeteID)
);

CREATE TABLE RadTilSete (
    SeteID INT NOT NULL,
    RadNr INT,
    PRIMARY KEY (SeteID)
);

CREATE TABLE OmrådeTilSete (
    SeteID INT NOT NULL,
    Område VARCHAR(50),
    PRIMARY KEY (SeteID)
);

CREATE TABLE SalTilSete (
    SeteID INT NOT NULL,
    SalNavn VARCHAR(50),
    PRIMARY KEY (SeteID),
    FOREIGN KEY (SalNavn) REFERENCES Sal(SalNavn)
);

CREATE TABLE Akt (
    SID INT,
    AktNr INT,
    AktNavn VARCHAR(50),
    PRIMARY KEY (SID, AktNr),
    FOREIGN KEY (SID) REFERENCES TeaterStykke(SID)
);

CREATE TABLE Rolle (
    SID INT,
    RolleNavn VARCHAR(50),
    PRIMARY KEY (SID, RolleNavn),
    FOREIGN KEY (SID) REFERENCES TeaterStykke(SID)
);

CREATE TABLE BillettKjøpKunde (
    KjøpID INT PRIMARY KEY,
    MobilNr INT NOT NULL,
    FOREIGN KEY (MobilNr) REFERENCES Kunde(MobilNr)
);

CREATE TABLE BillettKjøpsDato (
    KjøpID INT PRIMARY KEY,
    KjøpsDato DATE,
    KjøpsTid TIME,
    FOREIGN KEY (KjøpID) REFERENCES BillettKjøpKunde(KjøpID)
);

CREATE TABLE BillettKjøpForestilling (
    KjøpID INT PRIMARY KEY,
    Dato DATE NOT NULL,
    Tid TIME NOT NULL,
    FOREIGN KEY (KjøpID) REFERENCES BillettKjøpKunde(KjøpID),
    FOREIGN KEY (Dato, Tid) REFERENCES Forestilling(Dato, Tid)
);

CREATE TABLE Type (
    TypeID INT PRIMARY KEY,
    Navn VARCHAR(50),
    Pris DECIMAL(10, 2)
);

CREATE TABLE BillettType (
    KjøpID INT,
    Nummer INT,
    TypeID INT,
    PRIMARY KEY (KjøpID, Nummer),
    FOREIGN KEY (KjøpID) REFERENCES BillettKjøpKunde(KjøpID)
    FOREIGN KEY (TypeID) REFERENCES Type(TypeID)
);

CREATE TABLE BillettOmråde (
    KjøpID INT,
    Nummer INT,
    Område VARCHAR(100) NOT NULL,
    PRIMARY KEY (KjøpID, Nummer),
    FOREIGN KEY (KjøpID, Nummer) REFERENCES Billett(KjøpID, Nummer)
);

CREATE TABLE BillettRadNr (
    KjøpID INT,
    Nummer INT,
    RadNr INT NOT NULL,
    PRIMARY KEY (KjøpID, Nummer),
    FOREIGN KEY (KjøpID, Nummer) REFERENCES Billett(KjøpID, Nummer)
);

CREATE TABLE BillettSete (
    KjøpID INT,
    Nummer INT,
    SeteNr INT NOT NULL,
    PRIMARY KEY (KjøpID, Nummer),
    FOREIGN KEY (KjøpID, Nummer) REFERENCES Billett(KjøpID, Nummer)
);

CREATE TABLE RolleIAkt (
    SID INT NOT NULL,
    RolleNavn VARCHAR(50) NOT NULL,
    AktNr INT NOT NULL,
    PRIMARY KEY (SID, RolleNavn, AktNr),
    FOREIGN KEY (SID, RolleNavn) REFERENCES Rolle(SID, RolleNavn),
    FOREIGN KEY (SID, AktNr) REFERENCES Akt(SID, AktNr)
);

CREATE TABLE Person (
    PID INT PRIMARY KEY,
    Navn VARCHAR(50),
    Epost VARCHAR(50),
    Status VARCHAR(50)
);

CREATE TABLE Skuespiller (
    PID INT PRIMARY KEY,
    FOREIGN KEY (PID) REFERENCES Person(PID)
);

CREATE TABLE Personell (
    PID INT PRIMARY KEY,
    FOREIGN KEY (PID) REFERENCES Person(PID)
);

CREATE TABLE SpillerRolle (
    PID INT,
    SID INT,
    RolleNavn VARCHAR(50) NOT NULL,
    PRIMARY KEY (PID, SID, RolleNavn),
    FOREIGN KEY (PID) REFERENCES Skuespiller(PID),
    FOREIGN KEY (SID, RolleNavn) REFERENCES Rolle(SID, RolleNavn)
);

CREATE TABLE Medvirker (
    PID INT,
    SID INT,
    Jobb VARCHAR(50),
    PRIMARY KEY (PID, SID),
    FOREIGN KEY (PID) REFERENCES Personell(PID),
    FOREIGN KEY (SID) REFERENCES TeaterStykke(SID)
);
