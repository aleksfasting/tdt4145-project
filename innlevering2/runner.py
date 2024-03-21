import subprocess as sb

sb.run(["python3", "./connection.py"])

sb.run(["sqlite3", "teaterDB.db", ".read create-tables.sql"])

sb.run(["sqlite3", "teaterDB.db", ".read oppgave1.sql"])
sb.run(["python3", "./oppgave1.py"])

sb.run(["python3", "./oppgave2.py"])

# sb.run(["python3", "./oppgave3.py"])

sb.run(["python3", "./oppgave4.py"], input="2024-02-03\n", text=True)

sb.run(["sqlite3", "teaterDB.db", ".read oppgave5.sql"])

sb.run(["sqlite3", "teaterDB.db", ".read oppgave6.sql"])

sb.run(["python3", "./oppgave7.py"], input="Artuto Scotti\n", text=True)