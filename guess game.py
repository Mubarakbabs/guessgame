import random
x = random.randint(1,9)
no_of_times = 0
win = 0
lose = 0
name = input ("Enter your name: ")
print ("Welcome", name)
while True:
    user = input("Guess the number: ")
    try:
        user = int(user)    except:
        print ("Enter a valid number")
        continue
    if user == x:
        print ("Correct!")
        print ("You won!")
        win = win + 1
        play_again = input ("Type any number to play again")
        try:
            int(play_again)
        except:
            break
        x = random.randint(1,9)
        no_of_times = 0
        continue
    else:
        no_of_times = no_of_times + 1
    if no_of_times%3 == 0:
        print ("Game over")
        print ("The correct number is", x)
        lose = lose + 1
    else:
        print ("Try again")
        continue
    play_again = input ("Type any number to play again")
    try:
        int(play_again)
    except:
        break
    x = random.randint(1,9)
    no_of_times = 0
    continue
print (name + "'s", "score", "Wins:", win, "Losses:", lose)
