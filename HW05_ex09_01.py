#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports
txt=open("words.txt")                       #open the file and pass the file metadata to txt
txtfile=txt.read()                          #read the file and store the contents of that file in txtfile
listofwords=txtfile.split()                 #split the file into words
for m in listofwords:
    if len(m) > 20:                         #check for length of the word and if > 20 print it
        print(m)
# Body


##############################################################################
def main():
    pass  # Call your functions here.

if __name__ == '__main__':
    main()
