
import random

# POSITIONS ON BOARD CORRESPONDING TO VARIABLE NAME
#   ONE|TWO|THREE
#	FOUR|FIVE|SIX
#	SEVEN|EIGHT|NINE


#main game control
def tictactoe():
	gameBoard= gameBoardInit()
	parser(gameBoard)
	print("Game Ended.")

# Function to receive the game progress and display on board
#Expects a 9-element dictionary of all the characters on the board
def printboard (pattern):
	print("________________\n")
	printrow([pattern['ONE'],pattern['TWO'],pattern['THREE']])
	printrow([pattern['FOUR'], pattern['FIVE'], pattern['SIX']])
	printrow([pattern['SEVEN'], pattern['EIGHT'], pattern['NINE']])


#Expects a list of 3 characters in a list
def printrow (linein):
	print(f" {linein[0]} | {linein[1]} | {linein[2]} \n-----------")

#Function to take user input
def parser(gameBoard):
	quitting = False
	exitKey = None

	while not quitting:
		gameOver = False
		xPlayer = True
		currentplayer = miniGameOrder()
		while not gameOver:
			newPosition = playerPrompt(currentplayer, gameBoard)
			gameBoard[newPosition] = currentplayer
			printboard(gameBoard)
			winner = checkWinner(gameBoard)

			if winner != " ":
				exitKey = input(f"Winner! Congratulations, {winner}!\nDo you want to quit? (Y/N)")

				if exitKey == "Y" or exitKey == 'y':
					quitting = True
					gameOver = True
					break
				else:
					gameBoard = gameBoardInit()

			currentplayer = changePlayer(currentplayer)

#get next player
def changePlayer(lastPlayer):
	if lastPlayer == "X":
		return "O"
	else:
		return "X"

#Function to update gameBoard
def updateGameBoard(userChar, position, gameBoard):
	gameBoard[position] = userChar

#reset/initialize ):
def gameBoardInit():
	return {'ONE':" ",'TWO':" ",'THREE':" ",'FOUR':" ",'FIVE':" ",'SIX':" ",'SEVEN':" ",'EIGHT':" ",'NINE':" "}

# tells player to make a move
def playerPrompt(whatPlayer, gameBoard):
	newpos = None
	validMove = False

	while not validMove:
		if whatPlayer == "X":
			newpos = input("Player X, make your move.\n")
		else:
			newpos =input("Player O, make your move.\n")

		if gameBoard[newpos] == " ":
			break
		else:
			print("Invalid move. Someone is already there. Please pick a free position.")

	return newpos

# check if someone has won
def checkWinner(gameBoard):

	if gameBoard['ONE'] == gameBoard['TWO'] and gameBoard['THREE'] == gameBoard['TWO']:
		return(gameBoard['THREE'])
	elif gameBoard['FOUR'] == gameBoard['FIVE'] and gameBoard['FIVE'] == gameBoard['SIX']:
		return(gameBoard['SIX'])
	elif gameBoard['SEVEN'] == gameBoard['EIGHT'] and gameBoard['EIGHT'] == gameBoard['NINE']:
		return gameBoard['NINE']

	elif gameBoard['ONE'] == gameBoard['FOUR'] and gameBoard['SEVEN'] == gameBoard['FOUR']:
		return gameBoard['ONE']
	elif gameBoard['TWO'] == gameBoard['FIVE'] and gameBoard['EIGHT'] == gameBoard['FIVE']:
		return gameBoard['EIGHT']
	elif gameBoard['THREE'] == gameBoard['SIX'] and gameBoard['NINE'] == gameBoard['SIX']:
		return gameBoard['NINE']

	elif gameBoard['ONE'] == gameBoard['FIVE'] and gameBoard['NINE'] == gameBoard['FIVE']:
		return gameBoard['NINE']
	elif gameBoard['THREE'] == gameBoard['FIVE'] and gameBoard['FIVE'] == gameBoard['SEVEN']:
		return gameBoard['SEVEN']
	else:
		return " "

#decide on who goes first, returns a char for the player that goes first.
def miniGameOrder():
	xGuess = input("To decide who goes first, I have randomly drawn a number from 1-10. \nBoth players will randomly choose a number from 1-10 and the closet guess wins. \nX player goes first. Please enter your guess:\n")

	miniGameDone = False

	while not miniGameDone:
		oGuess = input("O player make your guess:\n")
		xGuess = ord(xGuess) - ord('1') + 1
		oGuess = ord(oGuess) - ord('1') + 1

		while oGuess == xGuess:
			oGuess = input("O player please pick a different number.")
			oGuess = ord(oGuess) - ord('1') + 1

		pick = random.randrange(1,10)
		print(f"Player X has picked {xGuess} and Player O has picked {oGuess}.\nThe number was {pick}.\n")
		xGuess = abs(pick-xGuess)
		oGuess = abs(pick - oGuess)

		if xGuess < oGuess:
			print("X goes first.\n")
			return "X"
		elif oGuess < xGuess:
			print("O goes first.\n")
			return "O"
		else:
			xGuess= input("Tie. Player X please go again:\n")


tictactoe()
