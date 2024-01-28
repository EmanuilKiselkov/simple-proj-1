import random 

top_of_range = input("Type a number: ") #input for starting number

if top_of_range.isdigit(): #check if number is digit
    top_of_range = int(top_of_range) #make it int

    if top_of_range <= 0: #check if number is positive
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range) #range for the random number between 0 and input number

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("Congratz!!! You got it!!!")
        break
    else:
        print("Please try again")

