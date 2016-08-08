#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    try:
        number = int(input("Enter an integer to check: "))
        if int(number) == number:           #checking whether the number in integer
            if number%2 == 0:               #checking for even or odd
                print("The number you entered is even")
            else:
                print("The number you entered is odd")
    except:
        print("Come on! That was supposed to be an integer. Try Again")


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for n in range(0,9):
        for m in range(1,11):               #loop for lines
            if m == 10:                     #loop for text within lines
                print(n*10+m)               #go to new line after one iteration of first loop
            else:
                print(str(n*10+m)+"\t",end="")      #remain on same line during iteration of second loop


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    numbers=0
    sumnum=0
    numericinput=''
    while True:
        try:
            inp=(input("Enter a number: "))
            if inp == 'done':               #check for terminal condition
                break
            else:
                inp=float(inp)              #take float type of entered number
                sumnum=sumnum+inp           #increment sum by inp
                numbers=numbers+1           #increment number of inputs by 1
        except:
            print("That was supposed to be a numeric input. Try again")
    return sumnum/numbers                   #return the average


##############################################################################
def main():
    even_odd()
    ten_by_ten()
    print(find_average())

if __name__ == '__main__':
    main()
