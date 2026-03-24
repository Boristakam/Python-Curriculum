#print(dir()) #prints all the double underscore attributes
#print(__name__)
#if __name__ == '__main__':
    #main() # to start our program 



#from script2 import *  #'*' means everything 
#print(__name__) #prints script 2 then __main__



def fave_food(food):
    print(f"your fave food is {food}!\ngoodbye! ")

def main():
    print("this is cript 1")
    fave_food("pizza")

if __name__ == '__main__': #are we running this program/file directly? if so run the main() method
    main() # to start our program 