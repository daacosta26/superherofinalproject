""" Superhero quiz game"""

__author__ = "Daniel Acosta"


def main():
    """executes the program"""
    name = input('What is your name?\n')
    # asks for the user's name
    print('Hello, ' + name + ' welcome to the Superhero Quiz Game!', end=' \n',
          sep='= ')
    # welcomes the user to the game
    print('Type the number of the answer you choose')
    # explains how to answer the question and receives input from user
    print('Question 1: Which newspaper company does Spider-man work for?')
    # shows the question to the user
    print('1. The Daily Bugle')
    print('2. The Daily Planet')
    print('3. The Daily Gotham')
    print('4. The Daily Metropolis')
    # shows the answer choices to the user
    score = 0
    # sets the score to zero
    while True:
        try:
            answer = int(input('What is the correct answer?\n'))
            # asks the user for input
            break
        except ValueError:
            print("Error. Must be an answer choice.")
            # if the user does not input an answer choice an error is shown
    if answer == 1:
        print('correct')
        # shows user is correct if the answer is 1
        score += 10
    # adds points to the score
    else:
        print('incorrect')
    # shows user is incorrect if the answer is not 1

    print("Question 2: What is the name of Batman's father?")
    print('1. Thomas Wayne')
    print('2. Terry Wayne')
    print('3. Bob Wayne')
    print('4. William Wayne')
    while True:
        try:
            answer = int(input('What is the correct answer?\n'))
            break
        except ValueError:
            print("Error. Must be a answer choice.")
    if answer == 1:
        print('correct')
        # shows user is correct if the answer is 1
        score += 10
    # adds points to the score
    else:
        print('incorrect')

    print("Question 3: What is Superman's Kryptonian name?")
    print('1. Kal-El')
    print('2. Jor-El')
    print('3. Kool-El')
    print('4. Clark-El')
    while True:
        try:
            answer = int(input('What is the correct answer?\n'))
            break
        except ValueError:
            print("Error. Must be an answer choice.")
    if answer == 1:
        print('correct')
        # shows user is correct if the answer is 1
        score += 10
    # adds points to the score
    else:
        print('incorrect')

    print(
        "Question 4: What is the name of the man who killed Batman's parents?")
    print('1. Joe Kill')
    print('2. Joe Chill')
    print('3. The Joker')
    print('4. Joe Mama')
    while True:
        try:
            answer = int(input('What is the correct answer?\n'))
            break
        except ValueError:
            print("Error. Must be an answer choice.")
    if answer == 2:
        print('correct')
        # shows user is correct if the answer is 2
        score += 10
    # adds points to the score
    else:
        print('incorrect')

    print("Question 5: Which of these heroes is apart of the seven original "
          "Justice league members?")
    print('1. Shazam')
    print('2. The Flash')
    print('3. Cyborg')
    print('4. Aquaman')
    print('5. Green Arrow')
    while True:
        try:
            answer = int(input('What is the correct answer?\n'))
            break
        except ValueError:
            print("Error. Must be an answer choice.")
    if answer == 4 or answer == 2:
        print('correct')
        # shows user is correct if the answer is 4 or 2
        score += 10
    # adds points to the score
    elif answer == 3 or answer == 1:
        print("incorrect. They are in the movies, but not in the comics.")
        # shows the user is incorrect if their answer is 3 or 1
    else:
        print('incorrect')
        score %= 2
        # divides and gives the remainder

    print("Bonus Question: Who was the creator of the Batman Character?")
    print("1. Stan Lee")
    print("2. Tom Hardy")
    print("3. Bob Kane")
    print("4. David Goyer")
    while True:
        try:
            answer = int(input('What is the correct answer?\n'))
            break
        except ValueError:
            print("Error. Must be an answer choice.")
    if answer == 3:
        print('correct your score was doubled!')
        score *= 2
        # score is multiplied by 2
    else:
        score -= 1
        # score is subtracted
        print('incorrect')

    print(
        "Super Question: What was the first marvel movie to reference Doctor "
        "Strange?\n")
    print("1. Spider-Man 2(2004)")
    print("2. Avengers(2012)")
    print("3. Guardians of the Galaxy(2012)")
    print('4. The Incredible Hulk(2008)')
    while True:
        try:
            answer = int(input('What is the correct answer?\n'))
            break
        except ValueError:
            print("Error. Must be an answer choice.")
    if answer == '1':
        print('correct,your score has increased exponentially!')
        score **= 2
        # score is increased to the second power
    else:
        score //= 2
        # divides and rounds the result down to the nearest whole number
        print('incorrect')
        print(' ')

    print("Thanos question: How many infinity stones are there")
    print("1. 5")
    print("2. 6")
    print('3. 8')
    print('4. 7')
    while True:
        try:
            answer = int(input('What is the correct answer?\n'))
            break
        except ValueError:
            print("Error. Must be an answer choice.")
    if answer == 2:
        print('correct!')
        score += 10
    else:
        score /= 2
        # score is divided by 2
        print('incorrect, your score has been reduced by 50%')
        print('there are six infinity stones,')
        print('*' * 6)
        # the star is printed 6 times
    stones = ["space", "reality", "power", 'mind', 'time', 'soul']
    for x in range(1):
        # The strings contained in the stones variable are printed once
        print(stones)

    def my_function(results, exclamation):
        """displays results when called"""
        print(results + " " + exclamation)

    dark = "1. Darkseid\n"
    hob = "2. Hobgoblin\n"
    grodd = "3. Gorilla Grodd\n"
    task = "4. Taskmaster\n"
    while True:
        try:
            chance = int(input("enter a number between 1 and 10\n"))
            if chance >= 3 or chance >= 4:
                # if the user inputs a number greater than 4 then the
                # question is given
                print(
                    "which of the following is a villain from the "
                    "DC universe?")
                print(dark + hob + grodd + task)
                # question is printed
                answer = int(input('What is the correct answer?\n'))
                if answer != 4 and not (answer == 2):
                    print('correct!')
                    score += 10
                else:
                    my_function("incorrect", "!")
            break
        except ValueError:
            print("Error. Must be an answer choice.")

    print('Congratulations! your score is :', score)
    # shows the final score to the user


if __name__ == "__main__":
    main()
