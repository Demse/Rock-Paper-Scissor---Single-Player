def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

import random
while True:    
    play_game =input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        player_choice = input('Choose rock, paper or scissor ')
        cpu_choice = random.choice(['rock','paper','scissor'])

        print('cpu chose '+ cpu_choice)
        print('player chose ' +player_choice)

        if player_choice == 'rock' and cpu_choice == 'rock':
            print('It is a tie')
            game_on = False
        elif player_choice == 'rock' and cpu_choice == 'paper':
            print('Player Loses')
            game_on = False
        elif player_choice == 'rock' and cpu_choice == 'scissor':
            print('Player Wins')
            game_on = False
        elif player_choice == 'paper' and cpu_choice == 'paper':
            print('It is a tie')
            game_on = False
        elif player_choice == 'paper' and cpu_choice == 'scissor':
            print('Player Loses')
            game_on = False
        elif player_choice == 'paper' and cpu_choice == 'rock':
            print('Player Wins')
            game_on = False
        elif player_choice == 'scissor' and cpu_choice == 'scissor':
            print('It is a tie') 
            game_on = False
        elif player_choice == 'scissor' and cpu_choice == 'rock':
            print('Player Loses')
            game_on = False
        elif player_choice == 'scissor' and cpu_choice == 'paper':
            print('Player Wins')
            game_on = False


    if not replay():
        break


start_game():

