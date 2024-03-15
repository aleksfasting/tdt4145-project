SELECT SpillerRolle.RolleNavn, Person.Navn, Teaterstykke.Navn
FROM Teaterstykke NATURAL JOIN SpillerRolle
     JOIN Person ON Spiller.Rolle.PID = Person.PID
