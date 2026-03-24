questions = ("how many elements are in the periodic table?: ", 
             "which animal lays the largest egg?: ",
             "What is the most abundant gas in earth?: ",
             "how many bones in the human body?: ")

options = (("A. 152", "B. 77", "C. 89", "D. 39"), 
           ("A. whale", "B. crocodile", "C. elephant", "D. lion"), 
           ("A. nitrogen", "B. oxygen", "C. co2", "D. hydrogen"), 
           ("A. 206", "B. 207", "C. 208", "D. 209"))

correct_answers = ("C", "D", "A", "A")

guesses = []

score = 0 

question_num = 0

for question in questions:
    print("---------")
    print(question)
    for option in options[question_num]: 
            print(option)
    
    guess = input("\nenter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == correct_answers[question_num]:
          score += 1
          print("CORRECT!\n")
    else:
          print("INCORRECT!")
          print(f"{correct_answers[question_num]} is the correct answer!\n")

    question_num += 1


print("---------")
print(" RESULTS ")
print("---------")

print("answers: ", end="")
for answer in correct_answers:
      print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
      print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"your score is: {score}%")