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
def compute_attacking_pairs(state):
	number_attacking_pairs = 0
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

	# Horizontal
	hAttacks = 0
	for index in range(n):
		selected = state[index]
		print("SELECTED VAL: " + str(selected))
		newRange = nLimit - index
		for newIndex in range(newRange):
			#print("new arr: " + str(state[index + newIndex + 1]))
			if (state[index + newIndex + 1] == selected):
				hAttacks += 1

	print("Horizontal attacks: " + str(hAttacks))

	# Diagonals
	qCol = 0
	arrIndex = 0
	totalDiagonalHits = 0
	while qCol <= nLimit:
		qRow = state[arrIndex]
		print(">>>>>>>>>>>>>Queen: @ " + str(qRow + 1) + "," + str(qCol + 1) + " : " + str(arrTable[qRow][qCol]))
	
		# Down Right (+ +)
		# Current position = qRow, qCol
		diagonalHit = 0
		subQRow = qRow + 1
		subQCol = qCol + 1
		while (subQRow <= n-1 and subQCol <= n-1):
			if (arrTable[subQRow][subQCol] == arrTable[qRow][qCol]):
				x = arrTable[qRow][qCol]
				y = arrTable[subQRow][subQCol]
				print("HIT: [" + x + "," + y + "]" + "[ (" + str(qRow + 1) + "," + str(qCol + 1) + ")(" + str(
					subQRow + 1) + "," + str(subQCol + 1) + ")]")
				diagonalHit += 1
			subQCol += 1
			subQRow += 1
	
		subQRow = qRow - 1
		subQCol = qCol + 1
		while (subQRow >= 0 and subQCol <= n-1):
			if (arrTable[subQRow][subQCol] == arrTable[qRow][qCol]):
				x = arrTable[qRow][qCol]
				y = arrTable[subQRow][subQCol]
				print("HIT: [" + x + "," + y + "]" + "[ (" + str(qRow + 1) + "," + str(qCol + 1) + ")(" + str(
					subQRow + 1) + "," + str(subQCol + 1) + ")]")
				diagonalHit += 1
			subQCol += 1
			subQRow -= 1
	
		print ("DIAGONAL HITS  @ " + str(qRow + 1) + "," + str(qCol + 1) + ": " + str(diagonalHit))
		totalDiagonalHits += diagonalHit
		# iteration
		qCol += 1
		arrIndex += 1

	totalHits = totalDiagonalHits + hAttacks

	print("TOTAL HITS: " + str(totalHits))
	
	
	
	return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
	final_state = []
	# Your code here
	return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
	final_state = []
	# Your code here
	return final_state






