#keyword arguments = arg preceeded by an identifier, helps with readability. order of arguments dont matter
#positional args come before keyword args, and non intialised args coome before default args

def hello(greeting, title, first_name, last_name):
    print(f"{greeting.capitalize()} {title.capitalize()}. {first_name.capitalize()} {last_name.capitalize()}")

def get_phone(country_code, area_code, first, last):
    return f"{country_code}-{area_code}-{first}-{last}" #retuns this data to the caller


hello("hello", "mr", "boris", "takam") #postional arguments (like in the previous lesson), order of args matter and matches directly to parameter order
hello("hello", first_name="boris", last_name="takam" , title="mr") #with keyword args the order of arguments no longer matters but like with default args if one arg has a keyword the following should also have them 


for x in range(1, 11): 
    print(x, end=" ") #end is a keyword argument
print()

print("1", "2", "3", "4", sep="-") #separate keyword argument


phone_num = get_phone(first=234, last=5678, country_code="+44", area_code=11)
print(phone_num)

