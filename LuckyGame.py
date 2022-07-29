import random
name = input("Enter your name: ")
print (f"welcome {name} to the digit guessing game")
lucky_num = random.randint(0, 100)
count = 0
for i in range (5):
    guess = int(input("Enter a number: "))
    count += 1
    if guess < lucky_num:
        if count == 5:
            print ("sorry, out of guesses")
        else:
            print ("you should guess more")
    elif guess > lucky_num:
        if count == 5:
            print ("sorry, out of guesses")
        else:
            print ("you should guess less")
    else:
        print ("congratulate you are a winner")
        print (count)
        break