SELECT SpillerRolle.RolleNavn, Person.Navn, Teaterstykke.Navn
FROM Teaterstykke NATURAL JOIN SpillerRolle
     JOIN Person ON SpillerRolle.PID = Person.PID
