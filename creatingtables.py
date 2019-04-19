import sqlite3 as lit

def main():
    try:
        db=lit.connect('employee.db')
        cur = db.cursor()

        tablequery= " CREATE TABLE employee1(empid INT PRIMARY KEY,firstname TEXT, lastname TEXT, dob TEXT, deptid INT)"

        cur.execute(tablequery)
        print("Employee1 table created successfully")



    except:
        print("Unable to create table")

    finally:
        db.close()

if __name__== "__main__":
    main()


