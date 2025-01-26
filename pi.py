from math import pi

def input_n():
# this function takes input from the user
    while True:
    # this while loop iterates till we get an integer input
        try:
            num = int(input("Please enter the value of n (the number of digits in pi after the decimal point) :"))
        except:
            print("Wrong input! Please enter an integer.")
            continue
        if type(num) == type(1):
            break
    # this returns the value of the integer input
    return num

def calculate_pi(n):
    # this function will calculate the value of pi to the nth digit
    pi_value = pi
    pi_n = round(pi_value, n)
    print("The value of pi to the {a}th digit after decimal points is:\n{b}".format(a=n, b=pi_n))

def welcome():
    # this function welcomes the user and starts the program
    print("         WELCOME TO THIS pi2nearest APP!!!       ")
    print("         Brought to you by Anirban Saren         ")
    print("\n\n\n")
    print("Instructions:")
    print("1. We will ask you to enter the value of n (the number of digits in pi after the decimal point)")
    print("2. Then we will print out the value of pi till that number of digits after decimal.")
    print("\n\n\n")
    print("         LET'S GOOOOOO!!!!!!!!                   ")
    
    value_of_n = input_n()
    calculate_pi(value_of_n)

if __name__=="__main__":
    welcome()
