import sqlite3 as lit


myemployees= (

    (101,'Deepa','K','26-03-1990',10),
    (102,'Chetana','Devi','26-11-1993',11),
    (103,'Uday','Kiran','27-02-1996',12),
    (104,'Vinod','S','24-10-1990',13),
    (105,'Waquas','Ashraf','09-01-1990',14),
    (106,'Sushma','C','08-11-1989',15),
)



db = lit.connect("employee.db")


with db:
    cur = db.cursor()
    cur.executemany('INSERT INTO employee1 VALUES (?,?,?,?,?)',myemployees)
    print("Data inserted successfully")
