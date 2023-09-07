from direct.showbase.ShowBase import ShowBase
import code2

class Game(ShowBase):
    def __init__(self):
        super().__init__(self)
        land = code2.Mapmanager()

game = Game()
game.run()