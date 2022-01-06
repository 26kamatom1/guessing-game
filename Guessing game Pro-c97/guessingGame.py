import random
print("number guessing game")
number = random.randint(1, 9) 
chances = 1
print("Guess a number (between 1 and 9):")
while chances < 6:
    guess=int(input("enter your guess:- "))
    if guess==number:
        print("Congratulations you won!")
        break
    elif guess<number:
        print("Your guess was too low: Guess a number higher than", guess)
    else:
        print("Your guess was too high: Guess a number lower than", guess)
    chances +=1
    if not chances<6:
        print("You lose :( The number is", number)