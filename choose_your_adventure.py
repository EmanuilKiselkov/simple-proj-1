name = input("Type your name: ")
print("Welcome", name ,"to this adventure!") 

answer = input("You are driving on the highway. Suddenly you feel a wobble on your steering wheel. Do you want to slow down? ").lower()

if answer == "yes":
    answer = input("Ok you stopped, but the engine is now on fire. Do you want to open the trunk? ")
    if answer == "yes":
        answer = input("You have lots of stuff. Do you want to search for fire extinguisher? ") 
        if answer == "yes":
            print("Good job, you saved the car and yourself ")
        elif answer == "no":
             print("sorry mate ")

    elif answer == "no":
        print("Car burned down, you died ")





elif answer == "no":
    print("What did you think was gonna happen? Your wheel flew and you died")




else:
    print("Game over, try again!")