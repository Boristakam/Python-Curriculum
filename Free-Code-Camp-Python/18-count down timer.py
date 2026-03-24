import time


# time.sleep(3) #module sleeps for 3 seconds
# print ("time is up!")


my_time = int(input("\nenter the sleep time in seconds: "))

for x in range(my_time, 0, -1):     #counts from my_time down to 0
    seconds = x % 60
    minutes = int(x / 60) % 60      #modulus 60 because we dont want to go over 60 seconds 
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("time is up!")
