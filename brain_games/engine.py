from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def run_game(game):
    name = welcome_user()
    print(game.DESCRIPTION)  

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.generate_round_data()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()

        match user_answer:
            case val if val == str(correct_answer):
                print("Correct!")
            case _:
                print(f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return

    print(f"Congratulations, {name}!")


