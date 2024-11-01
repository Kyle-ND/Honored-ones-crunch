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
    if 2023 == row[2] and 7 == row[3] and 28 == row[4] and "Leggett Street" in row[5]:
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


# print("Crime report:")
# for i in range(len(crime_scene_list)):
#     if "CS50 duck" in str(crime_scene_list[i]):
#         print(crime_scene_list[i], "\n*************************************************************************")
#         print()
     
print("Corrisponding invterviews:")
for i in range(len(interview_list)):
    if "bakery" in str(interview_list[i]):
        print(interview_list[i], "\n")
print("*********************************************************************************************")
    

print("Thief's car number plate is one these")
num_plates = []
for i in range(len(bakery_list)):# thiefs car number plates
    bakery_split = str(bakery_list[i]).split(",")
    if int(bakery_split[5]) >= 16 and int(bakery_split[5]) <= 25:
        # print(bakery_list[i])
        num_plates.append(bakery_split[7].replace(")", ""))

# print(num_plates)
print("**********************************************************************************\n")
print("Main Suspects are:")
main_suspects = []
for i in range(len(people_list)):
     people_split = str(people_list[i]).split(",")
     for num in range(len(num_plates)):
        if num_plates[num] in people_split[4]: 
            print(people_list[i])
            main_suspects.append(people_list[i])
# print(main_suspects, "\n")
# print("The call's under 60 minutes")
suspects_calls = []
for i in range(len(call_list)):
     call_split = str(call_list[i]).split(",")
     call_split2 = call_split[6].split(")")
     if int(call_split2[0]) < 60:
        # print(call_list[i], "\n")
        suspects_calls.append(call_list[i])

print("\nAter cross referencing main suspects and calls under 60 minues:")
main_suspects_calls = []
for i in range(len(suspects_calls)):
    suspects_calls_splt = str(suspects_calls[i]).split(",")
    main_suspects_split = str(main_suspects)
    #  for main in range(len(main_suspects)):
    if main_suspects_split[2] in main_suspects_split[i]:
         print(suspects_calls[i])
         main_suspects_calls.append(suspects_calls[i])
print(main_suspects_calls)




# print("Widthrawals at Leggett Street ")
# withdraw = []
# for i in range(len(atm_list)):
#     atm_split = str(atm_list[i]).split(",")
#     if "withdraw" in atm_split[6]:
#         print(atm_list[i])
#         withdraw.append(atm_list[i])
# # print(withdraw)


print("flight out of Fiftyville tomorrow(29 july 2023) that the thief would have taken")
for i in range(len(flights_list)):
    flights_split = str(flights_list[i]).split(",")
    if  "8" in flights_split[6] and "20" in flights_split[7]:
        print(flights_list[i])
print("**********************************************************************************\n")

print("The thiefs destination.")

for i in range(len(airports_list)):
    airports_split = str(airports_list[i]).split(",")
    if "4" in airports_split[0]:
        print(airports_list[i])
        print("The thief fled to ", airports_split[3])
print("***************************************************")

# print("The thief is one of these people")


# print("The thief is... :")
# thiefs_num = "" 
# for i in range(len(people_list)):
#      people_split = str(people_list[i]).split(",")
#      if num_plates[1] in people_split[4]:
#           print(people_list[i])
#           thiefs_num = people_split[2]

# print(thiefs_num)
# print("******************************************************************")

# print("The call's under 60 minutes")
# suspects_calls = []
# for i in range(len(call_list)):
#      call_split = str(call_list[i]).split(",")
#      call_split2 = call_split[6].split(")")
#      if int(call_split2[0]) < 60:
#         #   print(call_list[i], "\n")
#           suspects_calls.append(call_list[i])

# # print(suspects_calls)
# print("**************************************************************")
# print("Thief's call recever num:")
# accomplice_num = ""
# for i in range(len(suspects_calls)):
#     suspects_calls_split = str(suspects_calls[i]).split(",")
#     if thiefs_num in suspects_calls_split[1]:
#         print(suspects_calls[i])
#         accomplice_num = suspects_calls_split[2]
# print(accomplice_num)

# print("*************************************************************************")
# accomplice_name = ""
# for i in range(len(people_list)):
#      people_split = str(people_list[i]).split(",")
#      if accomplice_num in people_split[2]:
#           print(people_list[i])
#           accomplice_name = people_split[1]

# print(accomplice_name)