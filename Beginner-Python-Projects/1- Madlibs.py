while True:
    quitGame = input("Are you ready to play Madlib? (y or n) -->".lower())
    if quitGame == "y":
        adjective = input("Adjective: ")
        verbOne = input("Verb: ")
        verbTwo = input("Verb: ")
        famousPerson = input("Famous Person:")

        madlib = f"Computer programming is so {adjective}! It makes me so excited all the time because. I love to {verbOne}.\
        Stay hydrated and {verbTwo} like you are {famousPerson}!"
        print(madlib)
    elif quitGame == "n":
        print("Goodbye :(")
        break
    else:
        print("oops. You made an incorrect entry.")




