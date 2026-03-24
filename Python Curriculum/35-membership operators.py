#membership operators = used o test whether a value or variable is found in sequence (string, list, set, tuple, or dictionary)
#                       1. in 
#                       2. not in

word = "APPLE"
students = {"spongebob", "patrick", "Tom"}
grades = {"spongebob": "A", "patrick": "B"}
email = "boris@gmail.com"


letter = input("guess a letter in the secret word: ")
if letter in word:
    print(f"there is {letter} in the secret word")
elif letter not in word:       #note this is just for example purposes, this could and should be just an else 
    print(f"there is no {letter} in the secret word")
else:
    pass

student = input("enter the name of a student: ")
if student not in students:
    print(f"there is no {student} in the classroom")
else:       #note this is just for example purposes, this could and should be just an else 
    print(f"there is {student} in the classroom")
    if student not in grades.keys():
        print(f"{student} does not have a grade yet")
    else:
        print(f"{student}'s grande is {grades[student]}") #student is the key to a value in the dictionary 



if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")


