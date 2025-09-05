from dataclasses import dataclass, field

from stats import AddStats, MultiStats, BonusStats

@dataclass
class Artifact:
    name: str = ''

    flat: AddStats = field(default_factory=AddStats)
    multi: MultiStats = field(default_factory=MultiStats)

    pet_multi: MultiStats = field(default_factory=MultiStats)

    tier: int = None
    wave: int = None

@dataclass
class Specialization:
    name: str = ''

    flat: AddStats = field(default_factory=AddStats)
    multi: MultiStats = field(default_factory=MultiStats)

    pet_multi: MultiStats = field(default_factory=MultiStats)

    enemy_multi: MultiStats = field(default_factory=MultiStats)

    bonus: BonusStats = field(default_factory=BonusStats)

    level: int = 0

    def scale(self):
        self.flat *= self.level
        self.multi *= self.level

        self.pet_multi *= self.level

        self.enemy_multi *= self.level

        self.bonus *= self.level

@dataclass
class Companion:
    name: str = ''

    flat: AddStats = field(default_factory=AddStats)
    multi: MultiStats = field(default_factory=MultiStats)

    pet_multi: MultiStats = field(default_factory=MultiStats)

    bonus: BonusStats = field(default_factory=BonusStats)

    perm_flat: AddStats = field(default_factory=AddStats)
    perm_multi: MultiStats = field(default_factory=MultiStats)

    perm_pet_multi: MultiStats = field(default_factory=MultiStats)

    perm_enemy_multi: MultiStats = field(default_factory=MultiStats)

    perm_bonus: BonusStats = field(default_factory=BonusStats)

    level: int = 0

    def scale(self):
        self.flat *= self.level
        self.multi *= self.level

        self.pet_multi *= self.level

        self.bonus *= self.level

        self.perm_flat *= self.level
        self.perm_multi *= self.level

        self.perm_pet_multi *= self.level

        self.perm_enemy_multi *= self.level

        self.perm_bonus *= self.level

@dataclass
class Scroll:
    name: str = ''

    flat: AddStats = field(default_factory=AddStats)
    multi: MultiStats = field(default_factory=MultiStats)

    pet_multi: MultiStats = field(default_factory=MultiStats)

    enemy_multi: MultiStats = field(default_factory=MultiStats)

    bonus: BonusStats = field(default_factory=BonusStats)

    tier: int = None
    rarity: int = None

@dataclass
class Item:
    name: str = ''

    flat: AddStats = field(default_factory=AddStats)
    add: AddStats = field(default_factory=AddStats)

@dataclass
class Food:
    name: str = ''

    flat: AddStats = field(default_factory=AddStats)
    add: AddStats = field(default_factory=AddStats)

    pet_add: AddStats = field(default_factory=AddStats)

    duration: int = None

@dataclass
class Pet:
    name: str = ''

    base: AddStats = field(default_factory=AddStats)

    buff_flat: AddStats = field(default_factory=AddStats)
    buff_add: AddStats = field(default_factory=AddStats)

    buff_pet_flat: AddStats = field(default_factory=AddStats)
    buff_pet_add: AddStats = field(default_factory=AddStats)

@dataclass
class Wave:
    name: str = ''

    base: AddStats = field(default_factory=AddStats)

    max: int = 0