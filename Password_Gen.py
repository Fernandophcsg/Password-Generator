import string
import random

charactors = list(string.ascii_letters + string.digits + "!@#$%*&()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(charactors)

    password = []

    for x in range(password_length):
        password.append(random.choice(charactors))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate password?(Yes/No): ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended")
    quit()
else:
    print("Invalid input, Please input yes or No")
    quit()