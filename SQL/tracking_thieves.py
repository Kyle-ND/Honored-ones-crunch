from cs50 import SQL

def identify_thieves():
    database = SQL("sqlite:///fiftyville.db")

    #Acquiring crime scene data
    crime_scene_report = database.execute("SELECT * FROM crime_scene_reports WHERE year='2023' AND month='7' AND day='28' AND street = 'Humphrey Street' AND description LIKE '%cs50 duck%'")

    print('\nThe crime scene report reads:')
    print(crime_scene_report)

    #Acquiring witness reports
    print('\n\nNow we go through the statements by witnesses:')
    witness_testimony = database.execute("SELECT * FROM interviews WHERE year='2023' AND month='7' AND day='28'")
    print(witness_testimony)

    #Placing people at the crime scene
    print("\n\nThe details of the people who left the crime scene around the time the offense took place are as follows:")
    first_round_of_suspects = database.execute("SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year='2023' AND month='7' AND day='28' AND hour='10' AND minute BETWEEN '15' AND '25')")
    print(first_round_of_suspects)

    #Placing suspects who made an ATM transaction at Leggett Street
    print('\n\nOur shortlist of suspects is: ')
    second_round_of_suspects = database.execute("SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year='2023' AND month='7' AND day='28' AND hour='10' AND minute BETWEEN '15' AND '25') AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year='2023' AND month='7' AND day='28' AND atm_location='Leggett Street' AND transaction_type='withdraw'))")
    print(second_round_of_suspects)

    #Placing suspect who made a call
    print("\n\nA further shortlist of suspects is: ")
    third_round_of_suspects = database.execute("SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year='2023' AND month='7' AND day='28' AND hour='10' AND minute BETWEEN '15' AND '25') AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year='2023' AND month='7' AND day='28' AND atm_location='Leggett Street' AND transaction_type='withdraw')) AND phone_number IN (SELECT caller FROM phone_calls WHERE year='2023' AND month='7' AND day='28' AND duration<60)")
    print(third_round_of_suspects)

    #Placing suspect/s at the airport
    print("\n\nThe prime suspects are: ")
    prime_suspects = database.execute("SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year='2023' AND month='7' AND day='28' AND hour='10' AND minute BETWEEN '15' AND '25') AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year='2023' AND month='7' AND day='28' AND atm_location='Leggett Street' AND transaction_type='withdraw')) AND phone_number IN (SELECT caller FROM phone_calls WHERE year='2023' AND month='7' AND day='28' AND duration<60) AND passport_number IN (SELECT passport_number FROM passengers) AND (SELECT flight_id from passengers WHERE flight_id IN (SELECT id FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city='Fiftyville' AND year='2023' AND month='7' AND day='29')))")
    print(prime_suspects)
    
    print('\n\nThe flight times from Fiftyville on 29 July 2023 are as follows: ')
    flight_times = database.execute("SELECT hour,minute FROM flights WHERE year='2023' AND month='7' AND day='29' AND origin_airport_id IN (SELECT id FROM airports WHERE city = 'Fiftyville')")
    print(flight_times)

    print('\n\nThe ultimate prime suspect is: ')
    prime_suspect = database.execute("SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year='2023' AND month='7' AND day='28' AND hour='10' AND minute BETWEEN '15' AND '25') AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year='2023' AND month='7' AND day='28' AND atm_location='Leggett Street' AND transaction_type='withdraw')) AND phone_number IN (SELECT caller FROM phone_calls WHERE year='2023' AND month='7' AND day='28' AND duration<60) AND passport_number IN (SELECT passport_number FROM passengers) AND (SELECT flight_id from passengers WHERE flight_id IN (SELECT id FROM flights WHERE hour='8' AND minute='20' AND  origin_airport_id IN (SELECT id FROM airports WHERE city='Fiftyville' AND year='2023' AND month='7' AND day='29')))")
    print(prime_suspect)


identify_thieves()