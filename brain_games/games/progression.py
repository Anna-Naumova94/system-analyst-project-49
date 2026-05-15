import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start, step, length):
    progression = []
    for index in range(length):
        current_element = start + index * step
        progression.append(current_element)
    return progression


def generate_round_data():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)  

    progression = generate_progression(start, step, length)

    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])

    progression_strings = [str(x) for x in progression]
    progression_strings[hidden_index] = '..'
    
    question = " ".join(progression_strings)

    return question, correct_answer

