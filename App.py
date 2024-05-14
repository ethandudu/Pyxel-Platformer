import pyxel

import Player


class App:
    def __init__(self):
        pyxel.init(128, 128)
        self.player = Player.Player()
        pyxel.load("res.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.move()

    def draw(self):
        pyxel.cls(0)
        playercoords = self.player.getposition()
        pyxel.blt(playercoords[0], playercoords[1], 0, 0, 0, 16, 16, 0)


App()
