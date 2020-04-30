# クラス定義
class Person:
    def say_name(self):
        # インスタンスが保持する属性を使う場合、「self.name」となります
        print("I am " + self.name)

    def say_age(self):
        # インスタンスが保持する属性を使う場合、「self.age」となります
        print("I am " + str(self.age) + " years old")


# インスタンス作成
person1 = Person()
# インスタンスのデータ属性に「name」に値を代入
person1.name = "Micky"
# インスタンスのデータ属性に「age」に値を代入
person1.age = 17
# メソッド呼び出し
person1.say_name()
person1.say_age()
