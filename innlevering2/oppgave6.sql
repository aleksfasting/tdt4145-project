SELECT SID, Navn, F.Dato, F.Tid, COUNT(KjøpID) AS AntallBilletter
FROM    Forestilling AS F LEFT NATURAL JOIN (
        BillettKjøpForestilling NATURAL JOIN BillettSete)
        NATURAL JOIN TeaterStykke
GROUP BY SID, Navn, F.Dato, F.Tid
ORDER BY AntallBilletter DESC