from fractions import Fraction 

def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end="\t")
        print()

def getFraction(message):
    while True:
        rawInp = input(message)
        try:
            if "/" in rawInp: # Fraction
                inp = rawInp.split("/")
                num = int(inp[0])
                den = int(inp[1])
                return Fraction(num, den)
            else:
                return Fraction(int(rawInp), 1)
        except:
            print("Error: Invalid Input")
            continue

def getRowNum(message, matrix):
    length = len(matrix)
    while True:
        rawInp = input(message)
        try:
            inp = int(rawInp)
            if inp >= 0 and inp <= length:
                return inp - 1
            else:
                print("Error: Index out of range")
                continue
        except:
            print("Error: Invalid Input")
            continue

def cloneMatrix(matrix):
    clone = []
    for row in matrix:
        holder = []
        for num in row:
            holder.append(Fraction(num))
        clone.append(holder)
    return clone

rows = int(input("Matrix row: "))
columns = int(input("Matrix column: "))
matrix = []

for i in range(rows):
    holder = []
    for j in range(columns):
        holder.append(getFraction("matrix[%d][%d]: " %(i,j)))
    matrix.append(holder)

print("Input matrix: ")
printMatrix(matrix)
savedMatrix = [cloneMatrix(matrix)]
ind = 1

opt = "" 
while True:
    opt = input("Swap[w], Sum[s], Times[t], Undo[u] or Exit[x]: ")
    if opt == "w":
        row1 = getRowNum("Row 1 (1-based): ", matrix)
        row2 = getRowNum("Row 2 (1-based): ", matrix)
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
        ind += 1
        savedMatrix.append(cloneMatrix(matrix))
        printMatrix(matrix)
    elif opt == "s":
        x = getFraction("Enter coeff: ")
        row1 = getRowNum("Row multiplied (1-based): ", matrix)
        row2 = getRowNum("Row changed (1-based): ", matrix)
        for i in range(len(matrix[0])):
            matrix[row2][i] = matrix[row2][i] + (x * matrix[row1][i])
        ind += 1
        savedMatrix.append(cloneMatrix(matrix))
        printMatrix(matrix)
    elif opt == "t":
        x = getFraction("Enter coeff: ")
        row1 = getRowNum("Row added (1-based): ", matrix)
        for i in range(len(matrix[0])):
            matrix[row1][i] = x * matrix[row1][i]
        ind += 1
        savedMatrix.append(cloneMatrix(matrix))
        printMatrix(matrix)
    elif opt == "u":
        if ind == 1:
            print("Already at oldest change")
        else:
            savedMatrix.pop()
            ind -= 1
            matrix = cloneMatrix(savedMatrix[-1])
            printMatrix(matrix)
    elif opt == "x":
        break
    else:
        print("Error: Unrecognize command")


