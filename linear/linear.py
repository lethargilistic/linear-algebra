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
    firstRows = secondCols = len(first)
    firstCols = len(first[0])
    secondRows = len(first)

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

def isSquare(a):
    return len(a) > 0 and len(a) == len(a[0])

def isIdentity(a):
    if not isSquare(a):
        return False
    for i in range(len(a)):
        nums = range(len(a))
        if a[i][i] != 1:
            return False
        nums.remove(i)
        for j in nums:
            if a[i][j] != 0:
                return False
    return True

#TODO: suport for empty matricies in other operations.
#TODO: It should be possible for there to be a 0-row, non-0-col matrix.
def isEmptyMatrix(a):
    return len(a) == 0 or len(a[0]) == 0

def isValidMatrix(a):
    if type(a) != type(list()):
        raise TypeError

    rowLength = len(a[0])
    for row in a:
        if type(row) != type(list()):
            raise TypeError
        if len(row) != rowLength:
            raise ValueError
    return True

def areSameSize(a, b):
    return len(a) != len(b) or len(a[0]) != len(b)

def areValidForMultiplication(a, b):
    return len(a[0]) == len(b)

def areTranspose(a, b):
    if len(a[0]) != len(b) or len(a) != len(b[0]):
        return False
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
