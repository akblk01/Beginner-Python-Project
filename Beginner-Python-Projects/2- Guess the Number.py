import random

def guess (rangeNumber):
    randomNum = random.randint(1, rangeNumber)
    remainingRight = 5

    while True:
        number = int(input("Your Guess -->"))
        if remainingRight == 0:
            print("You lost")
            break
        elif remainingRight > 0:
            if number > randomNum:
                print(f"The number you entered is greater than expected. You should reduce it. Your remaining right: {remainingRight}")
                remainingRight -= 1

            elif number < randomNum:
                print(f"The number you entered is smaller than predicted. You should increase it. Your remaining right: {remainingRight}")
                remainingRight -= 1

            elif number == randomNum:
                print("Congratulations !")
                break

rangeNumber = int(input("What is the range of predictions from 1 to? -->"))

guess(rangeNumber)