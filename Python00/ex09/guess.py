import sys
import random

secret_number = random.randint(1, 99)
num_tries = 0;


while True:
    print (secret_number)
    user_input = input("Introduces 1 number between 1 - 99:")
    num_tries += 1


    if (user_input == "Exit"):
        break
    
    if (user_input.isnumeric() == False):
        print ("Input numeric value")
    else:
        if (int(user_input) > 99 or int(user_input) < 1):
            print ("Range not valid")

        if int(user_input) < secret_number:
            print("Too low!")
        elif int(user_input) > secret_number:
            print("Too high!")
        else :
            print(f"Congratulations {secret_number} in {num_tries} tries!")
            break;
