import time

#default arguments = default value for certain paremters. default is used when that argument is omitted, makes the function more flexible and faster (less args)

def net_price (list_price, discount = 0, tax = 5): #if a parameter has a default values the parameters that follow it also need to have default values because calling the function without overwriting that first default val would be impossible
    return list_price * (1-discount) * (1+tax)

def count(start, end = 5): #if you want a default value for start you would need a default for end too (in the order they are), or swap their positions (end, start=0)
    for x in range (start, end):
        print(x)
        time.sleep(1)
    print("done!")


print (net_price(500)) #3000
print (net_price(500, 0.1)) #overwriting the default val for discount with arg 0.1

count(0)


