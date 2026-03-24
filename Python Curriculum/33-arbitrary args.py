# *args = allows you to pass multiple non-key args
# **kwargs = allows you to pass multiple keyword-args
#            * is the unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

def add(*args): # we can pass any amount of aguments. the name args can be changed (doesnt matter at all it's just the typical param name)
    print(type(args)) #should say that it is a tupple (a tuple of arguments can be passed)
    total = 0
    for arg in args:
        total += arg
    return total 

print(add(1, 2, 3)) #6    note we cab oa


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr", "Boris", "Takam")


def print_addr(**kwargs): # can pass any amount of keyword aguments 
    print(type(kwargs)) #it is a dictionary
    for value, key in kwargs.items():
        print(f"{value}: {key}")
    print()
    
print_addr(street= "Redgate Roard", city= "Cambridge", post_code= "CB3")


def shipping_label(*args, **kwargs):  #combining args and kwargs (*args param comes first else it throws a syntax err)
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value)
    print(f"{kwargs.get('street')}")                          #just decoration the commented out lines above also work 
    print(f"{kwargs.get('city')} {kwargs.get('post_code')}")

shipping_label("Dr", "Boris", "Takam", 
               street= "Redgate Roard", city= "Cambridge", post_code= "CB3") 


