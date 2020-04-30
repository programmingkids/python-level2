class Person:
    # コンストラクタ
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print("私の名前は" + self.name + "です")

    def show_age(self):
        print("私は" + str(self.age) + "才です")

# 1個目のインスタンス作成
person1 = Person("佐藤", 16)
person1.show_name()
person1.show_age()

print("=====")

# 2個目のインスタンス作成
person2 = Person("田中", 14)
person2.show_name()
person2.show_age()
