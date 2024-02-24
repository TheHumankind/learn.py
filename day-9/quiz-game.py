def new_game():
    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key, e in enumerate(questions.keys()):
        print('----------------------------------')
        print(e)
        for j in options[questions_num - 1]:
            print(j)

        guesses.append(input('Enter (A, B, C, D): ').upper())
        correct_guesses += check_answer(questions.get(e), guesses[questions_num - 1])
        questions_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        return 1
    else:
        return 0


def display_score(correct_guesses, guesses):
    print('-----------------------')
    print('RESULTS')
    print('-----------------------')
    print('GUESSES: ', end="")
    for i in guesses:
        print(i, end="")
    print()
    print('ANSWERS: ', end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
    print('You score is: ' + str((correct_guesses / len(questions)) * 100) + '%')


def play_again():
    is_play = input('Do u want to play again? (Y/N): ').lower()
    if is_play == 'y':
        return True
    else:
        return False


questions = {
    'Who created Python?: ': 'A',
    'What year was Python created?: ': 'B',
    'Python is tribute to which comedy group?: ': 'C',
    'Is the Earth round?: ': 'A',
}

options = [
    ['A. Guido van Rossum', 'B. Elon Musk', 'C. Bill Gates', 'D. Mark Zuckerberg'],
    ['A. 1997', 'B. 1991', 'C. 2000', 'D. 2016'],
    ['A. Lonely Island', 'B. Smosh', 'C. Monty Python', 'D. SNL'],
    ['A. True', 'B. False', 'C. bla-bla-bla', 'D. What\'s Earth?'],
]

new_game()

while play_again():
    new_game()
