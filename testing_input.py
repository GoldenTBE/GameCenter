import csv
def is_digit():
    while True:
        var = input()
        try:
            var = int(var)
            break
        except ValueError:
            print("Was that an integer? Please try again...")
    return var

def is_str(): #testing for wanted input in main.py
    while True:
        var = input()
        try:
            var.isalpha()
            break
        except ValueError:
            print("Was that a String? Please try again...")
    return var
#def is_user_in_csv():
