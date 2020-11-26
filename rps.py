from random import *
import info
import main
from testing_input import is_digit

def gameamount():
    game_amount = is_digit(input(f'How many rounds of Rock, Paper, Scissors shall we play?\n'))
    return game_amount

def gamemode(gametype):
    if gametype == 0:
        bet_amount = is_digit(input(f'|Welcome to the betting game mode of Rock, Paper, Scissors. You have ?|\n'))
        #This section will be worked on when betting is implemented in user_functions class
    else:
        print(f'|Welcome to Practice Mode of Rock, Paper, Scissors.|')
        amount = gameamount()
        print(f'You are playing {amount} game\'s of Rock, Paper, Scissors. Good Luck!\n')
        rps_game(amount)


def rps_game (x): #x = gameamount
    y = 0
    score_cpu = 0
    score_user = 0

    rps_response = ["Rock", "Paper", "Scissors"]
    cpu = rps_response[randint(0, 2)]
    while y <= x:
        player = input(f'What would you like to pick? (Choices are Rock, Paper, & Scissors.\n')

        if player == cpu:
            print(f'Tie! No one gets a point. The score is {score_user} (you) {score_cpu} (Cpu)')
            y += 1
        elif player == "Rock":
            if cpu == "Paper":
                score_cpu += 1
                y += 1
                print(f'Paper covers rock. You lost this round. The score is {score_user} (you) {score_cpu} (Cpu)')
            else:
                score_user += 1
                y += 1
                print(f'Rock smashes Scissors. You won this round. The score is {score_user} (you) {score_cpu} (Cpu)')
        elif player == "Scissors":
            if cpu == "Rock":
                score_cpu += 1
                y += 1
                print(f'Rock smashes Scissors. You lost this round. The score is {score_user} (you) {score_cpu} (Cpu)')
            else:
                score_user += 1
                y += 1
                print(f'Scissors cut Paper.You won this round.The score is {score_user} (you) {score_cpu} (Cpu)')
        elif player == "Paper":
            if cpu == "Scissors":
                y += 1
                score_cpu += 1
                print(f'Scissors cut Rock. You lost this round. The score is {score_user} (you) {score_cpu} (Cpu)')
            else:
                score_user += 1
                y += 1
                print(f'Scissors cut Paper. You won this round. The score is {score_user} (you) {score_cpu} (Cpu)')
        else:
            print("Not a valid response, please use Rock, Paper, or Scissors.")
        cpu = rps_response[randint(0, 2)]

    if score_user == score_cpu:
        print(f'Game has ended. It is a tie. You have {score_user} points and the computer has {score_cpu}.')
    elif score_user > score_cpu:
        print(f'Game has ended. You have won! You have {score_user} points and the computer has {score_cpu}.')
    else:
        print(f'Game has ended. You have lost :(. You have {score_user} points and the computer has {score_cpu}.')




def main(gametype,username,coins,score):
    gamemode(gametype)
    print(username,coins,score)
    pass




if __name__ == '__main__':
    main()












