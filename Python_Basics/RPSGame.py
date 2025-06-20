import random

def getChoice():
    
    choices = ["rock","paper","scissors"]
    computer_choice = random.choice(choices)

    return computer_choice

def calculateWin(choices):
    pc,cc = choices["pc"],choices["cc"]
    if (pc==cc):
        return "It's a tie"
    elif(pc=="rock"):
        if(cc=="paper"):
            return "Computer Wins Player loses !!!!!"
        elif(cc=="scissors"):
            return "Player Wins Computer Loses 😁😁"
    elif(pc=="paper"):
        if(cc=="scissors"):
            return "Computer Wins Player loses !!!!!"
        elif(cc=="rock"):
            return "Player Wins Computer Loses 😁😁"
    elif(pc=="scissors"):
        if(cc=="rock"):
            return "Computer Wins Player loses !!!!!"
        elif(cc=="paper"):
            return "Player Wins Computer Loses 😁😁"

    return "Error in code"

choices = {"pc":input("Enter player choice: "),"cc":getChoice()}
print("Computer's choice: " + choices["cc"] + "\nPlayer's choice: " + choices["pc"])
print(calculateWin(choices))


