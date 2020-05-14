# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:36:30 2019

@author: ARVIND KRISHNA
"""
import random
"""A program which will simulate rolling of a die and moves of a pawn in snake and ladders.
Max number of players allowed is 4 and with a min of 2.
Enjoy the game.
A simple Command-line snake-and-ladder game"""

#this is the old and not so cool version,
#please go to the other file if you want a better version
def Move(Player, value):
    snake_squares = {16: 4, 22:10, 33: 20, 48: 24, 62: 56, 78: 69, 74: 60, 91: 42, 97: 6}
    ladder_squares = {3: 12, 7: 23, 11:25, 21: 56, 47: 53, 60: 72, 80: 96}
    Throw = random.randint(1, 6)
    num = value + Throw
    print(Player, "Rolled a", Throw, "And is now on", num)
    if num in snake_squares:
        print(Player, " got bitten by a snake and is now on square", snake_squares[num])
        num = snake_squares[num]
    elif num in ladder_squares:
        print(Player, " climbed a ladder and is now on square", ladder_squares[num])
        num = ladder_squares[num]

    return num

def playerscount():
    numofplayers = int(input("How many players are in the game?"))
    print()
    if numofplayers > 4 or numofplayers < 2:
        print("Must be less than 5 and greater than 1")
    else:
        return numofplayers


def nameofplayers(N):
    Names = []
    for i in range(1, N+1):
        Names.append(input("What is the name of Player "+str(i)+" ?"))
    return Names


numofplayers = playerscount()
playernames = nameofplayers(numofplayers)
#print(' Welcome To Snakes And Ladders',playernames)

name1 = ''
name2 = ''
name3 = ''
name4 = ''
for i in playernames:
    if name1 == '':
        name1 = i

    elif name2 == '':
        name2 = i
        if numofplayers == 2:
            name3, name4 = "", ""
            break
    elif name3 == '':
        name3 = i
        if numofplayers == 3:
            name4 = ""
            break
    elif name4 == '':
        name4 = i
    else:
        break
print(name1, name2, name3, name4, ", Welcome To Snakes And Ladders")
COMMANDSTATE = "Press Enter to continue or press 'stop' to stop"
WINSTATEMENT = "WINS THE GAME! CONGRATULATIONS"
COMMND = input(COMMANDSTATE)
Num1 = 0
Num2 = 0
Num3 = 0
Num4 = 0
TURNS = 0
while Num1 < 100 and Num2 < 100 and Num3 < 100 and Num4 < 100:       
    if COMMND != 'stop':
        while TURNS < numofplayers:
            TURNS = TURNS+1
            if TURNS == 1:
                Num1 = Move(name1, Num1)
                if Num1 >= 100:
                    print(name1, WINSTATEMENT)                    
                    break
                COMMANDSTATE1 = str("Hey "+name1+"! It's your turn now "+COMMANDSTATE)
                COMMND = input(COMMANDSTATE1)
            
            elif TURNS == 2:
                Num2 = Move(name2, Num2)
                if Num2 >= 100:
                    print(name2, ' ', WINSTATEMENT)
                    break
                COMMANDSTATE1 = str("Hey "+name1+"! It's your turn now "+COMMANDSTATE)
                COMMND = input(COMMANDSTATE1)
            
            elif TURNS == 3:
                Num3 = Move(name3, Num3)
                if Num3 >= 100:
                    print(name3, WINSTATEMENT)
                    break
                COMMANDSTATE1 = str("Hey "+name1+"! It's your turn now "+COMMANDSTATE)
                COMMND = input(COMMANDSTATE1)
            
            elif TURNS == 4:
                Num4 = Move(name4, Num4)
                if Num4 >= 100:
                    print(name4, WINSTATEMENT)
                    break
                COMMANDSTATE1 = str("Hey "+name4+"! It's your turn now "+COMMANDSTATE)
                COMMND = input(COMMANDSTATE1)
        TURNS = 0
    else:
        break

print("thanks")
