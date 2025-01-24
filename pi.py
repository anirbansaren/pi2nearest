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

print("The inputted number is:\n{}".format(input_n()))

