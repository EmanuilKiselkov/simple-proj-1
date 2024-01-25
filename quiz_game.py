print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay let's play!")
score = 0

answer = input("What is the capital of Bulgaria? ")
if answer.lower() == "sofia":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -=1

answer = input("What is the name of the highest mountain in Bulgaria? ")
if answer.lower() == "rila":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -=1
    
answer = input("What is the name of the longest mountain in Bulgaria? ")
if answer.lower() == "stara planina":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -=1

answer = input("What's the name of the longest river in Bulgaria? ")
if answer.lower() == "danube":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -=1

answer = input("What's the name of the largest lake in Bulgaria? ")
if answer.lower() == "burgas":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -=1

print("You got " + str(score) + " score aquired!")
