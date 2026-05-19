import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_round_data():
    question_number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(question_number) else 'no'
    
    return str(question_number), correct_answer
