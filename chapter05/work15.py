# ここに関数を作成します
def getEvenTotal( data ) :
    total = 0
    for number in data :
        if number % 2 == 0 :
            total += number
    return total

# これ以降は修正してはいけません
numbers = [2,5,7,8,6,9]
r = getEvenTotal( numbers )
print( r )
