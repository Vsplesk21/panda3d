from direct.showbase.ShowBase import ShowBase
class Game(ShowBase):

    def __init__(self) :
        super().__init__(self)
        
        self.model = self.loader.loadModel('models/environment')
        self.model.reparentTo(self.render)
        self.panda = self.loader.loadModel('models/panda')
        self.panda.reparentTo(self.render)
game = Game()
game.run()