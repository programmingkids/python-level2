# クラス定義
class Person:
    # 引数のあるメソッド
    def say_name(self, name):
        print("I am " + name)

# インスタンス作成
person1 = Person()
# 引数のあるメソッド呼び出し
person1.say_name("Tanaka")
