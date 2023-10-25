class Object:
    def __init__(self, x, y, texture):
        self.pos = (x, y)
        self.texture = texture
        self.isDestroyed = False
        self.hasAnimation = False
        self.animationList = []
        self.health = 100

    def setAnimation(self, animationList):
        self.animationList = animationList

    def getAnimation(self):
        return self.animationList

    def canMove(self):
        pass

    def move(self):
        pass

    def setHealth(self, health):
        self.health = health

    def getHealth(self):
        return self.health


class Player(Object):
    def __init__(self, x, y, texture):
        super().__init__(x, y, texture)
        self.isUsingSpear = False

    def useSpear(self):
        pass

    def spearCollideWithEnemy(self):
        pass

    def blowUpEnemy(self):
        pass

    def playerControls(self):
        pass


class Enemy(Object):
    def __init__(self, x, y, texture):
        super().__init__(x, y, texture)

    def trackPlayer(self):
        pass


class Rock(Object):
    def __init__(self, x, y, texture):
        super().__init__(x, y, texture)
        self.playerUnder = False

    def fall(self):
        pass


class Fygar(Enemy):
    def __init__(self, x, y, texture):
        super().__init__(x, y, texture)
        self.isBreathingFire = False

    def breathFire(self):
        pass


class Pookas(Enemy):
    pass

