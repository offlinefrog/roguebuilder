from stats import AddStats, MultiStats, BonusStats
from registry import Companions, Pets

companions = {'LADYBUG', 'OCELOT', 'ANT', 'SILVERFISH', 'BEE', 'MONKEY', 'PARROT', 'CHICKEN',
              'SHEEP', 'CRAB', 'FROG', 'SNAIL', 'BAT', 'GOLDEN_MONKEY', 'POLAR_BEAR'}

class Player:
    @staticmethod
    def compute_base(build):
        flat = AddStats()
        multi = MultiStats()

        for obj in build:
            flat += getattr(obj, 'flat', AddStats())
            multi *= getattr(obj, 'multi', MultiStats())

        for name in companions:
            comp = getattr(Companions, name)
            flat += getattr(comp, 'perm_flat', AddStats())
            multi *= getattr(comp, 'perm_multi', AddStats())

        return flat * multi

    @staticmethod
    def compute_add(build):
        add = AddStats() + 1

        for obj in build:
            add += getattr(obj, 'add', AddStats())
        return add

    @staticmethod
    def compute_bonus(build):
        bonus = BonusStats(
            time=60,
            oak_per_break=1
        )

        for obj in build:
            bonus += getattr(obj, 'bonus', BonusStats())

        for name in companions:
            comp = getattr(Companions, name)
            bonus += getattr(comp, 'perm_bonus', BonusStats())

        return bonus

    def __init__(self, build: iter):
        self.base = self.compute_base(build)
        self.add = self.compute_add(build)

        self.bonus = self.compute_bonus(build)

        self.final = None
        self.current = self.base.hp

    def is_alive(self):
        if self.current > 0:
            return True
        return False

    def kill(self):
        self.current = 0

    def __repr__(self):
        return f'Player:\n{self.base.__str__()}'

class Pet:
    @staticmethod
    def compute_base(build):
        flat = AddStats()
        multi = MultiStats()

        for obj in build:
            flat += getattr(obj, 'pet_flat', AddStats())
            multi *= getattr(obj, 'pet_multi', MultiStats())

        for name in companions:
            comp = getattr(Companions, name)
            multi *= getattr(comp, 'perm_pet_multi', MultiStats())

        return flat * multi

    @staticmethod
    def compute_add(build):
        add = AddStats() + 1

        for obj in build:
            add += getattr(obj, 'pet_add', AddStats())
        return add

    def load(self, build, name):
        pet = getattr(Pets, name)
        self.name = pet.name

        self.base = pet.base + self.compute_base(build)
        self.add = self.compute_add(build)

        self.final = None
        self.current = self.base.hp

        self.buff_flat = pet.buff_flat
        self.buff_add = pet.buff_add

        self.buff_pet_flat = pet.buff_pet_flat
        self.buff_pet_add = pet.buff_pet_add

    def __init__(self, build: iter = None, name: str = None):
        self.name = ''

        self.base = AddStats()
        self.add = AddStats()

        self.final = AddStats()
        self.current = 0

        self.buff_flat = AddStats()
        self.buff_add = AddStats()

        self.buff_pet_flat = AddStats()
        self.buff_pet_add = AddStats()

        if name is not None:
            self.load(build, name)

    def is_alive(self):
        if self.current > 0:
            return True
        return False

    def __repr__(self):
        if self.name is not None:
            return f'{self.name}:\n{self.base.__str__()}'
        return None