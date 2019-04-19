def main():
    try:
        db= lit.connect("department.db")
        print("Department database is created successfully")
        print("Department db")




    except:
         print("Failed to create database")


    finally:
        db.close()


if __name__==  "__main__":
     main()
