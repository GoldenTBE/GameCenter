import csv
import testing_input
from main import start

#info will be stored in a user:pass:coins:score format
#csv should allow for scalibilty/ more users
class user: #in works after login/create user
    def __init__(self,username = " ",password = " ",coins = 0, score = 0):
        self.username = username
        self.password = password
        self.coins = coins
        self.score = score
    def bet(self): #betting
        with open ('info.csv', 'r') as x:
            read = csv.reader (x)






'''------------------------------class separator---------------------------------------'''





def is_user_created(username):
    '''
    This function test if the username is in the csv file.
    :param username: inputted from the user
    :return: returns the username seen in function create_user
    '''
    with open ('info.csv', 'r') as x:
        read = csv.reader(x)
        user_list = []
        for row in read:
            user_list.append(row[0])
        while username in user_list:
            username = input(f'Username is taken already. Please enter a different username or login to your account.\n')

    return username

def create_user(): #add user to csv
    '''
    Creates user account
    :return:
    '''
    test_var = 0
    username = is_user_created(input(f'Please input a unique username for your account at GameCenter.\n'))
    password = input(f'Please enter your password to your account.\n')
    user_info = (username,password,'0','0')

    with open ('info.csv', 'a', newline='') as information:
        write_info = csv.writer(information)
        write_info.writerow(user_info)

    print(f'Congrats! You have succesfully registered your account! You can login now.')
    start()



def login_tester(username,pasword):
    '''
    This function test if the username is in the csv file.
    :param username: inputted from the user
    :return: returns the username seen in function create_user
    '''
    with open ('info.csv', 'r') as x:
        read = csv.reader(x)
        user_list = []
        for row in read:
            user_list.append(row[0])

        while username not in user_list:
                username = input(f'I couldn\'t find your username in our database. Please try again.\n')
    return username

def login_user(): #login to user
    '''
    Logging in to user's account.
    :return:
    '''
    test_var = 1
    login_tester(input(f'Please input your username. Case sensitive. Please do not include whitespaces.\n'))
    password = input(f'Please enter your password that goes with this account.\n')

    with open ('info.csv', 'r') as x:
       read = csv.reader (x)

