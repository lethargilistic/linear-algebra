def addition(first, second):
    isValidMatrix(first)
    isValidMatrix(second)
    
    result = []
    for row in range(len(first)):
        nextRow = []
        for col in range(len(first[row])):
            nextRow.append(first[row][col] + second[row][col])
        result.append(nextRow)

    return result

def subtraction(first, second):
    isValidMatrix(first)
    isValidMatrix(second)
    
    result = []
    for row in range(len(first)):
        nextRow = []
        for col in range(len(first[row])):
            nextRow.append(first[row][col] - second[row][col])
        result.append(nextRow)

    return result

def multiplication(first, second):
    isValidMatrix(first)
    isValidMatrix(second)
    
    areValidForMultiplication(first, second)
    
    result = []
    firstRows = len(first)
    firstCols = len(first[0])
    secondRows = len(first)
    secondCols = len(first[0])

    for k in range(secondCols):
        newRow = []
        for i in range(firstRows):
            nextElm = 0
            for j in range(firstCols):
                nextElm += first[j][i]*second[k][j]
            newRow.append(nextElm)
        result.append(newRow)
    return result

def transpose(matrix):
    isValidMatrix(matrix)

    transpose = []
    for row in range(len(matrix)):
        newRow = []
        for col in range(len(matrix[0])):
            newRow.append(matrix[col][row])
        transpose.append(newRow)

    return transpose

def areSameSize(a, b):
    return len(a) != len(b) or len(a[0]) != len(b)

def isValidMatrix(a):
    rowLength = len(a[0])
    for row in a:
        if len(row) != rowLength:
            return False #Should throw exception.
    return True

#TODO
def areValidForMultiplication(a, b):
    return True

#TODO: a,b compatibility validation
def areTranspose(a, b):
    for row in range(len(a)):
        for col in range(len(a[0])):
            if a[row][col] != b[col][row]:
                return False
    return True
            
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3],[4,5,6],[7,8,9]]
print(addition(a,b))
print(subtraction(a,b))
print(multiplication(a,b))
t = transpose(a)
print(t)
print(areTranspose(a,t))
t[0][0] = 99
print(areTranspose(a,t))
