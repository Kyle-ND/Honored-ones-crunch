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
    crime_scene_reports()
    interviews()
    print(bakery_security())



def crime_scene_reports():
    crime_scenes = []

    connection = sqlite3.connect("SQL/fiftyville.db")
    cursor = connection.cursor()

    crime_scene = cursor.execute("SELECT * FROM crime_scene_reports")
    for entry in crime_scene:
        if "Humphrey Street" in entry[4] and 7 == entry[2] and 28 == entry[3]:
            crime_scenes.append(entry[5])
            # print(crime_scenes)

    cursor.close()
    connection.close()


def interviews():
    interviews_list = []

    connection = sqlite3.connect("SQL/fiftyville.db")
    cursor = connection.cursor()

    interviews = cursor.execute("SELECT * FROM interviews")
    for entry in interviews:
        if 7 == entry[3] and 28 == entry[4]:
            interviews_list.append({entry[5]})
            # print(f"Witness: {entry[1]} Script: {entry[5]}\n")

    """
    Known:
    10min post theft, thief drove away, bakery parking lot
    Thief withdrawing money on Legget Street
    Thief called someone, call lasted less than a minute
    Thief planned to purchase earliest flight out of fiftyville, Did not purhcase own ticket

    Security cams, atms,phone calls, flights GO GO GO!!!!!!!!!!!
    """
    cursor.close()
    connection.close()


def bakery_security():

    license_plate_list = []

    connection = sqlite3.connect("SQL/fiftyville.db")
    cursor = connection.cursor()

    bakery_cam = cursor.execute("SELECT * FROM bakery_security_logs")
    for entry in bakery_cam:
        if 7 == entry[2] and 28 == entry[3] and 10 == entry[4] and entry[5]>= 16 and entry[5] <= 25 and "exit" in entry[6]:
            license_plate_list.append({entry[7]})
    
    print(f"{license_plate_list}\n")
    
    # Combined function

    people = cursor.execute("SELECT * FROM people")
    phone_number_list = []
    passport_list = []
    name_list = []

    for entry in people:
        for plate in license_plate_list:
            if plate in entry[4]:
                name_list.append({entry[1]})
                phone_number_list.append({entry[2]})
                passport_list.append({entry[3]})

    print(f"Name: {name_list}\nPhone number: {phone_number_list}\nPassport: {passport_list}")

                
    cursor.close()
    connection.close()



if __name__ == "__main__":
    main()
