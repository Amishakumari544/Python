  # returns random  number for  us
import random
def guessNumber(a):
    random_num = random.randint(2, a)
    guessNumber=6
    while guessNumber != random_num:
        guessNumber=int(input(f'guess the random number'))
        if(guessNumber>random_num):
            print("too high,try again")
        elif(guessNumber<random_num):
            print("too low,try again")
        else:
            print(f"that's good correct {random_num} ")    
        print(guessNumber)

guessNumber(10)
    # thank you 


 