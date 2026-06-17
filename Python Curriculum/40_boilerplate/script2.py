from script1 import *  #impoting script1 allows us to access the functions within script1.py without having to rewrite them in this file.
print(__name__)        # prints script 2 then __main__ because script2 is being run directly and not imported into another file. if it was imported into another file then it would print the name of that file instead of __main__

#NOTE: even though script 1 is imported running this file does not execute the content of the main method within cript1 because of the if statement 

def fave_drink(drink):
    print(f"your fave food is {drink}!\ngoodbye! ")

def main():
    print("this is cript 2")
    fave_food("chocolate") #this function in script1 can be accessed because it is not in the restrictive if statement (it is not part of the main method)
    fave_drink("honey")

if __name__ == '__main__': #are we running this program/file directly? if so run its main() method 
    main() 