import subprocess as sb

sb.run(["python3", "./connection.py"])

print("\nLaget `teaterDB.db`\n")

print('=============================================================================')

sb.run(["sqlite3", "teaterDB.db", ".read create-tables.sql"])

print("\nLaget tabeller\n")

print('=============================================================================')

print("\nOPPGAVE 1:")
sb.run(["sqlite3", "teaterDB.db", ".read oppgave1.sql"])
sb.run(["python3", "./oppgave1.py"])
print("    Satt inn tupler\n")

print('=============================================================================')

print("\nOPPGAVE 2:")
sb.run(["python3", "./oppgave2.py"])
print("    Satt inn kjøp\n")

print('=============================================================================')

print("\nOPPGAVE 3:")
sb.run(["python3", "./oppgave3.py"])
print("    Satt inn 9 nye kjøp på ledige rader\n")

print('=============================================================================')

print("\nOPPGAVE 4:    (input: '2024-02-03')\n")
sb.run(["python3", "./oppgave4.py"], input="2024-02-03\n", text=True)
print("\n    Hentet tabell\n")

print('=============================================================================')

print("\nOPPGAVE 5:\n")
sb.run(["sqlite3", "teaterDB.db", ".read oppgave5.sql"])
print("\n    Hentet tabell\n")

print('========================================================================')

print("\nOPPGAVE 6:\n")
sb.run(["sqlite3", "teaterDB.db", ".read oppgave6.sql"])
print("\n    Hentet tabell\n")

print('========================================================================')

print("\nOPPGAVE 7:    (input: 'Arturo Scotti')\n")
sb.run(["python3", "./oppgave7.py"], input="Arturo Scotti\n", text=True)
print("\n    Hentet tabell\n")