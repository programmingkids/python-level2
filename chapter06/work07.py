# ここにクラスを定義します
class Player :
    def __init__(self, name, job, level) :
        self.name = name
        self.job = job
        self.level = level
    
    def fight(self) :
        print( self.name + "は" + self.job + "として戦った" )
        
    def show_level(self) :
        print( self.name + "のレベルは" + str(self.level))


# これ以降は修正してはいけません
player = Player("ドナルド", "勇者", 5)
player.fight()
player.show_level()
