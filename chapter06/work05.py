class Person:
    # コンストラクタ
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print("私の名前は" + self.name + "です")

    def show_age(self):
        print("私は" + str(self.age) + "才です")

