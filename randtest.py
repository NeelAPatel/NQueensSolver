import random
# GENERATE nQueens
arr = []
for x in range(8):
	arr.append( random.randint(1,8))
	print(arr)


# Create table
arrTable = [[] for _ in range(8)]
print arrTable

#initialize table
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
	arrTable[rowVal-1][index] = 'Q'
	index+=1

print arrTable

#Horizontal
hAttacks = 0
for index in range(8):
	selected = arr[index]
	print("SELECTED VAL: " + str(selected))
	newRange = 7 - index
	for newIndex in range(newRange):
		print("new arr: " + str(arr[index + newIndex+1]))
		if (arr[index + newIndex+1] == selected):
			hAttacks+=1



print("Horizontal attacks: " + str(hAttacks))



 #Diagonal
dAttacks = 0
for index in range(8):
	currVal = arr[index]
	print("curr VAL: " + str(currVal))
	currCopy = currVal
	newRange = 7 - index
	for newIndex in range(newRange):
		print("new arr: " + str(arr[index + newIndex+1]))
		if (arr[index + newIndex+1] == selected):
			hAttacks+=1