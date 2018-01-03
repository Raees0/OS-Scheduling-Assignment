import random
def Instructions():
	print "---INSTRUCTIONS---"
	print "1- Enter Row number and column number to make move\n2- If you select an already occupied location, your turn will be losted.\n 	So be CAREFUL while making moves\n\n"

def Board(a0,a1,a2) :
    print('.............')
    print('|   |   |   |')
    print('| ' + a0[0] + ' | ' + a0[1] + ' | ' + a0[2] + ' | ')
    print('|   |   |   |')
    print('|---+---+---|')
    print('|   |   |   |')
    print('| ' + a1[0] + ' | ' + a1[1] + ' | ' + a1[2] + ' |')
    print('|   |   |   |')
    print('|---+---+---|')
    print('|   |   |   |')
    print('| ' + a2[0] + ' | ' + a2[1] + ' | ' + a2[2] + ' |')
    print('|___|___|___|')

def move(a0,a1,a2,letter,row,col):
	if row == 1 and col == 1:
		if a0[0] == ' ':
			a0[0]=letter
		else:
			print "As Location is already occupied, You wasted your turn.\nPlease select location carefully"
	elif row == 1 and col == 2:
		if a0[1] == ' ':
			a0[1]=letter
		else:
			print "As Location is already occupied, You wasted your turn.\nPlease select location carefully"
		
	elif row == 1 and col == 3:
		if a0[2] == ' ':
			a0[2]=letter
		else:
			print "As Location is already occupied, You wasted your turn.\nPlease select location carefully"
	elif row == 2 and col == 1:
		if a1[0] == ' ':
			a1[0]=letter
		else:
			print "As Location is already occupied, You wasted your turn.\nPlease select location carefully"
	elif row == 2 and col == 2:
		if a1[1] == ' ':
			a1[1]=letter
		else:
			print "As Location is already occupied, You wasted your turn.\nPlease select location carefully"
	elif row == 2 and col == 3:
		if a1[2] == ' ':
			a1[2]=letter
		else:
			print "As Location is already occupied, You wasted your turn.\nPlease select location carefully"
	elif row == 3 and col == 1:
		if a2[0] == ' ':
			a2[0]=letter
		else:
			print "As Location is already occupied, You wasted your turn.\nPlease select location carefully"
	elif row == 3 and col == 2:
		if a2[1] == ' ':
			a2[1]=letter
		else:
			print "As Location is already occupied, You wasted your turn.\nPlease select location carefully"

	elif row == 3 and col == 3:
		if a2[2] == ' ':
			a2[2]=letter
		else:
			print "As Location is already occupied, You wasted your turn.\nPlease select location carefully"

	#print letter	
	#Board(a0,a1,a2)	

def checkWin(a0,a1,a2,letter):
	return ((a0[0] == letter and a0[1] == letter and a0[2] == letter) or # checking hor. rows
	(a1[0] == letter and a1[1] == letter and a1[2] == letter) or   # checking hor. rows
	(a2[0] == letter and a2[1] == letter and a2[2] == letter) or   # checking hor. rows
	(a0[0] == letter and a1[0] == letter and a2[0] == letter) or   # checking vertically
	(a0[1] == letter and a1[1] == letter and a2[1] == letter) or   # checking vertically
	(a0[2] == letter and a1[2] == letter and a2[2] == letter) or   # checking vertically
	(a0[0] == letter and a1[1] == letter and a2[2] == letter) or   # checking diagonally
	(a0[2] == letter and a1[1] == letter and a2[0] == letter))  # checking diagonally
	
def isEmpty(a0,a1,a2):
	return((a0[0] == ' ') or (a0[1] == ' ') or (a0[2] == ' ') or
		(a1[0] == ' ') or (a1[1] == ' ') or (a1[2] == ' ') or
		(a2[0] == ' ') or (a2[1] == ' ') or (a2[2] == ' '))	

def main ():
	print "---TIC TAC TOE---\n"
	Instructions()
	
	a0=[' ',' ',' ']
	a1=[' ',' ',' ']
	a2=[' ',' ',' ']
	Board(a0,a1,a2)
	print "\nPlayer 1 = X\n"
	print "Player 2 = O\n"
	x=0
# input move
	while isEmpty(a0,a1,a2):
		#player 1
		print "\nPlayer 1's turn"

		while 1:
			row=input("Enter row: ")
			if row<1 or row>3:
				print "Invalid input\n"
			else:
				break
		while 1:		
			col=input("Enter Column: ")
			
			if col<1 or col>3:
				print "Invalid input\n"
			else:
				break		

		letter='X'
		
		move(a0,a1,a2,letter,row,col)
		Board(a0,a1,a2)
		
		if checkWin(a0,a1,a2,letter):
			print "Player 1 Won...*_*\n"
			x = 1	
			break
		#player 2
		if isEmpty(a0,a1,a2):		
			print "\nPlayer 2's turn"
			while 1:
				row=input("Enter row: ")
				if row<1 or row>3:
					print "Invalid input\n"
				else:
					break
			while 1:		
				col=input("Enter Column: ")
			
				if col<1 or col>3:
					print "Invalid input\n"
				else:
					break
			letter='O'
		
			move(a0,a1,a2,letter,row,col)
			Board(a0,a1,a2)
				
			if checkWin(a0,a1,a2,letter):
				print "Player 2 Won...*_*\n"
				x = 1			
				break
	if x == 0:
		print "Match drawed"	

if __name__ == "__main__":
    main()
