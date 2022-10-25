#Lena Lanza
#INST126
#10/23/22
#Project 1: Rock, Paper, Scissors
import random

# ASCII art Sourced from github user wynand1004 
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# The following function takes in a move as a parameter. 
# It will return the corresponding string art based on the move. 
"""
e.g: 
    move = "rock"
    moveArt = printMove(move)
    print(moveArt)
    # will print the rock hand as shown below
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    
"""
def printMove(move):
        
        if move == 'rock':
                return rock
        if move == 'paper':
                return paper
        if move == 'scissors':
                return scissors


# The following function takes in the playerName as a parameter.
# The function will return the playerMove as a string 
"""
e.g: 
    playerName = "Alex"
    makePlayerMove(playerName)
    
    # the following would get printed
    
    Choose rock, paper, or scissors: 
    rock
    
    Alex chose: 
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        
"""
def makePlayerMove(playerName):

        #Takes in input from player
	playerMove = input("Choose rock, paper, or scissors: ").casefold()
	playerArt = printMove(playerMove)
	print(playerName, "chose:\n" + playerArt)

	return playerMove

# The following function takes in the computerName as a parameter. 
# The function will return the computerMove as a string
"""
e.g: 
    computerName = "Eric"
    makeComputerMove(computerName)
    
    # for this example, we will say the random number drawn was 1, so the following will get printed
    
    Eric chose: 
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        
"""
def makeComputerMove(computerName):
        computerMove = ''

        #Set random number range; values to correspond w/ rock/paper/scissors
        randomNumber = random.randrange(3)
        

        if randomNumber == 0:
                computerMove = 'rock'
        elif randomNumber == 1:
                computerMove = 'paper'
        elif randomNumber == 2:
                computerMove = 'scissors'
	
        computerArt = printMove(computerMove)
        print(computerName, "chose:\n" + computerArt)
	

        return computerMove

# The following function takes in the playerMove and computerMove as parameters and returns the winner as a string. 
def checkRoundWinner(playerMove, computerMove):

        #All possibile game outcomes shown using if-statements    

        if playerMove == computerMove:
                print("It was a tie!\n")
        
        elif playerMove == "rock":
                if computerMove == "scissors":
                        return "W"
                else:
                        return "L"
                        
        elif playerMove == "paper":
                if computerMove == "rock":
                        return "W"
                else:
                        return "L"
                        
        elif playerMove == "scissors":
                if computerMove == "paper":
                        return "W"
                else:
                        return "L"
                        

	# Return statement(s)


# The main function will be the main driver for your game of rock, paper, scissors. 
# We want the game to continue until either the player or the computer wins the best out of three. 
# *Hint: a while loop might be helpful :)* 
def main():
        playerName = input("What would you like the player's name to be?: ")
        computerName = input("What would you like the computer's name to be?: ")
	
        #Setting number of wins at 0 for both participants, before the game starts
        playerWins, computerWins = 0, 0

        #While loop: Unless the round wins for either participant is over 2, the game continues
        while playerWins < 2 and computerWins < 2:

                #Have the player & computer make their move
                p1 = makePlayerMove(playerName)
                p2 = makeComputerMove(computerName)

                #Checking to see if the player won or lost the round
                winDecider = checkRoundWinner(p1, p2)
                
               #Points added to the winner's scores using if-statements 
                if winDecider == "W":
                        playerWins+=1
                        print(playerName,"won this round!\n")
                elif winDecider == "L":
                        computerWins+=1
                        print(computerName, "won this round!\n")
        #Winner of the match is decided best 2 out of 3
        if playerWins == 2:
                print(playerName,"wins the match!")
        else:
                print(computerName,"wins the match!")
main()
