# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:36:30 2019
@author: ARVIND KRISHNA
"""
import random
import sys
"""A program which will simulate rolling of a die and moves of a pawn in snake and ladders.
Max number of players allowed is 4 and with a min of 2.
Enjoy the game.
A simple Command-line snake-and-ladder game"""


def Move(Player, value):
    """THIS FUNCTION MOVES THE PAWN AND ALSO CHECKS FOR 
    WINNING AND OVERFLOW"""
    snake_squares = {16: 4, 22:10, 33: 20, 48: 24, 62: 56, 78: 69, 74: 60, 91: 42, 97: 6}
    ladder_squares = {3: 12, 7: 23, 11:25, 21: 56, 47: 53, 60: 72, 80: 96}
    Throw = random.randint(1, 6)
    num = value + Throw
    if num>100:
        print("BAD LUCK, YOU CANT MOVE, YOU NEED A {} TO WIN".format(100 - value))
        return value
    if num == 100:
        return num
    #IF NONE OF THE OTHER CONDITIONS ARE MATCHED,
    print(Player, "Rolled a", Throw, "And is now on", num)
    if num in snake_squares:
        #if landed in a snake square
        print(Player, " got bitten by a snake and is now on square", snake_squares[num])
        num = snake_squares[num]
    elif num in ladder_squares:
        #if landed in a ladder square
        print(Player, " climbed a ladder and is now on square", ladder_squares[num])
        num = ladder_squares[num]

    return num

def playerscount():
    """ACCEPTS THE NUM OF PLAYERS"""
    numofplayers = int(input("How many players are in the game?"))
    print()
    if numofplayers > 4 or numofplayers < 2:
        print("Must be less than 5 and greater than 1")
    else:
        return numofplayers


def nameofplayers(N):
    """ACCEPTS THE NAME OF PLAYERS AND REUTUNS THE LIST OF NAMES"""
    Names = ['','','','']
    for i in range(N):
        Names[i] = input("What is the name of Player "+str(i+1)+" ?")
    return Names

def turn(player,pos):
    COMMANDSTATE = "Press Enter to continue or press 'stop' to stop"
    WINSTATEMENT = "WINS THE GAME! CONGRATULATIONS"
    COMMANDSTATE1 = str("Hey "+player+"! It's your turn now "+COMMANDSTATE)
    Command = input(COMMANDSTATE1)
    if Command.lower() == 'stop':
        #if the user commands to stop, the game must stop,
        #so the GameOver flag will become true
        return True, pos
    pos = Move(player, pos)
    if pos == 100:
        print(player, WINSTATEMENT)
        print("AT WINNING {} was at {}".format(player, pos))                 
        #if a player wins, the game is over
        #so the GameOver flag will become true
        return True, pos
        
    #if the function has not returned anywhere above
    #it means that the game is still on
    return False, pos
def main():
    """THE MAIN FUNCTION"""
    numofplayers = playerscount()
    playernames = nameofplayers(numofplayers)
    print(playernames[0], playernames[1], playernames[2], playernames[3], "- Welcome To Snakes And Ladders")
    COMMANDSTATE = "Press Enter to continue or press 'stop' to stop: "
    WINSTATEMENT = "WINS THE GAME! CONGRATULATIONS"
    Command = ''
    TURNS = 0
    PosArr=[1,1,1,1]
    #A list containing the present positions of the pawns
    GameOver = False
    #Flag to check whether the game should be continued or not
    while not GameOver:      
        while TURNS < numofplayers:
            #This loops takes care of each person's moves.
            #if TURNS == 1, it means that its person1's turn
            TURNS += 1
            GameOver, PosArr[TURNS - 1] = turn(playernames[TURNS - 1], PosArr[TURNS - 1])
            if GameOver:
                #if gameover, exit the function
                return
        TURNS = 0
    return
if __name__=='__main__':
    main()
    
