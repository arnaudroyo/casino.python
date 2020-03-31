import random
import time

pot = 0
while pot <= 0 or pot > 10000:
    try:
        pot = int(input("What's your begining pot ?"))
        assert pot > 0 and pot < 10000
    except AssertionError:
        print("Type a number bigger than 0 and smaller than 10000")
    except ValueError:
        print("Type a number")
        pot = 0
    
print("You start with ", pot,"€")

while pot > 0:
    number = -1
    while number <=0 or number >50:
        try:
            number = int(input("Bet on a number between 0 and 50"))
            assert number > 0 and number < 50
        except AssertionError:
            print("Type a number bigger than 0 and smaller than 50")
        except ValueError:
            print("Type a number")

    bet = -1        
    while bet <=0 or bet > pot:
        try:
            bet = int(input("Bet a amount of your pot:"))
            assert bet > 0 and bet < pot
        except AssertionError:
            print("Type a number bigger than 0 and smaller than ", pot)
        except ValueError:
            print("Type a number")

    print("You bet ", bet,"€ on number ", number,",Good luck !")
    time.sleep(2)
    print("Wheel is rolling..")    
    res = random.randint(1, 50)
    time.sleep(3)
    if res == number:
        pot += bet * 2
        print(res, " - GG")

    elif number % 2 == res % 2:
        print(res, " - You are refund")
    else:
        pot -= bet
        print(res," - lost, try again")
        
    print("You have ", pot,"€ left")
    time.sleep(3)
print("Not enough money to play again, sorry")






