import pyxel


class Player:
    def __init__(self):
        self.x = 64
        self.y = 64
        self.life = 3

    def move(self):
        """Handle the player's movement."""
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x < 120:
                self.x = self.x + 1
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.x > 0:
                self.x = self.x - 1
        if pyxel.btn(pyxel.KEY_DOWN):
            if self.y < 120:
                self.y = self.y + 1
        if pyxel.btn(pyxel.KEY_UP):
            if self.y > 0:
                self.y = self.y - 1

    def getposition(self):
        """Return the player's coordinates."""
        return self.x, self.y

