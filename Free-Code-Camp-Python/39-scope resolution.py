#variable scope = where a variable is visible and accessible
#scope resolution order = LEGB (local -> encloded -> global -> built-in). that is the order of search by the compiler 

from math import e   # e is a global var

h = 6           #global var      
def func1():
    a = 1       #local 
    print(a)
    #print(b)   #b is not visible to func1

def func2():
    x = 2
    b = 1
    print(b)
    def func3(): #funtion in function (will learn in later lessons)
        e = 4    # this e unlike the first is a local var
        print(x) #x is not in the local scope but in the enclosed scope
        print(h)
        print(e) #if there are no local e var then then enclosed loop is searched and so on until a var id found or not 
 
func1()
func2()
#func3()         #see lessson for function within function