def say_message():
    # global変数として扱う
    global message
    # グローバル変数「message」への代入
    message = "How are you"
    # 「How are you」と表示
    print(message)

# これはグローバル変数
message = "Hello"

# 「Hello」と表示
print( message )

say_message()

# 「How are you」と表示
print(message)
