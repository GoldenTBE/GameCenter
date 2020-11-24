import rps
import info
import rps
from tabulate import tabulate
from testing_input import is_str,is_digit
def start():
   string = input((f'\nWhat would you like to do?\nL - Login to user\nC - Create a user\nQ - Quit out of app\n'))
   while string != 'Q':
       if string == 'L':
           player_info = info.login_user()
           return player_info
           break
       elif string == 'C':
           info.create_user()
           break
       elif string == 'Q':
           quit()
       else:
           string = input(f'You did not select one of the options. Try Again.\n')

    #will pass class after login/create
#def options():





def main():
    print(f'|------------------------------------------------------------------|\n'
          f'|Hello! Welcome to the Gamecenter! We offer multiple games to play.|\n'
          f'|Login to play! Playing games will change your score if you win or |\n'
          f'|lose. Place bets to increase your coin amount. More games to come!|\n'
          f'|------------------------------------------------------------------|')
    users_info = start()
    print(users_info.username)








if __name__ == '__main__':

    main()
