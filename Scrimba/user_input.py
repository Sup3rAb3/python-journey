name = input("What is your name?: ")
age = input("What is your age?: ")
print("Hi " + name + "!")
print("You told the computer that you are " + age + " years old. Correct?")
user_answer = input("Type 'yes' or 'no': ")
if user_answer == "yes":
    print("Great! Thanks for confirming.")
else:    print("Oh no! Please try again and provide the correct information.")