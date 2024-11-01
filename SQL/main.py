import sqlite3

"""
How to use SQlite3 modulwe:
1) Call sqlite3.connect() to create a connection to the database in the current working directory, implicitly creating it if it 
does not exist:
2)In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor. 
3)Now that we've got a database connection and a cursor, we can create a database table, in this case the tables exist
4) Execute that query by calling cur.execute(...), assign the result to res, and call res.fetchone() to fetch the resulting row:
"""

def main():
    print(crime_scene_reports())

def crime_scene_reports():
    crime_scenes = []

    connection = sqlite3.connect("SQL/fiftyville.db")
    cursor = connection.cursor()

    resolution = cursor.execute("SELECT * FROM crime_scene_reports")
    for entry in resolution:
        if "Humphrey Street" in entry[4] and 7 == entry[2] and 28 == entry[3]:
            crime_scenes.append(entry[5])
            print(crime_scenes)


    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
