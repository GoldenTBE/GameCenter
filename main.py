import info
from tabulate import tabulate
from testing_input import is_str,is_digit

def start():
   string = input((f'\nWhat would you like to do?\nL - Login to user\nC - Create a user\nQ - Quit out of app\n'))
   if string == 'L':
       player_info = info.login_user()
       return player_info
   elif string == 'C':
       info.create_user()
   elif string == 'Q':
       quit()
   else:
       print(f'You did not select one of the options. Try Again.\n')
       start()


def options(user_info):
    string = input(f'|-Main Menu-|\n'
                   f'|P - Play Games|\n'
                   f'|PL - Player Leaderboard|\n'
                   f'|L - Logout|\n'
                   f'|Q - Quit|\n')
    if string == 'P':
        play()
    elif string == 'PL':
        user_info.leaderboard(user_info)
    elif string == 'L':
        print(f'Bye {user_info.username}! See you again soon.')

    elif string == 'Q':
        quit()
    else:
        print(f'You did not select one of the options. Try Again.\n')
        options(user_info) #recursion

def play():
    string = input(f'|Games Offered|\n'
                       f'|RPS - Rock Paper Scissors|\n'
                       f'|BJ - BlackJack|\n'
                       f'|B - Battleship|\n'
                       f'|* - Back|\n')
    if string == 'RPS':
        user_info.rps()
    elif string == 'BJ':
        pass
    elif string == 'B':
        pass
    elif string == '*':
        options(user_info)
    else:
        print(f'You did not select one of the options. Try Again.\n')
        user_info.play(user_info)




def main():
    print(f'|------------------------------------------------------------------|\n'
          f'|Hello! Welcome to the Gamecenter! We offer multiple games to play.|\n'
          f'|Login to play! Playing games will change your score if you win or |\n'
          f'|lose. Place bets to increase your coin amount. More games to come!|\n'
          f'|------------------------------------------------------------------|')










if __name__ == '__main__':
    main()
    run = False
    while run == False:
        user_info = start()
        options(user_info)
