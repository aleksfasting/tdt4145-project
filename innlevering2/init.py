from connection import con
import subprocess as sb

sb.run(["sqlite3", "teaterDB.db", ".read create-tables.sql"])

con.commit()
con.close()