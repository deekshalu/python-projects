import random 

min_value = 1
max_value = 6

roll_again = "yes"

while roll_again == "yes":
    print("Rolling the dices")
    print("The values are:")


    print(random.randint(min_value, max_value))
    print(random.randint(min_value, max_value))

    roll_again = input("Roll the dice again? Enter yes/no \n")