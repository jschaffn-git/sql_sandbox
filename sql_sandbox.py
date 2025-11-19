    import mysql.connector

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_mysql_root_password", # Replace with your actual password
            database="your_database_name" # Optional: specify a database
        )
        print("Connected to MySQL!")

        # Example: Create a cursor and execute a query
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            print("MySQL connection closed.")
