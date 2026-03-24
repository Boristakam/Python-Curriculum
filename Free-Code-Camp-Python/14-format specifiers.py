#{value : flags} format value based on what flags are inserted 

# .(number)f = round to that many decimal places (fixed point) NOTE:dont add the bracket
# :(number) = allocate that many spaces  NOTE:dont add the bracket
# :03 = allocate and zero pad that many spaces
# :> = right justified
# :< = left justified
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := =  place a sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3500.1473
price2 = -987.253
price3 = 1212.542

print(f"price 1 is ${price1:09}")  #0 pads (to make total number of digits = 9)
print(f"price 1 is ${price1:015}")  #0 pads (to make total number of digits = 15)
print(f"price 2 is ${price2:.2f}") #2 decimal places
print(f"price 3 is ${price3:9}\n")   #9 spaces before writing the value

print(f"price 1 is ${price1:>10}")
print(f"price 2 is ${price2:<10}") 
print(f"price 3 is ${price3:^}\n")  

print(f"price 1 is ${price1:+}")
print(f"price 2 is ${price2:+}") 
print(f"price 3 is ${price3:+}\n")

print(f"price 1 is ${price1:,}")
print(f"price 2 is ${price2:=}") 
print(f"price 3 is ${price3:,}\n")  #coma separator

print(f"price 1 is ${price1:+,.2f}")
print(f"price 2 is ${price2: ,.2f}") 
print(f"price 3 is ${price3:+,.2f}\n")  