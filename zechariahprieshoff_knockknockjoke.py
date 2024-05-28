#Zechariah Prieshoff
#Knock Knock Joke
#May 10, 2024
#This program will tell the user a Knock Knock Joke using prints, ifs, and else statements.

name = input("Hi! What's your name?: ")
joke= input(f"Nice to meet you {name}! Do you want to hear a joke? (Enter Yes or No): ")

if joke == "Yes" or joke == "yes":
    print("Great!")
    print("Knock knock!")
    response1 = input()
    if response1 == "Who's there?" or response1 == "who's there?":
        print("Ivana.")
        response2 = input()
        if response2 == "Ivana who?" or response2 == "ivana who?":
            print("Ivana suck your blood! Blah, blah, blah.")
        else:
            print("Thats not how knock knock jokes work. You were supposed to say 'Ivana who?'")
    else:
        print("This is what's wrong with todays world. People can't even follow a simple knock knock joke! You were supposed to say 'Who's there?'")
else:
    print(":(")
    