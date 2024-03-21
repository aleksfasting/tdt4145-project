import subprocess as sb

sb.run(["python3", "./connection.py"])

print("\nLaget `teaterDB.db`\n")

sb.run(["sqlite3", "teaterDB.db", ".read create-tables.sql"])

print("\nLaget tabeller\n")

print("\nOPPGAVE 1:")
sb.run(["sqlite3", "teaterDB.db", ".read oppgave1.sql"])
sb.run(["python3", "./oppgave1.py"])
print("    Satt inn tupler\n")

print("\nOPPGAVE 2:")
sb.run(["python3", "./oppgave2.py"])
print("    Satt inn kjøp\n")

print("\nOPPGAVE 3:")
sb.run(["python3", "./oppgave3.py"])
print("    Satt inn 9 nye kjøp på ledige rader")

print("\nOPPGAVE 4:")
sb.run(["python3", "./oppgave4.py"], input="2024-02-03\n", text=True)
print("\n    Hentet tabell\n")

print("\nOPPGAVE 5:")
sb.run(["sqlite3", "teaterDB.db", ".read oppgave5.sql"])
print("\n    Hentet tabell\n")

print("\nOPPGAVE 6:")
sb.run(["sqlite3", "teaterDB.db", ".read oppgave6.sql"])
print("\n    Hentet tabell")

print("\nOPPGAVE 7:")
sb.run(["python3", "./oppgave7.py"], input="Artuto Scotti\n", text=True)
print("    Hentet tabell\n")