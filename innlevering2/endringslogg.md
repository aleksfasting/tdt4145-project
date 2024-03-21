# Endringslogg

### Endringslogg fra del 1

**Vi har endret 2 av tabellene våre:**

- Sete(Område, RadNr, SeteNr)
- OmrådeISal(Område, Sal)

Vi har funnet at det ikke eksisterer en funksjonell avhengighet `Område->Sal`. Det kan altså være saler som har de samme områdenavnene. Vi antok at dette ikke var mulig, og at det dermed fantes en FA `Område->Sal` da vi gjorde del 1 av innleveringen, så vi må endre strukturen på databasen.

Vi har slått disse sammen til Sete(Sal, Område, RadNr, SeteNr).

Men denne har flere ikke trivielle MVD-er. For eksempel finnes en `Sal->>Rad`, hvor Sal ikke er en supernøkkel. Dermed er ikke den tabellen på 4NF. Løsningen vår er å introdusere en seteID også splitte opp tabellen i 2 eller 4. Hvilken vi velger er litt vilkårlig.

Denne tabellen har ingen funksjonelle avhengigheter.