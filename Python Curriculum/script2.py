from script1 import *
print(__name__)

#NOTE: even though script 1 is imported running this file does not execute the content of the main method within cript1 because of the if statement 

def fave_drink(drink):
    print(f"your fave food is {drink}!\ngoodbye! ")

def main():
    print("this is cript 2")
    fave_food("chocolate") #this function in script1 can be accessed because it is not in the restrictive if statement 
    fave_drink("honey")

if __name__ == '__main__': #are we running this program/file directly? if so run the main() method
    main() 