import csv
def is_digit(num):
    while True:
        try:
            num = int(num)
            break
        except ValueError:
            print("Was that an integer? Please try again...")
    return num

