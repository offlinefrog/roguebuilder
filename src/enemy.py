from stats import MultiStats
from registry import Companions, Waves

companions = {'LADYBUG', 'OCELOT', 'ANT', 'SILVERFISH', 'BEE', 'MONKEY', 'PARROT', 'CHICKEN',
              'SHEEP', 'CRAB', 'FROG', 'SNAIL', 'BAT', 'GOLDEN_MONKEY', 'POLAR_BEAR'}

class Enemy:

    @staticmethod
    def compute_multi(build):
        multi = MultiStats()

        for obj in build:
            multi *= getattr(obj, 'enemy_multi', MultiStats())

        for name in companions:
            comp = getattr(Companions, name)
            multi *= getattr(comp, 'perm_enemy_multi', MultiStats())

        return multi

    def __init__(self, build, name):
        self.name = name

        self.base = getattr(Waves, name).base
        self.multi = self.compute_multi(build)

        self.final = self.base * self.multi
        self.max = getattr(Waves, name).max

    def is_alive(self):
        if self.final.hp > 0:
            return True
        return False

    def __repr__(self):
        return f'{self.name}:\n{self.base.__str__()}'