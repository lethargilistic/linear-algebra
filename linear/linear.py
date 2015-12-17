def addition(first, second):
    is_valid_matrix(first)
    is_valid_matrix(second)
    
    result = []
    for row in range(len(first)):
        nextRow = []
        for col in range(len(first[row])):
            nextRow.append(first[row][col] + second[row][col])
        result.append(nextRow)

    return result

def subtraction(first, second):
    is_valid_matrix(first)
    is_valid_matrix(second)
    
    result = []
    for row in range(len(first)):
        nextRow = []
        for col in range(len(first[row])):
            nextRow.append(first[row][col] - second[row][col])
        result.append(nextRow)

    return result

def multiplication(first, second):
    is_valid_matrix(first)
    is_valid_matrix(second)
    are_valid_for_multiplication(first, second)
    
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

#Only works for diagonal square matrices
def exponent(matrix, power):
    if not is_diagonal(matrix) or not is_square(matrix):
        raise ValueError
    result = matrix[:]
    for i in range(len(matrix)):
        result[i][i] **= power
    return result

def transpose(matrix):
    is_valid_matrix(matrix)

    transpose = []
    for row in range(len(matrix)):
        newRow = []
        for col in range(len(matrix[0])):
            newRow.append(matrix[col][row])
        transpose.append(newRow)

    return transpose

def is_square(a):
    return len(a) > 0 and len(a) == len(a[0])

#Not sure if it's required for diagonal matrix to be square
def is_diagonal(a):
    if not is_square(a):
        return False
    for i in range(len(a)):
        nums = list(range(len(a)))
        if a[i][i] == 0:
            return False
        nums.remove(i)
        for j in nums:
            if a[i][j] != 0:
                return False
    return True    

def is_identity(a):
    if not is_square(a):
        return False
    for i in range(len(a)):
        nums = list(range(len(a)))
        if a[i][i] != 1:
            return False
        nums.remove(i)
        for j in nums:
            if a[i][j] != 0:
                return False
    return True

#TODO: suport for empty matricies in other operations.
#TODO: It should be possible for there to be a 0-row, non-0-col matrix.
def is_empty_matrix(a):
    return len(a) == 0 or len(a[0]) == 0

#The name implies Boolean, but throws exceptions on failure
def is_valid_matrix(a):
    if type(a) != type(list()):
        raise TypeError

    rowLength = len(a[0])
    for row in a:
        if type(row) != type(list()):
            raise TypeError
        if len(row) != rowLength:
            raise ValueError
    return True

def are_same_size(a, b):
    is_valid_matrix(a)
    is_valid_matrix(b)
    return len(a) == len(b) and len(a[0]) == len(b[0])

def are_valid_for_multiplication(a, b):
    return len(a[0]) == len(b)

def are_transposed(a, b):
    if len(a[0]) != len(b) or len(a) != len(b[0]):
        return False
    for row in range(len(a)):
        for col in range(len(a[0])):
            if a[row][col] != b[col][row]:
                return False
    return True

def equals(a,b):
    raise NotImplementedError
