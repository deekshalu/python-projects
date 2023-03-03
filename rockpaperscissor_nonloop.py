import random




def play(): 
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r','p','s'])




        if user == computer: 
            return "It's a tie"

# r > s, s > p, p > r

        if is_win(user, computer):
            return "you won!"

        else: 
            return "you lose"

def is_win(player, opponent):

# return true if player wins
# r > s, s > p, p > r 

    if (player == 'r' and opponent == 's'):
        return True

    elif (player == 's' and opponent == 'p'):
        return True
    
    elif (player == 'p' and opponent == 'r'):
        return True



print(play())
