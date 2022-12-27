from sport import Sport

class Game(Sport):
    def tools(self):
        return "ball"
    pass

soccer = Game("play ball", 12)
print(soccer.tools())
print(soccer.rule)
print(soccer.player)