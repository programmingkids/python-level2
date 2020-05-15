# クラス定義
class Triangle :
    def __init__(self, base, height ) :
        self.base = base
        self.height = height
    
    def get_area(self) :
        area = (self.base * self.height) / 2
        return area


# インスタンス作成
triangle = Triangle(6,8)
# メソッド「get_area」を呼び出す
