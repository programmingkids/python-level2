# 普通に関数を定義
def add ( a, b ) :
    return a + b

# 変数に関数を代入
tashizan = add

# 普通に関数を呼び出すこともできます
answer1 = add(5, 3)
print( answer1 )

# 変数から関数を呼び出すこともできます
answer2 = tashizan(8, 3)
print( answer2 )
