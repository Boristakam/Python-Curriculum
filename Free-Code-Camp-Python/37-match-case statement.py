#match-case statement (switch) = an alternatice to using many elif statements 
#                                executes some code if the value matches a 'case' (similar to switch statements in C and C++)
#                                it is cleaner and syntax is more readable


#case values are passed via function arguments 

def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day" #the underscore (_) acts as a wildcard, matching any value not previously matched
        
print(day_of_week(1))  # Output: Monday
print(day_of_week(5))  # Output: Friday 
print(day_of_week("pixxa"))  # Output: Invalid day 

def is_weekent(day):
    match day:
        case 6 | 7:  # Matches either 6 or 7 (Saturday or Sunday)
            return True
        case _:
            return False
        
print(is_weekent(6))  # Output: True