from dataclasses import dataclass, fields, MISSING

STATS = {'dmg', 'hp', 'hpr'}

@dataclass
class AddStats:
    dmg: int | float = 0
    hp: int | float = 0
    hpr: int | float = 0

    def __imul__(self, other: int) -> 'AddStats':
        for stat in STATS:
            setattr(self, stat, getattr(self, stat) * other)
        return self

    def __iadd__(self, other: 'AddStats') -> 'AddStats':
        for stat in STATS:
            setattr(self, stat, getattr(self, stat) + getattr(other, stat))
        return self

    def __mul__(self, other: (int, 'MultiStats', 'AddStats')) -> 'AddStats':
        kwargs = {}
        for stat in STATS:
            if isinstance(other, int):
                kwargs[stat] = getattr(self, stat) * other
            elif isinstance(other, MultiStats) or isinstance(other, AddStats):
                kwargs[stat] = int(getattr(self, stat) * getattr(other, stat))
        return AddStats(**kwargs)

    def __add__(self, other: (int, float, 'AddStats')) -> 'AddStats':
        kwargs = {}
        for stat in STATS:
            if isinstance(other, int) or isinstance(other, float):
                kwargs[stat] = getattr(self, stat) + other
            elif isinstance(other, AddStats):
                kwargs[stat] = getattr(self, stat) + getattr(other, stat)
        return AddStats(**kwargs)

    def __repr__(self):
        return f'DMG: {self.dmg}\nHP: {self.hp}\nHPR: {self.hpr}'

@dataclass
class MultiStats:
    dmg: float = 1.0
    hp: float = 1.0
    hpr: float = 1.0

    def __imul__(self, other: (int, 'MultiStats')) -> 'MultiStats':
        for stat in STATS:
            if isinstance(other, int):
                value = getattr(self, stat)
                if value != 0:
                    if value < 1:
                        base = 1 / value
                        new_val = 1 / (1 + (base - 1) * other)
                    else:
                        new_val = 1 + (value - 1) * other
                    setattr(self, stat, new_val)
            elif isinstance(other, MultiStats):
                setattr(self, stat, getattr(self, stat) * getattr(other, stat))
        return self

@dataclass
class BonusStats:
    speed: int | float = 0
    time: int = 0

    oak_per_break: int = 0
    cobblestone_per_break: int = 0
    iron_per_break: int = 0

    all_collector_speed: float = 0.0
    mine_collector_speed: float = 0.0
    wood_collector_speed: float = 0.0
    desert_collector_speed: float = 0.0
    snowy_collector_speed: float = 0.0
    magical_collector_speed: float = 0.0
    fishing_collector_speed: float = 0.0
    toxic_collector_speed: float = 0.0
    slime_factory_processing_speed: float = 0.0
    gem_excavation_speed: float = 0.0
    volcanic_eruption_speed: float = 0.0

    farm_size: float = 0.0
    food_effectiveness: float = 0.0
    food_duration: float = 0.0

    stars: float = 1.0
    ruby_generation_speed: float = 1.0
    companion_xp: float = 1.0

    misc: (str, True) = ('', False)

    @staticmethod
    def scale_multi(self, other):
        if self != 0:
            if self < 1:
                return 1 / (1 + ((1 / self) - 1) * other)
            return 1 + (self - 1) * other
        return 0

    def __imul__(self, other: int) -> 'BonusStats':
        self.speed = int(self.speed * other)
        self.time *= other

        self.all_collector_speed *= other
        self.mine_collector_speed *= other
        self.wood_collector_speed *= other
        self.desert_collector_speed *= other
        self.snowy_collector_speed *= other
        self.magical_collector_speed *= other
        self.fishing_collector_speed *= other
        self.toxic_collector_speed *= other
        self.slime_factory_processing_speed *= other
        self.gem_excavation_speed *= other
        self.volcanic_eruption_speed *= other

        self.farm_size *= other
        self.food_effectiveness *= other
        self.food_duration *= other

        self.stars = self.scale_multi(self.stars, other)
        self.ruby_generation_speed = self.scale_multi(self.ruby_generation_speed, other)
        self.companion_xp = self.scale_multi(self.companion_xp, other)

        if self.misc[1]:
            if other >= 7:
                self.misc[0].replace('_', 'Birch')
            elif other >= 4:
                self.misc[0].replace('_', 'Stone')
            elif other >= 1:
                self.misc[0].replace('_', 'Oak')

        return self

    def __iadd__(self, other: 'BonusStats') -> 'BonusStats':
        self.speed += other.speed
        self.time += other.time

        self.oak_per_break += other.oak_per_break
        self.cobblestone_per_break += other.cobblestone_per_break
        self.iron_per_break += other.iron_per_break
        
        self.all_collector_speed += other.all_collector_speed
        self.mine_collector_speed += other.mine_collector_speed
        self.wood_collector_speed += other.wood_collector_speed
        self.desert_collector_speed += other.desert_collector_speed
        self.snowy_collector_speed += other.snowy_collector_speed
        self.magical_collector_speed += other.magical_collector_speed
        self.fishing_collector_speed += other.fishing_collector_speed
        self.toxic_collector_speed += other.toxic_collector_speed
        self.slime_factory_processing_speed += other.slime_factory_processing_speed
        self.gem_excavation_speed += other.gem_excavation_speed
        self.volcanic_eruption_speed += other.volcanic_eruption_speed

        self.farm_size += other.farm_size
        self.food_effectiveness += other.food_effectiveness
        self.food_duration += other.food_duration

        self.stars *= other.stars
        self.ruby_generation_speed *= other.ruby_generation_speed
        self.companion_xp *= other.companion_xp

        self.misc = ('\n'.join((self.misc[0], other.misc[0])), False)

        return self

    def __repr__(self):
        cls_name = self.__class__.__name__
        parts = []
        for f in fields(self):
            value = getattr(self, f.name)

            if f.default is not MISSING:
                default = f.default
            elif f.default_factory is not MISSING:
                default = f.default_factory()
            else:
                default = MISSING

            if default is MISSING or value != default:
                parts.append(f'{f.name}={value!r}')

        return f'{cls_name}({', '.join(parts)})'