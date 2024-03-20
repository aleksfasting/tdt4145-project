INSERT INTO Forestilling(`Dato`, `Tid`) VALUES 
    ('2024-02-01','19:00'),
    ('2024-02-02','19:00'),
    ('2024-02-03','19:00'),
    ('2024-02-05','19:00'),
    ('2024-02-06','19:00'),
    ('2024-02-03','18:30'),
    ('2024-02-06','18:30'),
    ('2024-02-07','18:30'),
    ('2024-02-12','18:30'),
    ('2024-02-13','18:30'),
    ('2024-02-14','18:30');

INSERT INTO TeaterStykke(`SID`, `Navn`, `Forfatter`, `Tid`) VALUES 
    (1, 'Kongsemnene', 'Henrik Ibsen', 19.00),
    (2, 'Størst av alt er kjærligheten', 'Jonas Corell Petersen', 18.30);

INSERT INTO Sal(`SalNavn`, `SID`) VALUES 
    ('Hovedscenen', 1),
    ('Gamle Scene', 2);

INSERT INTO Akt(`SID`, `AktNr`, `AktNavn`) VALUES 
    (1, 1, NULL),
    (1, 2, NULL),
    (1, 3, NULL),
    (1, 4, NULL),
    (1, 5, NULL),
    (2, 1, NULL);

INSERT INTO Rolle(`SID`, `RolleNavn`) VALUES 
    (1,'Haakon Haakonssønn'),
    (1,'Inga fra Vartejg'),
    (1,'Skule Jarl'),
    (1, 'Fru Ragnhild'),
    (1, 'Margrete'),
    (1, 'Sigrid/Ingebjørg'),
    (1, 'Biskop Nikolas'),
    (1, 'Gregorius Jonssønn'),
    (1, 'Paal Flida/Trønder'),
    (1, 'Baard Bratte/Trønder'),
    (1, 'Jatgeir Skald/Dagfinn Bonde'),
    (1, 'Peter'),
    (2,'Sunniva Du Mond Nordal'),
    (2,'Jo Sabiernak'),
    (2,'Marte M. Steinsholt'),
    (2,'Tor Ivar Hagen'),
    (2,'Trond-Ove Skrødal'),
    (2,'Natalie Grøndahl Tangen'),
    (2,'Åsmund Flaten');

INSERT INTO Person(`PID`,`Navn`,`Epost`,`Status`) VALUES 
    (1,'Arturo Scotti','arsc@gmail.com', 'Freelance'),
    (2,'Ingunn Beate Strige Øyen', 'inøy@gmail.com', 'Freelance'),
    (3,'Hans Petter Nilsen', 'hani@gmail.com', 'Freelance'),
    (4,'Madeleine Brandtzæg', 'mabr@gmail.com', 'Freelance'),
    (5,'Synnøve Fossum Eriksen', 'syer@gmail.com', 'Freelance'),
    (6,'Emma Caroline Deichmann', 'emde@gmail.com', 'Freelance'),
    (7,'Thomas Jensen Takyi', 'thta@gmail.com', 'Freelance'),
    (8,'Per Bogstad Gulliksen', 'pegu@gmail.com', 'Freelance'),
    (9, 'Isak Holmen Sørensen', 'issø@gmail.com', 'Freelance'),
    (10,'Fabian Heidelberg Lunde', 'falu@gmail.com', 'Freelance'),
    (11,'Emil Olafsson', 'emol@gmail.com', 'Freelance'),
    (12,'Snorre Ryen Tøndel', 'sntø@gmail.com', 'Freelance'),
    (13,'Yury Butusov','yubu@gmail.com', 'Freelance'),
    (14,'Aleksandr Shishkin-Hokusai','alsh@gmail.com', 'Freelance'),
    (15,'Eivind Myren','eimy@gmail.com', 'Freelance'),
    (16,'Mina Rype Stokke','mist@gmail.com', 'Freelance'),
    (17,'Sunniva Du Mond Nordal','suno@gmail.com', 'Freelance'),
    (18,'Jo Sabiernak','josa@gmail.com', 'Freelance'),
    (19,'Marte M. Steinsholt', 'mast@gmail.com', 'Freelance'),
    (20,'Tor Ivar Hagen', 'toha@gmail.com', 'Freelance'),
    (21,'Trond-Ove Skrødal','trsk@gmail.com', 'Freelance'),
    (22,'Natalie Grøndahl Tangen', 'nata@gmail.com', 'Freelance'),
    (23,'Åsmund Flaten', 'åsfl@gmail.com', 'Freelance'),
    (24,'Jonas Corell Petersen','jope@gmail.com', 'Freelance'),
    (25,'David Gehrt', 'dage@gmail.com', 'Freelance'),
    (26,'Gaute Tønder','gatø@gmail.com', 'Freelance'),
    (27,'Magnus Mikaelsen', 'mami@gmail.com', 'Freelance'),
    (28,'Kristoffer Spender', 'krsp@gmail.com', 'Freelance');

INSERT INTO Skuespiller(`PID`) VALUES 
    (1),
    (2),
    (3),
    (4),
    (5),
    (6),
    (7),
    (8),
    (9),
    (10),
    (11),
    (12),
    (17),
    (18),
    (19),
    (20),
    (21),
    (22),
    (23);

INSERT INTO Personell(`PID`) VALUES
    (13),
    (14),
    (15),
    (16),
    (24),
    (25),
    (26),
    (27),
    (28);

    /* Kongsemnene */
INSERT INTO RolleIAkt(`SID`,`RolleNavn`,`AktNr`) VALUES
    (1, 'Haakon Haakonssønn', 1),
    (1, 'Haakon Haakonssønn', 2),
    (1, 'Haakon Haakonssønn', 3),
    (1, 'Haakon Haakonssønn', 4),
    (1, 'Haakon Haakonssønn', 5),
    (1, 'Inga fra Vartejg', 1),
    (1, 'Inga fra Vartejg', 3),
    (1, 'Skule Jarl', 1),
    (1, 'Skule Jarl', 2),
    (1, 'Skule Jarl', 3),
    (1, 'Skule Jarl', 4),
    (1, 'Skule Jarl', 5),
    (1, 'Fru Ragnhild', 1),
    (1, 'Fru Ragnhild', 5),
    (1, 'Margrete', 1),
    (1, 'Margrete', 2),
    (1, 'Margrete', 3),
    (1, 'Margrete', 4),
    (1, 'Margrete', 5),
    (1, 'Sigrid/Ingebjørg', 1),
    (1, 'Sigrid/Ingebjørg', 2),
    (1, 'Sigrid/Ingebjørg', 5),
    (1, 'Biskop Nikolas', 1),
    (1, 'Biskop Nikolas', 2),
    (1, 'Biskop Nikolas', 3),
    (1, 'Gregorius Jonssønn', 1),
    (1, 'Gregorius Jonssønn', 2),
    (1, 'Gregorius Jonssønn', 3),
    (1, 'Gregorius Jonssønn', 4),
    (1, 'Gregorius Jonssønn', 5),
    (1, 'Paal Flida/Trønder', 1),
    (1, 'Paal Flida/Trønder', 2),
    (1, 'Paal Flida/Trønder', 3),
    (1, 'Paal Flida/Trønder', 4),
    (1, 'Paal Flida/Trønder', 5),
    (1, 'Baard Bratte/Trønder', 1),
    (1, 'Jatgeir Skald/Dagfinn Bonde', 4),
    (1, 'Peter', 3),
    (1, 'Peter', 4),
    (1, 'Peter', 5);

    /* Størst av alt er kjærligheten */
INSERT INTO RolleIAkt(`SID`, `RolleNavn`, `AktNr`) VALUES
    (2,'Sunniva Du Mond Nordal',1),
    (2,'Jo Sabiernak',1),
    (2,'Marte M. Steinsholt',1),
    (2,'Tor Ivar Hagen',1),
    (2,'Trond-Ove Skrødal',1),
    (2,'Natalie Grøndahl Tangen',1),
    (2,'Åsmund Flaten',1);

INSERT INTO SpillerRolle(`PID`,`SID`,`RolleNavn`) VALUES
    (1, 1,'Haakon Haakonssønn'),
    (2, 1,'Inga fra Vartejg'),
    (3, 1,'Skule Jarl'),
    (4, 1, 'Fru Ragnhild'),
    (5, 1, 'Margrete'),
    (6, 1, 'Sigrid/Ingebjørg'),
    (7, 1, 'Biskop Nikolas'),
    (8, 1, 'Gregorius Jonssønn'),
    (9, 1, 'Paal Flida/Trønder'),
    (10, 1, 'Baard Bratte/Trønder'),
    (11, 1, 'Jatgeir Skald/Dagfinn Bonde'),
    (12, 1, 'Peter'),
    (17, 2,'Sunniva Du Mond Nordal'),
    (18, 2,'Jo Sabiernak'),
    (19, 2,'Marte M. Steinsholt'),
    (20, 2,'Tor Ivar Hagen'),
    (21, 2,'Trond-Ove Skrødal'),
    (22, 2,'Natalie Grøndahl Tangen'),
    (23, 2,'Åsmund Flaten');

INSERT INTO medvirker(`PID`,`SID`,`Jobb`) VALUES
    (13, 1, 'Regi og musikkutvelgelse'),
    (14, 1, 'Scenografi og kostymer'),
    (15, 1, 'Lysdesign'),
    (16, 1, 'Dramaturg'),
    (24, 2, 'Regi'),
    (25, 2, 'Scenografi og kostymer'),
    (26, 2, 'Musikalsk ansvarlig'),
    (27, 2, 'Lysdesign'),
    (28, 2, 'Dramaturg');

INSERT INTO Type(`TypeID`, `Navn`, `Pris`) VALUES
    (1, 'Voksen', 199.99);