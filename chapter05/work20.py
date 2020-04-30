# 関数の定義は今までと同じです
def add( a, b ) :
    total = a + b
    return total

# 普通に関数呼び出し
print( add(3,2) )

# キーワード引数で関数呼び出す
print( add(b=4, a=3) )
