import random

# GENERATE nQueens
arr = []
for x in range(8):
	arr.append(random.randint(1, 8))
	print(arr)

# Create table
arrTable = [[] for _ in range(8)]
print arrTable

# initialize table
rowIndex = 0
while rowIndex <= 7:
	for x in range(8):
		arrTable[rowIndex].append('')
	print arrTable
	rowIndex += 1
	print("============")

# add queens
index = 0
while (index <= 7):
	rowVal = arr[index]
	arrTable[rowVal - 1][index] = 'Q'
	index += 1

print arrTable

# Horizontal
hAttacks = 0
for index in range(8):
	selected = arr[index]
	print("SELECTED VAL: " + str(selected))
	newRange = 7 - index
	for newIndex in range(newRange):
		print("new arr: " + str(arr[index + newIndex + 1]))
		if (arr[index + newIndex + 1] == selected):
			hAttacks += 1

print("Horizontal attacks: " + str(hAttacks))

# Diagonal
qCol = 0
arrIndex = 0
totalDiagonalHits = 0
while qCol <= 7:
	qRow = arr[arrIndex] - 1
	print( ">>>>>>>>>>>>>Queen: @ " + str(qRow+1) + "," + str(qCol+1) + " : "  + str(arrTable[qRow][qCol]))

	# Down Right (+ +)
	# Current position = qRow, qCol
	diagonalHit = 0
	subQRow = qRow + 1
	subQCol = qCol + 1
	while (subQRow <= 7 and subQCol <= 7):
		if (arrTable[subQRow][subQCol] == arrTable[qRow][qCol]):
			x = arrTable[qRow][qCol]
			y = arrTable[subQRow][subQCol]
			print("HIT: [" + x + "," + y +"]" +  "[ (" + str(qRow+1) + "," + str(qCol+1) + ")(" + str(subQRow+1) + "," + str(subQCol+1) + ")]")
			diagonalHit += 1
		subQCol += 1
		subQRow += 1

	subQRow = qRow - 1
	subQCol = qCol + 1
	while (subQRow >= 0 and subQCol <= 7):
		if (arrTable[subQRow][subQCol] == arrTable[qRow][qCol]):
			x = arrTable[qRow][qCol]
			y = arrTable[subQRow][subQCol]
			print("HIT: [" + x + "," + y + "]" + "[ (" + str(qRow + 1) + "," + str(qCol + 1) + ")(" + str(
				subQRow + 1) + "," + str(subQCol + 1) + ")]")
			diagonalHit += 1
		subQCol += 1
		subQRow -= 1

	print ("DIAGONAL HITS  @ " + str(qRow+1) + "," + str(qCol+1)+ ": " + str(diagonalHit))
	totalDiagonalHits += diagonalHit
	#iteration
	qCol+=1
	arrIndex+=1

totalHits = totalDiagonalHits + hAttacks

print("TOTAL HITS: " + str(totalHits))