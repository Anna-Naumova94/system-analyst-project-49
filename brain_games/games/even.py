import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round_data():
    question_number = random.randint(1, 100)
    correct_answer = 'yes' if is_even(question_number) else 'no'
    return str(question_number), correct_answer
