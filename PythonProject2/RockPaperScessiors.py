import random
def play():
    user = input("enter your choice: ")
    print(user)
   
    # computer have random choice
    computer= random.choice(['r', 'p', 's'])
    # if user win falls into this conditon
    if(user == computer):
        return 'oh! Its a tie'

    if is_winner(user,computer):
        return 'you won!'
    else:
        return 'computer won'

def is_winner(player,opponent):
    # return true if playe win
    # r>s s>p p>r 
    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
