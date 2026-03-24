#[start : end : step]

creditcard_num = "1234-654-6857"    #NOTE the "-" are also characters
print(creditcard_num[0])
print(creditcard_num[0:4])  #prints the first 4 characters starting from 1st element
print(creditcard_num[:4])   #prints the first 4 characters starting from 1st element
print(creditcard_num[5:])   #prints everything from the 6th char (index 5)
print(creditcard_num[-1])   #prints last char. NEGATIVE INDEX
print(creditcard_num[-2])   #prints second to last char
print(creditcard_num[-4:])  #prints last 4 chars
print(creditcard_num[::2])  #prints every second character withing the string 
print(creditcard_num[0::2]) #same as above
print(creditcard_num[::-2]) #prints every second character withing the string starting from the last char 
print(creditcard_num[::-1]) #reverts the string