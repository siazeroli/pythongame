# Game: Ttic-Tac-Toe
#initialize the game board
board = []

for i in range(3):
	board.append(['*']*3)

#print the board
def showBoard(board):
	for i in board:
		print('|'.join(i))

#change the turn
turn = True
end = False
tie = False
winner = 'none'

player1 = 'X'
player2 = 'O'
currentPlayer = 'none'

def changeTurn(t,p1,p2):
	if t == False:
		return p1,True
	elif t == True:
		return p2,False

#fill the player decision to the board
row = 0
col = 0

def fillBoard(board,row,col,currentPlayer):
	i = False
	while i == False:
		if board[row][col] != '*':
			print('\nHere is already filled.\nPlease enter again')
			row = int(input('\nPlease enter the row\n'))
			col = int(input('Please enter the col\n'))
			row -= 1
			col -= 1
		else:
			board[row][col] = currentPlayer
			i = True

#determine if it is ended by win or tie
def deterEnd(board,currentPlayer):
	if board[0][0] == currentPlayer and board[1][0] == currentPlayer and board[2][0] == currentPlayer:
		return True,currentPlayer
	elif board[0][0] == currentPlayer and board[0][1] == currentPlayer and board[0][2] == currentPlayer:
		return True,currentPlayer
	elif board[0][0] == currentPlayer and board[1][1] == currentPlayer and board[2][2] == currentPlayer:
		return True,currentPlayer
	elif board[0][1] == currentPlayer and board[1][1] == currentPlayer and board[2][1] == currentPlayer:
		return True,currentPlayer
	elif board[0][2] == currentPlayer and board[1][2] == currentPlayer and board[2][2] == currentPlayer:
		return True,currentPlayer
	elif board[0][2] == currentPlayer and board[1][1] == currentPlayer and board[2][1] == currentPlayer:
		return True,currentPlayer
	elif board[1][0] == currentPlayer and board[1][1] == currentPlayer and board[1][2] == currentPlayer:
		return True,currentPlayer
	elif board[2][0] == currentPlayer and board[2][1] == currentPlayer and board[2][2] == currentPlayer:
		return True,currentPlayer
	else:
		k = True
		for i in range(3):
			for j in range(3):
				if board[i][j] == '*':
					k = False
		if k == True:
			return True,'tie'
		else:
			return False,currentPlayer

#game main
print("Player1 is 'X', player2 is 'O'")
first = input('Enter the first player(1 or 2)\n')
if first == '1':
	currentPlayer = player1
	turn = True
elif first == '2':
	currentPlayer = player2
	turn = False

while end == False:
	print('\nCurrentPlayer is %s' % currentPlayer)
	showBoard(board)
	row = int(input('Please enter the row\n'))
	col = int(input('Please enter the col\n'))
	fillBoard(board,row-1,col-1,currentPlayer)
	end,winner = deterEnd(board,currentPlayer)
	currentPlayer,turn = changeTurn(turn,player1,player2)
else:
	if winner == 'X':
		print('\nThe winner is player1')
	elif winner == 'O':
		print('\nThe winner is player2')
	else:
		print('\nNo winner. This is tie')
	showBoard(board)
