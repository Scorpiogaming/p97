import random
print("number guessing game")
number=random.randint(1,9)
chances=0
print("guess any number between 1 and 9")
while chances<5:
    guess=int(input("enter the number now"))
    if guess==number:
        print ("you won")
        break
    elif guess<number:
        print("your guess was to low")
    else:
        print("your guess was too high")
    chances+=1
if not chances<5:
    print ("you losse the number is " ,guess)