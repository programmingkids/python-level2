# ここにクラスを定義します
class Character :
    def __init__(self, name, hp, weapon) :
        self.name = name
        self.hp = hp
        self.weapon = weapon
    
    def show_hp(self) :
        print( self.name + "のHPは" + str(self.hp) )
        
    def show_weapon(self) :
        print( self.name + "の武器は" + self.weapon)


# これ以降は修正してはいけません
c1 = Character("ミッキー" , 15, "鋼の剣")
c1.show_hp()
c1.show_weapon()

print("=====")

c2 = Character("ミニー", 12, "光の剣")
c2.show_hp()
c2.show_weapon()
