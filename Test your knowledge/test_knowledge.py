import random
from history_q_and_r import questions
from history_q_and_r import answers
from art import logo
import os

print(logo)
print("Welcome to the Test Your Knowledge,\n"
      "a quizz about History !")

EASY = 15
MEDIUM = 30
HARD = 45


def difficulty():
    choice = input("choose your difficulty, Type easy, medium or hard\n"
                   "(easy = 15 questions, medium = 30 questions, hard = 45 questions): ").lower()
    if choice == "easy":
        return EASY
    if choice == "medium":
        return MEDIUM
    if choice == "hard":
        return HARD


def random_question():
    random_q = random.choice(questions)
    question = random_q["question"]
    return f"{question}"


def checker(value, list):
    list_of_bool = [True for elem in list
                    if value in elem.values()]

    if any(list_of_bool):
        return True
    else:
        return False


def game():
    score = 0
    turns = difficulty()
    replay = True

    while replay:

        while turns:

            print(random_question())

            value = input("Type your answer: ")
            check_answer = checker(value, answers)

            os.system('clear')

            if check_answer == True:
                print(f"Yes, '{value}' is the right answer.")
                score += 3
                print(f"Your score is {score}")
                turns -= 1

            else:
                print(f"No, '{value}' is the wrong answer.")
                print(f"Your score is {score}")
                turns -= 1

        os.system('clear')

        replay_choice = input("Do you want to replay the game ?").lower()
        if replay_choice == "no":
            replay = False
        else:
            game()

    print(f"Your final score is {score}")


if __name__ == "__main__":
    game()
