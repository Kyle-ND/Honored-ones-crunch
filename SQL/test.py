import sqlite3

# Connect to the database
conn = sqlite3.connect("fiftyville.db")
cursor = conn.cursor()

# Step 1: Identify suspects from crime scene reports
cursor.execute("""
    SELECT name 
    FROM crime_scene_reports 
    WHERE location = 'Humphrey Street' 
    AND date = '2023-07-28';
""")
suspects = cursor.fetchall()

# Print potential suspects
print("Potential suspects from crime scene reports:")
for suspect in suspects:
    print(suspect[0])

# # Step 2: Find interviews related to the crime
# cursor.execute("""
#     SELECT interviewee, account 
#     FROM interviews 
#     WHERE date = '2023-07-28';
# """)
# interviews = cursor.fetchall()

# print("\nInterview records:")
# for interview in interviews:
#     print(f"{interview[0]} reported: {interview[1]}")

# # Step 3: Check ATM transactions around the crime date
# cursor.execute("""
#     SELECT name, amount, transaction_time 
#     FROM atm_transactions 
#     WHERE transaction_time BETWEEN '2023-07-28 00:00:00' AND '2023-07-29 00:00:00';
# """)
# atm_transactions = cursor.fetchall()

# print("\nATM transactions around the crime date:")
# for transaction in atm_transactions:
#     print(f"Name: {transaction[0]}, Amount: {transaction[1]}, Time: {transaction[2]}")

# # Step 4: Check bakery security logs
# cursor.execute("""
#     SELECT name 
#     FROM bakery_security_logs 
#     WHERE timestamp BETWEEN '2023-07-28 00:00:00' AND '2023-07-28 23:59:59';
# """)
# bakery_visitors = cursor.fetchall()

# print("\nBakery security logs visitors:")
# for visitor in bakery_visitors:
#     print(visitor[0])

# # Step 5: Check flight records for suspects
# cursor.execute("""
#     SELECT passengers.name, flights.destination_city 
#     FROM passengers 
#     JOIN flights ON passengers.flight_id = flights.id 
#     WHERE flights.departure_date = '2023-07-28' 
#     AND passengers.name IN (
#         SELECT name FROM crime_scene_reports 
#         WHERE location = 'Humphrey Street' AND date = '2023-07-28'
#     );
# """)
# travel_info = cursor.fetchall()

# print("\nTravel records for suspects on the same day:")
# for record in travel_info:
#     print(f"Suspect: {record[0]}, Destination City: {record[1]}")

# # Step 6: Find accomplices by checking for co-passengers
# cursor.execute("""
#     SELECT DISTINCT p1.name AS accomplice, p2.name AS thief
#     FROM passengers p1 
#     JOIN passengers p2 ON p1.flight_id = p2.flight_id 
#     WHERE p1.name != p2.name
#     AND p2.name IN (
#         SELECT name FROM crime_scene_reports 
# """)