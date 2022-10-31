import random

no = [1, 2, 3, 4, 5, 6]
x = 0
p = 0  #p is player
c = 0  #c is computer variable
pScore = 0
cScore = 0
try:
    while x < 3:

        number = int(input("Insert any number between 1 to 6:"))
        no1 = int(random.choice(no))
        print("Computer rolled:", no1)
        print("Player rolled:", number)
        if number > no1:
            print("Player wins")
            p += 1

        elif no1 > number:
            print("Computer wins")
            c += 1

        else:
            print("The match was draw")  #no point for both
        x += 1

    pScore = p
    cScore = c
except:
    print("You input other than integer")

finally:
    print("Thank you for playing")
    print("\n### Game Over ###\n")
    print("Computer scored:", cScore)
    print("Player scored:", pScore)
