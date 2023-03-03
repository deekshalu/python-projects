from random import randint,choice

def choose_door(doors):
    return choice(doors) 

def place_money():
    doors = [False for i in range (3)]
    chosen_door = randint(0,2)
    doors[chosen_door] = True 
    return doors 

def trial():
    doors = place_money()
    player_choice = choose_door(doors)
    if player_choice:
        return 0 
    else:
        return 1

def main():
    total_trials = 1000
    correct_switch = 0 
    wrong_switch = 0

    for i in range(total_trials):
        correct_switch += trial()
    
    wrong_switch = total_trials - correct_switch
  
    print(correct_switch)
    print(wrong_switch)
    print(f"Probability of winning after switching {(correct_switch/total_trials)*100}%")
  

main()

"""
import random 

number_of_trials = 1000

for _ in range(number_of_trials):
    winning_door = random.randint(1,3)
    player_choice = random.randint(1,3)

    if winning_door == player_choice:
        better_to_stay += 1 

print(f'Were the player to stay, he would have won {(better_to_stay/number_of_trials)*100})
print(f'Were the player to stay, he would have won {(1-(better_to_stay/number_of_trials))*100})


"""

