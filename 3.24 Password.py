password = "pass123"
answer = ""
number_of_try = 0
number_max_of_try = 8
max_try = "not reached"

while answer != password and max_try != 'reached':
    if number_of_try < number_max_of_try:
        answer = input("what is the password ")
        number_of_try = number_of_try + 1
    else:
        max_try = "reached"

if max_try == "reached":
    print("Account Blocked")
else:
    print("Access Granted")