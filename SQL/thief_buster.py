import sqlite3

#To connect to a new database
crime_scene_list = []
interview_list = []
bakery_list = []
atm_list = []
flights_list = []
people_list = []
airports_list = []
call_list = []
bank_account_list = []
passengers_list = []

conn = sqlite3.connect('SQL/fiftyville.db')
cur = conn.cursor()

# display data
crime_scene = cur.execute("SELECT * FROM crime_scene_reports")
for row in crime_scene:
    if "Humphrey Street" in row[4] and 2023 == row[1] and 7 == row[2] and 28 == row[3]:
        crime_scene_list.append(row) 

interviews = cur.execute("SELECT * FROM interviews")
for row in interviews:
    if 2023 == row[2] and 7 == row[3] and 28 == row[4] :
        interview_list.append(row) 

bakery_logs = cur.execute("SELECT * FROM bakery_security_logs")
for row in bakery_logs:
    if 2023 == row[1] and 7 == row[2] and 28 == row[3] and 10 == row[4] and row[5] <= 25 and row[5] >= 15 :
        bakery_list.append(row)

atm_trans = cur.execute("SELECT * FROM atm_transactions")
for row in atm_trans:
    if 2023 == row[2] and 7 == row[3] and 28 == row[4]:
        atm_list.append(row)

bank_acc = cur.execute("SELECT * FROM bank_accounts")
for row in bank_acc:
        bank_account_list.append(row)

flights = cur.execute("SELECT * FROM flights")
for row in flights:
    if 2023 == row[3] and 7 == row[4] and 29 == row[5] and row[5] > 10:
        flights_list.append(row)

calls = cur.execute("SELECT * FROM phone_calls")
for row in calls:
    if 2023 == row[3] and 7 == row[4] and 28 == row[5]:
            call_list.append(row)

people = cur.execute("SELECT * FROM people")
for row in people:
      people_list.append(row)

airports = cur.execute("SELECT * FROM airports")
for row in airports:
      airports_list.append(row)

passengers = cur.execute("SELECT * FROM passengers")
for row in passengers:
      passengers_list.append(row)

#To close connection
cur.close()
conn.close()

def get_crime_report():
    print("Crime report:")
    for i in range(len(crime_scene_list)):
        if "CS50 duck" in str(crime_scene_list[i]):
            print(crime_scene_list[i])
# get_crime_report()

def get_inteviews():
    print("Corrisponding invterviews:")
    for i in range(len(interview_list)):
        if "bakery" in str(interview_list[i]):
            print(interview_list[i], "\n")
# get_inteviews()

def get_exited_car():
     print("\nCars that left between 10:15 and 10:25 :")
     for i in range(len(bakery_list)):
          bakery_split = str(bakery_list[i]).split(",")
          if "10" in bakery_split[4] and int(bakery_split[5]) > 15 and int(bakery_split[5]) <= 25:
               print(bakery_split) 
get_exited_car()

def get_atm_withdrawals():
     print("\nATM transactions made at Leggett Street:")
     for i in range(len(atm_list)):
          atm_split = str(atm_list[i]).split(",")
          if "Leggett Street" in atm_split[5] and "withdraw" in atm_split[6]:
               print(atm_list[i])
get_atm_withdrawals()       

print("\nCalls made under 60 seconds:")
def get_calls():
    calls = []
    for i in range(len(call_list)):
        call_split = str(call_list[i]).split(",")
        if int(call_split[6].replace(")", "")) < 60:
             print(call_list[i])
             calls.append(call_list[i])
    # return calls             
get_calls()

def get_earliest_flight():
    #  print("\nEarliest flight out of Fiftyville tomorrow:")
     for i in range(len(flights_list)):
          flights_split = str(flights_list[i]).split(",")
          if int(flights_split[6].replace(")", "")) < 10 and int(flights_split[7].replace(")", "")) < 30:
               return ["\nEarliest flight out of Fiftyville tomorrow:", flights_list[i]]
print(get_earliest_flight()[0], "\n" ,get_earliest_flight()[1])

def get_escape_destination():
     flights_split = str(get_earliest_flight()[1]).split(",")
     for i in range(len(airports_list)):
          airport_split = str(airports_list[i]).split(",")
          if int(flights_split[2]) == int(airport_split[0].replace("(", "")):
               return [airports_list[i], airports_list[i][3]]
print("\nThe thief escaped to:\n", get_escape_destination()[0], "\n", get_escape_destination()[1])

print("\nSuspect passengers :")
def get_passenger():
    sus_passengerd = []
    for i in range(len(passengers_list)):
        passengers_split = str(passengers_list[i]).split(",")
        flight = int(get_earliest_flight()[1][0])
        if flight == int(passengers_split[0].replace("(", "")):
             sus_passengerd.append(passengers_list[i])
    return sus_passengerd
print(get_passenger())

print("\nSuspected people are :")
def get_people():
    sus_people = []
    for i in range(len(people_list)):
        people_split = str(people_list[i]).split(",")
        for passen in range(len(get_passenger())):
             passengers_split = str(get_passenger()[passen]).split(",")
             if passengers_split[1] in people_split[3]:
                  print(people_list[i])
                  sus_people.append(people_list[i])
    # return sus_people
get_people()

print("************************************************************************************************************")
print("Thief is either Bruce of Kesly their accomplic are either Robin for Bruce and Melisa or Larry for kelsey")
print("The thief fled to New York city")