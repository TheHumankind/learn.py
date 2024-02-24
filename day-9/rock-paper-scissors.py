import random

choices = ['rock', 'paper', 'scissors']
player = None


def show_result(computer_choice: str, player_choice: str, result: str):
    print('computer: ' + computer_choice)
    print('player: ' + player_choice)
    print('result: ' + result)


while True:
    computer = random.choice(choices)

    while player not in choices:
        player = input('Pick rock, paper or scissors: ')

    if player == computer:
        show_result(computer, player, 'TIE')
    elif ((player == 'rock' and computer != 'paper')
          or (player == 'paper' and computer != 'scissors')
          or (player == 'scissors' and computer != 'rock')):
        show_result(computer, player, 'WIN')
    else:
        show_result(computer, player, 'LOSE')

    end_game = input('Do u want play again (Y/N): ').lower()
    if end_game == 'n':
        break

    player = None
    computer = None
