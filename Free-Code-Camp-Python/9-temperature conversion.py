unit = input("is this celcius or kelvin (type C or K)")
temp = float(input("what is the temperature? "))

if unit == "C":
    temp = round((9 * temp)/ 5 + 32, 1)
    print(f" the temperature is {temp} F")
if unit =="K":
    temp = round(( temp - 32) * 5 / 9, 1)
    print(f" the temperature is {temp} C")
else:
    print("you entered an invalid unit ")