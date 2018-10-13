import random

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
				For Search Algorithms
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

bfsQueue = []
dfsQueue = []
UCQueue = []
AStrQueue = []

'''
BFS add to queue 
'''
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
	# Your code here
	bfsQueue.append((node_id, parent_node_id))
	# Nodes go at the end of the queue
	return

'''
BFS check if empty
'''
def is_queue_empty_BFS():
	# Your code here
	if bfsQueue:
		return False
	else:
		return True

'''
BFS pop from queue
'''
def pop_front_BFS():
	(node_id, parent_node_id) = bfsQueue.pop(0)
	#first index
	# Your code here
	return (node_id, parent_node_id)




'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
	# Your code here
	dfsQueue.insert(0, (node_id,parent_node_id))
	#insert node at front
	return

'''
DFS check if empty
'''
def is_queue_empty_DFS():
	# Your code here
	if dfsQueue:
		return False
	else:
		return True

'''
DFS pop from queue
'''
def pop_front_DFS():
	(node_id, parent_node_id) = dfsQueue.pop(0)
	#pop front node
	# Your code here
	return (node_id, parent_node_id)




'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
	# Your code here
	return

'''
UC check if empty
'''
def is_queue_empty_UC():
	if UCQueue:
		return False
	else:
		return True

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
	if AStrQueue:
		return False
	else:
		return True

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
	#n = 8
	for x in range(n):
		state.append(random.randint(0, n-1))
		# print(state)
	
	
	# state = [4,5,7,5,2,5,1]
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
	
	
	#Copy state into ORI state for safe keeping
	oriState = []
	for i in range(len(state)):
		oriState.append(state[i])
	
	oriConflicts = comp_att_pairs(oriState)
	
	#print(state)
	#print(oriState)
	
	n = len(state)
	nLimit = n-1
	
	prevConflicts = oriConflicts
	minCol = n + 1
	minRow = n + 1
	
	minConflicts = oriConflicts -1
	while (1):
		print("START ITERATION")
		colStateIndex = 0
		
		
		minConflicts = comp_att_pairs(state)
		print("Minimum value set to: " +str(minConflicts))
		while colStateIndex <= nLimit:
			# for each column in state[]
			print(">> Column " + str(colStateIndex) + " of " + str(nLimit))
			potentialRow = 0
			originalValue = state[colStateIndex]
			
			
			# print ("State RESET: " + str(state))
			
			while potentialRow <= nLimit:
				
				state[colStateIndex] = potentialRow
				# print state
				#keep track of minimum x value (change variable names after)
				tempMin = comp_att_pairs(state)
				print ("Conflicts at "+ str(potentialRow) + "," + str(colStateIndex) + " is: " + str(tempMin))
				
				if (tempMin < minConflicts):
					minConflicts = tempMin
					minCol = colStateIndex
					minRow = potentialRow
					
				potentialRow+=1
			
			minTuple = (minConflicts, "@", minRow, minCol)
			print(">>> So far the minimum is: " + str(minTuple))
			state[colStateIndex] = originalValue
			colStateIndex+= 1
		
		
		#Just for checking
		newState = []
		for i in range(len(state)):
			newState.append(state[i])
			
		newState[minCol] = minRow
		
		print("Changing states from " + str(state) + " to " + str(newState))
		print("Conflicts lowered from " + str(comp_att_pairs(state)) + " to " + str(comp_att_pairs(newState)))
		
		#Keep this
		state[minCol] = minRow
		if (minConflicts == 0):
			print("Broken with 0")
			break
		elif (prevConflicts == minConflicts):
			print("Broken with matching prev and curr conflicts")
			break
		else:
			prevConflicts = minConflicts
		
	print("BROKEN :D")
	
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
	
	
	return state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
	final_state = []
	# Your code here
	
	conflicts = n * n
	while (conflicts != 0):
		state = get_random_state(n)
		final_state = hill_descending(state, comp_att_pairs)
		conflicts = comp_att_pairs(final_state)
	
	
	return final_state






