def getTotal( data ) :
    total = 0
    for number in data :
        total += number
    return total

numbers = [5, 7, 2, 6]
answer = getTotal( numbers )
print( answer )
