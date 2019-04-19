import sqlite3 as lit

db = lit.connect("employee.db")

with db:
      cur = db.cursor()
      selectquery =  "SELECT * FROM employee1"
      cur.execute(selectquery)

      rows = cur.fetchall()


      for data in rows:
           print(data)

