import random

user_wins = 0
comp_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("try something valid")
        continue

    random_number = random.randint(0, 2) 
    #rock = 0, paper = 1, scissors = 2 
    comp_pick = options[random_number]
    print("Computer picked", comp_pick)

    if user_input == comp_pick:
        print("Draw...")
    elif user_input == "rock" and comp_pick == "scissors":
        print("You win!")
        user_wins += 1
    elif user_input == "paper" and comp_pick == "rock":
        print("You win!")
        user_wins += 1
    else:
        print("You lose........")
        comp_wins += 1




print("Your score is ", user_wins , " and Computer score is ", comp_wins)
print("Goodbye")