# クラス定義は修正しません
class Triangle :
    def get_area(self) :
        area = (self.width * self.height) / 2
        return  area

# インスタンス作成、データ属性に値を代入、メソッド呼び出しを行う
t1 = Triangle()
t1.width = 5
t1.height = 6
answer = t1.get_area()
print( answer )
