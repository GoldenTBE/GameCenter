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
        for row in read:
            while row[0] == username:
                username = input(f'Username is taken already. Please enter a different username or login to your account.\n')

    return username

def create_user(): #add user to csv
    '''
    Creates user account
    :return:
    '''
    username = is_user_created(input(f'Please input a unique username for your account at GameCenter.\n'))
    password = input(f'Please enter your password to your account.\n')
    user_info = (username,password,'0','0')

    with open ('info.csv', 'a', newline='') as information:
        write_info = csv.writer(information)
        write_info.writerow(user_info)

    print(f'Congrats! You have succesfully registered your account! You can login now.')


def login_user(): #login to user
        with open ('info.csv', 'a') as x:
            read = csv.reader (x)
