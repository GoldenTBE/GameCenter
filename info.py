import csv
import testing_input
from main import start, options, play
import rps
import BlackJack


#info will be stored in a user:pass:coins:score format
#csv should allow for scalibilty/ more users
#guide: 1A- logging in/create user
class user_functions:
    def __init__(self,username = " ",coins = 0, score = 0):
        self.username = username
        self.coins = coins
        self.score = score
    def leaderboard(self,user):
        print(f'In Works')
        options(user)
    def your_info(self,user):
        print(f'|Username: {self.username}|\n'
              f'|Coins: {self.coins}|\n'
              f'|Score: {self.score}|')
        options(user)

    def rps(self,user): #RPS
        string = input(f'|Welcome to Rock, Paper, Scissors!|\n'
              f'|B - Bet Mode|\n'
              f'|P - Practice Mode|\n'
              f'|* - Back to Game Options|\n')
        gametype = 0
        if string == 'B':
            rps.main(gametype,self.username,self.coins,self.score)
            user_functions.rps(self)
        elif string == 'P':
            gametype += 1
            rps.main(gametype,self.username,self.coins,self.score)
            user_functions.rps(self)
        elif string == '*':
            play(user)
        else:
            print(f'You did not select one of the options. Try Again.\n')
            user_functions.rps()
    def blackjack(self, user): #Blackjack
        string = input(f'|Welcome to BlackJack!|\n'
                       f'|B - Bet Mode|\n'
                       f'|P - Practice Mode|\n'
                       f'|R - Rules|\n'
                       f'|* - Back to Game Options|\n')
        gametype = 0
        if string == 'B':
            BlackJack.main(gametype, self.username, self.coins, self.score)
            user_functions.blackjack(self,user)
        elif string == 'P':
            gametype += 1
            BlackJack.main(gametype, self.username, self.coins, self.score)
            user_functions.blackjack(self,user)
        elif string == 'R':
            BlackJack.rules()
            user_functions.blackjack(self,user)
        elif string == '*':
            play(user)
        else:
            print(f'You did not select one of the options. Try Again.\n')
            user_functions.blackjack()



    def bet(self): #betting
        with open ('info.csv', 'r') as x:
            read = csv.reader (x)






'''------------------------------class separator---------------------------------------'''



'''1A----------------------------------------------------------------------------------------'''

def is_user_created(username,testcase):
    '''
    This function test if the username is in the csv file.
    :param username: inputted from the user
    :param testcase: testcase depends on the function that is called. Loging or account create.
    :return: returns the username seen in function create_user
    '''
    with open ('info.csv', 'r') as x:
        read = csv.reader(x)
        user_list = []
        for row in read:
            user_list.append(row[0])
        if testcase == 0:
            while username in user_list:
                username = input(f'Username is taken already. Please enter a different username or login to your account.\n')
        if testcase == 1:
            while username not in user_list:
                username = input(f'Username is not found in database. PLease try again.\n')
    return username

def create_user(): #add user to csv
    '''
    Creates user account
    :return:
    '''
    testcase = 0
    username = is_user_created(input(f'Please input a unique username for your account at GameCenter.\n'),testcase)
    password = input(f'Please enter a password to your account.\n')
    user_info = (username,password,'0','0')

    with open ('info.csv', 'a', newline='') as information:
        write_info = csv.writer(information)
        write_info.writerow(user_info)

    print(f'Congrats! You have succesfully registered your account! You can login now.')
    start()



def login_tester(username,password):
    '''
    This function test if the username is in the csv file.
    :param username: inputted from the user
    :return: returns the username seen in function create_user
    '''
    with open ('info.csv', 'r') as x:
        read = csv.reader(x)
        user_list = {}
        for row in read:
            user_list[row[0]] = row[1:]

        password_correct = False
        while password_correct == False:
            if password != user_list[username][0]:
                password = input(f'Your password is incorrect. Please type in your password again or create an account.\n')
            else:
                password_correct = True

        print(f'You have succesfully logged in!\n'
              f'Username: {username}\n'
              f'Coins: {user_list[username][1]}\n'
              f'Score: {user_list[username][2]}\n')

    return username,user_list[username]

def login_user(): #login to user
    '''
    Logging in to user's account.
    :return:
    '''
    testcase = 1 #testcase 1
    username = is_user_created(input(f'Please input your username. Case sensitive. Please do not include whitespaces.\n'),testcase)
    password = input(f'Please enter your password that goes with this account.\n')

    username, information = (login_tester(username,password)) # calls function login tester.

    player = user_functions(username,information[1],information[2])
    return player

'''1A-----------------------------------------------------------------------------------------'''

