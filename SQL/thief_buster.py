import sqlite3

#To connect to a new database
conn = sqlite3.connect('SQL/fiftyville.db')
cur = conn.cursor()

# display data
member_data = cur.execute("SELECT * FROM crime_scene_reports")
for row in member_data:#This gets me the crimes that happened on july 28 2023 at hamphrey street
    if "Humphrey Street" in row[4] and 2023 == row[1] and 7 == row[2] and 28 == row[3]:
        print(row)        

#To close connection
cur.close()
conn.close()