import random

def guess(hidden: int, answer: int):
    correct = False
    if answer != hidden:
        high_or_low(hidden, answer)
    else:
        correct = True
    return correct

def selection_phase(attempts:int):
    statement = ""
    if attempts == 5:
        statement = "Welcome, player! Guess the number between 1 to 100!"
    else:
        statement = "You can do it! Try again and guess another number between 1 to 100!"
    return statement

def high_or_low(hidden:int, answer:int):
    print("Wrong number! \n")
    if hidden > answer:
        print("The hidden number is greater than your chosen answer: ", answer)
    else:
        print("The hidden number is lesser than your chosen answer: ", answer)


def main():
    result = False
    hidden_num = random.randint(1, 100)
    no_of_attempts = int(5)

    while no_of_attempts != 0:
        print(selection_phase(no_of_attempts))
        answer_attempt = int(input("What is your guess? "))

        result = guess(hidden_num, answer_attempt)

        if result:
            break
        else:
            no_of_attempts -= 1

    if result:
        print('You got the correct number, ', hidden_num)
    else:
        print('The correct answer is: ', hidden_num)

main()
