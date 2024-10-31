import sqlite3

#To connect to a new database
crime_scene_list = []
interview_list = []
bakery_list = []
atm_list = []
flights_list = []
conn = sqlite3.connect('SQL/fiftyville.db')
cur = conn.cursor()

# display data
crime_scene = cur.execute("SELECT * FROM crime_scene_reports")
for row in crime_scene:#This gets me the crimes that happened on july 28 2023 at hamphrey street
    if "Humphrey Street" in row[4] and 2023 == row[1] and 7 == row[2] and 28 == row[3]:
        crime_scene_list.append(row) 

interviews = cur.execute("SELECT * FROM interviews")
for row in interviews:#This gets me the crimes that happened on july 28 2023 at hamphrey street
    if 2023 == row[2] and 7 == row[3] and 28 == row[4] :
        interview_list.append(row) 


bakery_logs = cur.execute("SELECT * FROM bakery_security_logs")
for row in bakery_logs:#This gets me the crimes that happened on july 28 2023 at hamphrey street
    if 2023 == row[1] and 7 == row[2] and 28 == row[3] and 10 == row[4] and 15 == row[5] :
        bakery_list.append(row)

atm_trans = cur.execute("SELECT * FROM atm_transactions")
for row in atm_trans:#This gets me the crimes that happened on july 28 2023 at hamphrey street
    if 2023 == row[2] and 7 == row[3] and 28 == row[4] and "Humphrey Lane" in row[5]:
        atm_list.append(row)

# bank_acc = cur.execute("SELECT * FROM bank_accounts")
# for row in bank_acc:#This gets me the crimes that happened on july 28 2023 at hamphrey street
#     # if 2023 == row[2] and 7 == row[3] and 28 == row[4] and "Humphrey Lane" in row[5]:
#         print(row)

# airports = cur.execute("SELECT * FROM airports")
# for row in airports:#This gets me the crimes that happened on july 28 2023 at hamphrey street
#     # if 2023 == row[2] and 7 == row[3] and 28 == row[4] and "Humphrey Lane" in row[5]:
#         print(row)

flights = cur.execute("SELECT * FROM flights")
for row in flights:#This gets me the crimes that happened on july 28 2023 at hamphrey street
    if 2023 == row[3] and 7 == row[4] and 28 == row[5] and row[5] > 10:
        flights_list.append(row)

# calls = cur.execute("SELECT * FROM phone_calls")
# for row in calls:#This gets me the crimes that happened on july 28 2023 at hamphrey street
#     if 2023 == row[3] and 7 == row[4] and 28 == row[5]:
#         print(row)

#To close connection
cur.close()
conn.close()
