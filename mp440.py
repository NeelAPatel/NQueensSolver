import random

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
				For Search Algorithms
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
BFS add to queue 
'''
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
	# Your code here
	 return

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
	# Your code here
	return False

'''
BFS pop from queue
'''
def pop_front_BFS():
	(node_id, parent_node_id) = (0, 0)
	# Your code here
	return (node_id, parent_node_id)

'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
	# Your code here
	return

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
	# Your code here
	return False

'''
DFS pop from queue
'''
def pop_front_DFS():
	(node_id, parent_node_id) = (0, 0)
	# Your code here
	return (node_id, parent_node_id)

'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
	# Your code here
	return

'''
UC add to queue 
'''
def is_queue_empty_UC():
	# Your code here
	return False

'''
UC pop from queue
'''
def pop_front_UC():
	(node_id, parent_node_id) = (0, 0)
	# Your code here
	return (node_id, parent_node_id)

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
	# Your code here
	return

'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
	# Your code here
	return False

'''
A* pop from queue
'''
def pop_front_ASTAR():
	(node_id, parent_node_id) = (0, 0)
	# Your code here
	return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
				For n-queens problem
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
	state = []
	# GENERATE nQueens
	# n = 8
	for x in range(n):
		state.append(random.randint(0, n-1))
		# print(state)
	
	print state
	return state

'''
Compute pairs of queens in conflict 
'''


# noinspection PyRedundantParentheses
def compute_attacking_pairs(state):
	
	# count number of elements in state
	n = len(state)
	nLimit = n-1
	# ==== CREATE AND INITIALIZE TABLE
	
	# Create table: Table of empty rows
	arrTable = [[] for _ in range(n)]
	#print arrTable

	# Initialize table:
	rowIndex = 0
	while rowIndex <= nLimit:
		for x in range(n):
			arrTable[rowIndex].append('')
		#print arrTable
		rowIndex += 1
		#print("============")
	#print arrTable
	
	# add queens
	colIndex = 0
	while (colIndex <= nLimit):
		rowVal = state[colIndex]
		arrTable[rowVal][colIndex] = 'Q'
		colIndex += 1
	#print arrTable

	# ==== COMPUTE ATTACKS

	# Horizontal | Checks if the same number exists elsewhere in the state[]
	hAttacks = 0
	for stateIndex in range(n):
		selected = state[stateIndex]
		# print("SELECTED VAL: " + str(selected))
		subRange = nLimit - stateIndex
		for subIndex in range(subRange):
			#print("new arr: " + str(state[index + newIndex + 1]))
			if (state[stateIndex + subIndex + 1] == selected):
				hAttacks += 1

	# print("Horizontal hits: " + str(hAttacks))

	# Diagonals
	qCol = 0
	stateIndex = 0
	totalDiagonalHits = 0
	while qCol <= nLimit:
		# Get queen's row value
		qRow = state[stateIndex]
		#Queen's coordinate = its row and column.
		qCoordTpl = (qRow+1, qCol+1)
		#Print for confirmation. If Q shows up = ready
		# print(">>>>>>>>>>>>>Queen: @ " + str(qCoordTpl) + " : " + str(arrTable[qRow][qCol]))
	
		
		# Down Right (+ +)
		# Current position = qRow, qCol
		diagonalHit = 0
		subQRow = qRow + 1
		subQCol = qCol + 1
		while (subQRow <= n-1 and subQCol <= n-1):
			if (arrTable[subQRow][subQCol] == arrTable[qRow][qCol]):
				
				hitTpl = (arrTable[qRow][qCol], arrTable[subQRow][subQCol])
				subQCoordTpl = (subQRow +1, subQCol + 1)
				
				# print("HIT: [" + str(hitTpl) + "]" + "[(" + str(qCoordTpl) + ") X (" + str(subQCoordTpl) + ")]")
				diagonalHit += 1
			subQRow += 1
			subQCol += 1
			
		
		# Up Right (- +)
		subQRow = qRow - 1
		subQCol = qCol + 1
		while (subQRow >= 0 and subQCol <= n-1):
			if (arrTable[subQRow][subQCol] == arrTable[qRow][qCol]):
				hitTpl = (arrTable[qRow][qCol], arrTable[subQRow][subQCol])
				subQCoordTpl = (subQRow + 1, subQCol + 1)
				
				# print("HIT: [" + str(hitTpl) + "]" + "[(" + str(qCoordTpl) + ") X (" + str(subQCoordTpl) + ")]")
				diagonalHit += 1
			subQRow -= 1
			subQCol += 1
			
	
		# print ("DIAGONAL HITS  @ " + str(qRow + 1) + "," + str(qCol + 1) + ": " + str(diagonalHit))
		totalDiagonalHits += diagonalHit
		# iteration
		qCol += 1
		stateIndex += 1

	totalHits = totalDiagonalHits + hAttacks

	# print("TOTAL HITS: " + str(totalHits))
	
	number_attacking_pairs = totalHits
	
	return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
	final_state = []
	
	oriState = state
	n = len(state)
	nLimit = n-1
	
	colStateIndex = 0
	minCol = 0
	minRow = 0
	
	potentialRow = 0
	while colStateIndex <= nLimit:
		# for each column in state[]
		print(">> Column " + str(colStateIndex) + " of " + str(nLimit))
		potentialRow = 0
		# Reset state here
		while potentialRow <= nLimit:
			
			state[colStateIndex] = potentialRow
			print state
			#keep track of minimum x value (change variable names after)
			x=comp_att_pairs(state)
			print ("Conflicts at "+ str(potentialRow) + "," + str(colStateIndex) + " is: " + str(x))
			potentialRow+=1
		colStateIndex+= 1
	
	
	
	'''
	> Create empty table based on len(state) x len(state) size
	
	> Loop through table and fill out 'potential' numbers
	
	while (each column)
		while(each row)
			coordinate = (row,col)
			newState = [ replace row value for each iteration ]
			attacks = compute_attacking_pairs(newState)
			potentialTable[r][c] = attacks
			
			
			keep going until every place is filled out
	
	> By this point you will have a table for the FIRST state array about what happens when you move a queen up or down
	
	> now idk what to do.
	'''
	
	
	return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
	final_state = []
	# Your code here
	return final_state






