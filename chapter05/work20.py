# 関数の定義は今までと同じです
def divide( a, b ) :
    answer = a / b
    return answer

# 普通に関数呼び出し
print( divide( 10,2 ) )

# キーワード引数で関数呼び出す
print( divide( b=10, a=2 ) )
