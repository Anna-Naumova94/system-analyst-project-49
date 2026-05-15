import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round_data():
    # Генерируем два случайных числа
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f"{num1} {num2}"
    # Вычисляем правильный ответ и приводим к строке
    correct_answer = str(math.gcd(num1, num2))

    return question, correct_answer