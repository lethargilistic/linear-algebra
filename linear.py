def addition(first, second):
    #How to handle improper input?
    result = []
    for row in range(len(first)):
        nextRow = []
        for col in range(len(first[row])):
            nextRow.append(first[row][col] + second[row][col])
        result.append(nextRow)

    return result

def subtraction(first, second):
    #How to handle improper input?
    result = []
    for row in range(len(first)):
        nextRow = []
        for col in range(len(first[row])):
            nextRow.append(first[row][col] - second[row][col])
        result.append(nextRow)

    return result

def multiplication(first, second):
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

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3],[4,5,6],[7,8,9]]
print(addition(a,b))
print(subtraction(a,b))

print(multiplication(a,b))
