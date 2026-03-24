money = 0 
duration = 0
rate = 0 

while money <= 0:
    money = float(input("\nenter initial investment amount?: "))
    if money <= 0:
        print("your initial investment should be higher than 0") 
    
while rate <= 0:
    rate = float(input("whats the annual rate?: "))
    if rate <= 0:
        print("he rate should be higher than 0") 

while duration <= 0:
    duration = float(input("how long is the money saved for (enter number of years)?: "))
    if duration <= 0:
        print("duration should be higher than 0 year") 

total = money * pow(1 + (rate/duration), duration)
print(f"your total amount would be ${total: ,.2f} after {duration} year(s)!\n")