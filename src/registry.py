from stats import AddStats, MultiStats, BonusStats
from definitions import Artifact, Specialization, Companion, Scroll, Item, Pet, Food, Wave

class Artifacts:
    OAK_SPEAR = Artifact(
        'Oak Spear',
        flat=AddStats(5, 40, 2),
        tier=1,
        wave=3
    )
    GIANT_ROCK = Artifact(
        'Giant Rock',
        flat=AddStats(1, 125, 1),
        multi=MultiStats(hp=1.2),
        tier=1,
        wave=4
    )
    TORCH = Artifact(
        'Torch',
        flat=AddStats(4, 20, 4),
        multi=MultiStats(dmg=1.3),
        tier=1,
        wave=6
    )
    HAY_BALE = Artifact(
        'Hay Bale',
        flat=AddStats(hp=80, hpr=8),
        pet_multi=MultiStats(hp=1.5),
        tier=1,
        wave=9
    )
    BONE = Artifact(
        'Bone',
        flat=AddStats(9, 35, 1),
        pet_multi=MultiStats(1.8),
        tier=1,
        wave=12
    )
    GOLDEN_CARROT = Artifact(
        'Golden Carrot',
        flat=AddStats(1, 20, 1),
        multi=MultiStats(1.5, 1.5, 1.5),
        tier=1,
        wave=14
    )
    SPRUCE_SAPLING = Artifact(
        'Spruce Sapling',
        flat=AddStats(5, 90, 6),
        multi=MultiStats(hpr=1.7),
        tier=1,
        wave=18
    )
    JACK_O_LANTERN = Artifact(
        "Jack o'Lantern",
        flat=AddStats(2, 45, 5),
        pet_multi=MultiStats(2, 1.5),
        tier=1,
        wave=20
    )
    DIAMOND_SCYTHE = Artifact(
        'Diamond Scythe',
        flat=AddStats(12, 10, 1),
        multi=MultiStats(2),
        tier=1,
        wave=23
    )
    REDSTONE = Artifact(
        'Redstone',
        flat=AddStats(6, 75, 7),
        multi=MultiStats(hpr=2),
        pet_multi=MultiStats(hpr=2),
        tier=1,
        wave=27
    )
    EMERALD_BLOCK = Artifact(
        'Emerald Block',
        flat=AddStats(12, 250, 15),
        tier=1,
        wave=30
    )

    PACKED_ICE = Artifact(
        'Packed Ice',
        flat=AddStats(10, 150, 0),
        multi=MultiStats(hp=2.5, hpr=0.8),
        tier=2,
        wave=21
    )
    SANDSTONE_THRONE = Artifact(
        'Sandstone Throne',
        flat=AddStats(1, 40, 5),
        multi=MultiStats(hpr=1.5),
        pet_multi=MultiStats(3),
        tier=2,
        wave=24
    )
    SEA_LANTERN = Artifact(
        'Sea Lantern',
        flat=AddStats(2, 180, 12),
        multi=MultiStats(hp=1.5),
        pet_multi=MultiStats(hp=2, hpr=1.7),
        tier=2,
        wave=27
    )
    CHERRY_BLOSSOM = Artifact(
        'Cherry Blossom',
        flat=AddStats(1, 1, 1),
        multi=MultiStats(2, 1.8, 2.4),
        tier=2,
        wave=31
    )
    SALMON_STEW = Artifact(
        'Salmon Stew',
        flat=AddStats(8, 20, 4),
        pet_multi=MultiStats(hp=5),
        tier=2,
        wave=35
    )
    MUSIC_DISC = Artifact(
        'Music Disc',
        flat=AddStats(25, 115, 20),
        multi=MultiStats(1.5),
        pet_multi=MultiStats(1.5),
        tier=2,
        wave=38
    )
    RED_MUSHROOM = Artifact(
        'Red Mushroom',
        flat=AddStats(3, 70, 1),
        multi=MultiStats(hp=0.3),
        pet_multi=MultiStats(dmg=3.5, hpr=3),
        tier=2,
        wave=42
    )
    LONGBOW = Artifact(
        'Longbow',
        flat=AddStats(120, 5, 0),
        multi=MultiStats(0.5),
        pet_multi=MultiStats(hp=3.5, hpr=1.5),
        tier=2,
        wave=46
    )
    THORNBUSH = Artifact(
        'Thornbush',
        flat=AddStats(2, 30, 3),
        multi=MultiStats(dmg=5, hpr=0.6),
        pet_multi=MultiStats(4.5),
        tier=2,
        wave=50
    )

    STICKY_PISTON = Artifact(
        'Sticky Piston',
        flat=AddStats(3, 50, 15),
        multi=MultiStats(3.5),
        pet_multi=MultiStats(1.5, 4),
        tier=3,
        wave=35
    )
    BRICK = Artifact(
        'Brick',
        flat=AddStats(12, 250, 0),
        pet_multi=MultiStats(6.5),
        tier=3,
        wave=38
    )
    GLOWSTONE = Artifact(
        'Glowstone',
        flat=AddStats(0, 30, 3),
        multi=MultiStats(0.8, 8, 4),
        tier=3,
        wave=42
    )
    WATER_BUCKET = Artifact(
        'Water Bucket',
        flat=AddStats(6, 300, 10),
        multi=MultiStats(dmg=3, hpr=3),
        pet_multi=MultiStats(dmg=3, hpr=3),
        tier=3,
        wave=46
    )
    SOUL_SAND = Artifact(
        'Soul Sand',
        flat=AddStats(14, 500, 28),
        multi=MultiStats(2),
        tier=3,
        wave=51
    )
    GHAST_TEAR = Artifact(
        'Ghast Tear',
        flat=AddStats(0, 25, 0),
        pet_multi=MultiStats(2.5, 4, 4),
        tier=3,
        wave=55
    )
    FIERY_ASHES = Artifact(
        'Fiery Ashes',
        flat=AddStats(5, 75, 0),
        multi=MultiStats(dmg=10, hpr=0.4),
        pet_multi=MultiStats(hpr=0.4),
        tier=3,
        wave=59
    )
    INK_SAC = Artifact(
        'Ink Sac',
        flat=AddStats(10, 100, 10),
        multi=MultiStats(2, 3, 2.5),
        pet_multi=MultiStats(2, 3, 2.5),
        tier=3,
        wave=63
    )
    PURPLE_DYE = Artifact(
        'Purple Dye',
        flat=AddStats(0, 750, 2),
        multi=MultiStats(hpr=5),
        pet_multi=MultiStats(2, 6),
        tier=3,
        wave=67
    )
    EYE_OF_ENDER = Artifact(
        'Eye of Ender',
        flat=AddStats(30, 1, 40),
        multi=MultiStats(hp=10),
        pet_multi=MultiStats(hp=4, hpr=5),
        tier=3,
        wave=71
    )
    ENCHANTMENT_TABLE = Artifact(
        'Enchantment Table',
        flat=AddStats(1, 20, 1),
        multi=MultiStats(5, 3, 2),
        pet_multi=MultiStats(7, 2),
        tier=3,
        wave=75
    )

class Specializations:
    WARRIOR = Specialization(
        'Warrior',
        multi=MultiStats(
            dmg=1.3
        )
    )
    ATHLETE = Specialization(
        'Athlete',
        flat=AddStats(
            dmg=1,
            hp=25,
            hpr=2,
        ),
        bonus=BonusStats(
            speed=1
        )
    )
    COLLECTOR = Specialization(
        'Collector',
        bonus=BonusStats(
            all_collector_speed=0.15,
            stars=1.1,
            misc=('Start with _ Axe (Eff 3)', True)
        ),
    )
    FARMER = Specialization(
        'Farmer',
        multi=MultiStats(
            hp=1.1
        ),
        pet_multi=MultiStats(
            hp=1.1
        ),
        bonus=BonusStats(
            farm_size=0.2,
            food_effectiveness=0.25
        )
    )
    TRAINER = Specialization(
        'Trainer',
        multi=MultiStats(
            dmg=(1/1.1)
        ),
        pet_multi=MultiStats(
            dmg=1.25,
            hpr=1.2
        )
    )
    WITCH = Specialization(
        'Witch',
        enemy_multi=MultiStats(
            dmg=(1/1.2),
            hp=(1/1.15)
        ),
        bonus=BonusStats(
            stars=(1/1.1)
        )
    )
    PURIST = Specialization(
        'Purist',
        bonus=BonusStats(
            time=2,
            ruby_generation_speed=1.5,
            companion_xp=1.4
        )
    )

    def __init__(self, **levels):
        for name, level in levels.items():
            if not hasattr(self, name):
                raise ValueError(f"Specialization '{name}' does not exist")

            spec = getattr(self, name)
            spec.level = level
            spec.scale()

class Companions:
    LADYBUG = Companion(
        'Ladybug',
        flat=AddStats(
            hp=5
        ),
        multi=MultiStats(
            hp=1.1
        ),
        perm_multi=MultiStats(
            hp=1.05
        )
    )
    OCELOT = Companion(
        'Ocelot',
        flat=AddStats(
            hpr=2
        ),
        perm_multi=MultiStats(
            hpr=1.05
        )
    )
    ANT = Companion(
        'Ant',
        multi=MultiStats(
            dmg=1.12
        ),
        pet_multi=MultiStats(
            dmg=(1/1.05)
        ),
        perm_multi=MultiStats(
            dmg=1.05
        )
    )
    SILVERFISH = Companion(
        'Silverfish',
        bonus=BonusStats(
            mine_collector_speed=0.05,
            wood_collector_speed=0.05,
            ruby_generation_speed=1.1,
        ),
        perm_bonus=BonusStats(
            stars=1.06
        )
    )
    BEE = Companion(
        'Bee',
        perm_pet_multi=MultiStats(
            dmg=1.03,
            hp=1.03,
            hpr=1.03
        ),
        bonus=BonusStats(
            misc=('Start with Bee Pet (best perk)', False)
        )
    )
    MONKEY = Companion(
        'Monkey',
        pet_multi=MultiStats(
            dmg=1.05
        ),
        perm_multi=MultiStats(
            hp=1.04
        ),
        perm_pet_multi=MultiStats(
            hp=1.04
        ),
        bonus=BonusStats(
            farm_size=0.08
        )
    )
    PARROT = Companion(
        'Parrot',
        multi=MultiStats(
            hpr=1.03
        ),
        bonus=BonusStats(
            speed=0.5
        ),
        perm_bonus=BonusStats(
            time=1
        )
    )
    CHICKEN = Companion(
        'Chicken',
        bonus=BonusStats(
            food_effectiveness=0.15
        ),
        perm_bonus=BonusStats(
            food_duration=0.05
        )
    )
    SHEEP = Companion(
        'Sheep',
        pet_multi=MultiStats(
            hp=1.05
        ),
        perm_flat=AddStats(
            hp=6
        ),
        bonus=BonusStats(
            desert_collector_speed=0.05,
            snowy_collector_speed=0.05,
            magical_collector_speed=0.05
        )
    )
    CRAB = Companion(
        'Crab',
        multi=MultiStats(
            hp=(1/1.03)
        ),
        pet_multi=MultiStats(
            hpr=1.06
        ),
        perm_enemy_multi=MultiStats(
            hp=(1/1.03)
        ),
        bonus=BonusStats(
            fishing_collector_speed=0.1
        )
    )
    FROG = Companion(
        perm_multi=MultiStats(
            dmg=1.04
        ),
        perm_pet_multi=MultiStats(
            dmg=1.04
        ),
        bonus=BonusStats(
            toxic_collector_speed=0.05,
            slime_factory_processing_speed=0.05,
            gem_excavation_speed=0.05,
            volcanic_eruption_speed=0.05,
            stars=1.05
        )
    )
    SNAIL = Companion(
        multi=MultiStats(
            dmg=1.05,
        ),
        bonus=BonusStats(
            stars=1.1
        ),
        perm_bonus=BonusStats(
            ruby_generation_speed=1.05
        )
    )
    BAT = Companion(
        perm_multi=MultiStats(
            hpr=1.04
        ),
        perm_pet_multi=MultiStats(
            hpr=1.04
        ),
        bonus=BonusStats(
            time=2
        )
    )
    GOLDEN_MONKEY = Companion(
        bonus=BonusStats(
            misc=("Start with Divine Helmet :O", False)
        ),
        perm_bonus=BonusStats(
            companion_xp=1.05
        )
    )
    POLAR_BEAR = Companion(
        bonus=BonusStats(
            ruby_generation_speed=1.3
        ),
        perm_bonus=BonusStats(
            stars=1.07
        )
    )

    def __init__(self, **levels):
        for name, level in levels.items():
            if not hasattr(self, name):
                raise ValueError(f"Companion '{name}' does not exist")

            comp = getattr(self, name)
            comp.level = level
            comp.scale()

class Scrolls:
    T1_HEALTH_BOOST = Scroll(
        'T1 Health Boost',
        multi=MultiStats(
            hp=1.2
        ),
        tier=1,
        rarity=1
    )
    T1_HEALTH_REGEN_BOOST = Scroll(
        'T1 Health Regen Boost',
        multi=MultiStats(
            hpr=1.2
        ),
        tier=1,
        rarity=1
    )
    T1_DAMAGE_BOOST = Scroll(
        'T1 Damage Boost',
        multi=MultiStats(
            dmg=1.2
        ),
        tier=1,
        rarity=1
    )
    T1_LARGER_FARM = Scroll(
        'T1 Larger Farm',
        bonus=BonusStats(
            farm_size=0.35
        ),
        tier=1,
        rarity=1
    )
    T1_FASTER_MINE = Scroll(
        'T1 Faster Mine',
        bonus=BonusStats(
            mine_collector_speed=0.35
        ),
        tier=1,
        rarity=1
    )
    T1_FASTER_WOOD_COLLECTORS = Scroll(
        'T1 Faster Wood Collectors',
        bonus=BonusStats(
            wood_collector_speed=0.35
        ),
        tier=1,
        rarity=1
    )
    T1_PET_HEALTH_BOOST = Scroll(
        'T1 Pet Health Boost',
        pet_multi=MultiStats(
            hp=1.3
        ),
        tier=1,
        rarity=2
    )
    T1_PET_HEALTH_REGEN_BOOST = Scroll(
        'T1 Pet Health Regen Boost',
        pet_multi=MultiStats(
            hpr=1.3
        ),
        tier=1,
        rarity=2
    )
    T1_PET_DAMAGE_BOOST = Scroll(
        'T1 Pet Damage Boost',
        pet_multi=MultiStats(
            dmg=1.3
        ),
        tier=1,
        rarity=2
    )
    T1_STAR_BOOST = Scroll(
        'T1 Star Boost',
        bonus=BonusStats(
            stars=1.3
        ),
        tier=1,
        rarity=2
    )
    T1_HEALTHY_HABITS = Scroll(
        'T1 Healthy Habits',
        flat=AddStats(
            hp=20,
            hpr=3
        ),
        tier=1,
        rarity=2
    )
    T1_STRENGTH_TRAINING = Scroll(
        'T1 Strength Training',
        flat=AddStats(
            dmg=4
        ),
        tier=1,
        rarity=3
    )
    T1_BAKERS_TOUCH = Scroll(
        "T1 Baker's Touch",
        bonus=BonusStats(
            food_duration=1
        ),
        tier=1,
        rarity=3
    )
    T1_SPRINTER = Scroll(
        'T1 Sprinter',
        bonus=BonusStats(
            speed=3
        ),
        tier=1,
        rarity=3
    )
    T1_REINFORCED_FISTS = Scroll(
        'T1 Reinforced Fists',
        bonus=BonusStats(
            oak_per_break=15,
            cobblestone_per_break=30,
            iron_per_break=30
        ),
        tier=1,
        rarity=3
    )
    T1_PLAYER_BOOST = Scroll(
        'T1 Player Boost',
        multi=MultiStats(
            dmg=1.1,
            hp=1.1,
            hpr=1.1
        ),
        tier=1,
        rarity=4
    )
    T1_DETERMINED_GRINDER = Scroll(
        'T1 Determined Grinder',
        bonus=BonusStats(
            mine_collector_speed=-0.2,
            wood_collector_speed=-0.2,
            stars=1.6
        ),
        tier=1,
        rarity=4
    )
    T1_COUNTERMEASURES = Scroll(
        'T1 Countermeasures',
        bonus=BonusStats(
            time=8
        )
    )
    T2_HEALTH_BOOST = Scroll(
        'T2 Health Boost',
        multi=MultiStats(
            hp=1.15
        ),
        pet_multi=MultiStats(
            hp=1.15
        ),
        tier=2,
        rarity=1
    )
    T2_HEALTH_REGEN_BOOST = Scroll(
        'T2 Health Regen Boost',
        multi=MultiStats(
            hpr=1.15
        ),
        pet_multi=MultiStats(
            hpr=1.15
        ),
        tier=2,
        rarity=1
    )
    T2_DAMAGE_BOOST = Scroll(
        'T2 Damage Boost',
        multi=MultiStats(
            dmg=1.15
        ),
        pet_multi=MultiStats(
            dmg=1.15
        ),
        tier=2,
        rarity=1
    )
    T2_STAR_BOOST = Scroll(
        'T2 Star Boost',
        bonus=BonusStats(
            stars=1.35
        ),
        tier=2,
        rarity=1
    )
    T2_FASTER_COLLECTORS = Scroll(
        'T2 Faster Collectors',
        bonus=BonusStats(
            mine_collector_speed=0.25,
            wood_collector_speed=0.25
        ),
        tier=2,
        rarity=1
    )
    T2_FASTER_DESERT_COLLECTORS = Scroll(
        'T2 Faster Desert Collectors',
        bonus=BonusStats(
            desert_collector_speed=0.5
        ),
        tier=2,
        rarity=2
    )
    T2_FASTER_SNOWY_COLLECTORS = Scroll(
        'T2 Faster Snowy Collectors',
        bonus=BonusStats(
            snowy_collector_speed=0.5
        ),
        tier=2,
        rarity=2
    )
    T2_FASTER_MAGICAL_COLLECTORS = Scroll(
        'T2 Faster Magical Collectors',
        bonus=BonusStats(
            magical_collector_speed=0.5
        ),
        tier=2,
        rarity=2
    )
    T2_MECHANICAL_IMPLANTS = Scroll(
        'T2 Mechanical Implants',
        flat=AddStats(
            dmg=3,
            hpr=3
        ),
        tier=2,
        rarity=2
    )
    T2_ENHANCED_COOKING = Scroll(
        'T2 Enhanced Cooking',
        bonus=BonusStats(
            food_effectiveness=0.5
        ),
        tier=2,
        rarity=2
    )
    T2_PET_BOOST = Scroll(
        'T2 Pet Boost',
        pet_multi=MultiStats(
            dmg=1.15,
            hp=1.15,
            hpr=1.15
        ),
        tier=2,
        rarity=3
    )
    T2_SOLO_WARRIOR = Scroll(
        'T2 Solo Warrior',
        multi=MultiStats(
            dmg=1.35
        ),
        pet_multi=MultiStats(
            dmg=0.75
        ),
        tier=2,
        rarity=3
    )
    T2_NOCTURNAL = Scroll(
        'T2 Nocturnal',
        multi=MultiStats(
            hp=0.85,
        ),
        bonus=BonusStats(
            stars=1.5
        ),
        tier=2,
        rarity=3
    )
    T2_FRUGAL_FARMER = Scroll(
        'T2 Frugal Farmer',
        multi=MultiStats(
            hpr=0.9
        ),
        bonus=BonusStats(
            farm_size=0.6
        )
    )
    T2_DIAMOND_RUSH = Scroll(
        'T2 Diamond Rush',
        bonus=BonusStats(
            misc=("Start with Tier I Diamond Mine", False)
        ),
        tier=2,
        rarity=3
    )
    T2_INSTANT_RECOVERY = Scroll(
        'T2 Instant Recovery',
        multi=MultiStats(
            hp=0.9,
            hpr=1.35
        ),
        tier=2,
        rarity=4
    )
    T2_BLOOD_INFUSION = Scroll(
        'T2 Blood Infusion',
        multi=MultiStats(
            hpr=0.7
        ),
        pet_multi=MultiStats(
            hp=1.4,
            hpr=1.25
        ),
        tier=2,
        rarity=4
    )
    T2_POISONOUS_GAS = Scroll(
        'T2 Poisonous Gas',
        enemy_multi=MultiStats(
            hp=0.7
        ),
        bonus=BonusStats(
            stars=0.5
        ),
        tier=2,
        rarity=4
    )
    T2_TIME_WARP = Scroll(
        'T2 Time Warp',
        bonus=BonusStats(
            speed=4,
            time=3
        ),
        tier=2,
        rarity=4
    )
    T3_PLAYER_BOOST = Scroll(
        'T3 Player Boost',
        multi=MultiStats(
            dmg=1.15,
            hp=1.2
        ),
        tier=3,
        rarity=1
    )
    T3_PET_BOOST = Scroll(
        'T3 Pet Boost',
        pet_multi=MultiStats(
            dmg=1.15,
            hp=1.2
        ),
        tier=3,
        rarity=1
    )
    T3_FASTER_COLLECTORS = Scroll(
        'T3 Faster Collectors',
        bonus=BonusStats(
            desert_collector_speed=0.25,
            snowy_collector_speed=0.25,
            magical_collector_speed=0.25
        ),
        tier=3,
        rarity=1
    )
    T3_RUBY_BOOST = Scroll(
        'T3 Ruby Boost',
        bonus=BonusStats(
            ruby_generation_speed=1.65
        ),
        tier=3,
        rarity=1
    )
    T3_WEAKEN_ENEMIES = Scroll(
        'T3 Weaken Enemies',
        enemy_multi=MultiStats(
            hp=0.8
        ),
        tier=3,
        rarity=1
    )
    T3_FEROCITY = Scroll(
        'T3 Ferocity',
        pet_multi=MultiStats(
            dmg=1.5,
            hp=0.9
        ),
        tier=3,
        rarity=2
    )
    T3_VITAMINS = Scroll(
        'T3 Vitamins',
        flat=AddStats(
            hpr=8
        ),
        multi=MultiStats(
            hpr=1.1
        ),
        tier=3,
        rarity=2
    )
    T3_CLEAR_SKIES = Scroll(
        'T3 Clear Skies',
        bonus=BonusStats(
            speed=2,
            stars=1.25
        ),
        tier=3,
        rarity=2
    )
    T3_HIGH_TIDE = Scroll(
        'T3 High Tide',
        multi=MultiStats(
            hp=0.95
        ),
        pet_multi=MultiStats(
            hp=0.95
        ),
        bonus=BonusStats(
            fishing_collector_speed=0.6
        ),
        tier=3,
        rarity=2
    )
    T3_RADIOACTIVE_FALLOUT = Scroll(
        'T3 Radioactive Fallout',
        multi=MultiStats(
            hpr=0.9
        ),
        pet_multi=MultiStats(
            hpr=0.9
        ),
        bonus=BonusStats(
            toxic_collector_speed=0.4,
            slime_factory_processing_speed=0.8
        ),
        tier=3,
        rarity=2
    )
    T3_TEAMWORK = Scroll(
        'T3 Teamwork',
        multi=MultiStats(
            dmg=1.25
        ),
        pet_multi=MultiStats(
            hp=1.4
        ),
        tier=3,
        rarity=3
    )
    T3_NIGHT_VISION_GOGGLES = Scroll(
        'T3 Night-vision Goggles',
        bonus=BonusStats(
            gem_excavation_speed=0.4,
            stars=1.15
        ),
        tier=3,
        rarity=3
    )
    T3_FIREPROOF = Scroll(
        'T3 Fireproof',
        multi=MultiStats(
            dmg=1.15
        ),
        pet_multi=MultiStats(
            dmg=1.1
        ),
        bonus=BonusStats(
            volcanic_eruption_speed=1
        ),
        tier=3,
        rarity=3
    )
    T3_PRESERVATIVES = Scroll(
        'T3 Preservatives',
        bonus=BonusStats(
            food_effectiveness=-0.2,
            food_duration=5,
        ),
        tier=3,
        rarity=3
    )
    T3_LIGHTSPEED = Scroll(
        'T3 Lightspeed',
        bonus=BonusStats(
            speed=8,
            time=-2
        ),
        tier=3,
        rarity=3
    )
    T3_RUBY_CRAZED = Scroll(
        'T3 Ruby-crazed',
        multi=MultiStats(
            dmg=1.2,
            hpr=0.85,
        ),
        bonus=BonusStats(
            ruby_generation_speed=1.8
        ),
        tier=3,
        rarity=3
    )
    T3_TYRANNY = Scroll(
        'T3 Tyranny',
        multi=MultiStats(
            dmg=1.55
        ),
        pet_multi=MultiStats(
            hp=0.5,
            hpr=1.5
        ),
        tier=3,
        rarity=4
    )
    T3_PROVISIONS = Scroll(
        'T3 Provisions',
        bonus=BonusStats(
            misc=("Start with Emerald Pickaxe (Eff III)", False)
        ),
        tier=3,
        rarity=4
    )
    T3_ASTRONOMY = Scroll(
        'T3 Astronomy',
        bonus=BonusStats(
            stars=1.8,
            ruby_generation_speed=0.5
        ),
        tier=3,
        rarity=4
    )
    T3_TELEPATHY = Scroll(
        'T3 Telepathy',
        multi=MultiStats(
            hp=0.7
        ),
        bonus=BonusStats(
            time=13
        ),
        tier=3,
        rarity=4
    )
    T4_HEALTH_BOOST = Scroll(
        'T4 Health Boost',
        flat=AddStats(
            hp=30
        ),
        multi=MultiStats(
            hp=1.3
        ),
        tier=4,
        rarity=1
    )
    T4_DAMAGE_BOOST = Scroll(
        'T4 Damage Boost',
        flat=AddStats(
            dmg=2
        ),
        multi=MultiStats(
            dmg=1.3
        ),
        tier=4,
        rarity=1
    )
    T4_PET_BOOST = Scroll(
        'T4 Pet Boost',
        pet_multi=MultiStats(
            dmg=1.25,
            hpr=1.3
        ),
        tier=4,
        rarity=1
    )
    T4_FASTER_PRODUCTION = Scroll(
        'T4 Faster Production',
        bonus=BonusStats(
            slime_factory_processing_speed=0.5,
            gem_excavation_speed=0.25,
            volcanic_eruption_speed=0.75
        ),
        tier=4,
        rarity=1
    )
    T4_LONGER_WAVES = Scroll(
        'T4 Longer Waves',
        bonus=BonusStats(
            time=10
        ),
        tier=4,
        rarity=1
    )
    T4_SACRIFICES = Scroll(
        'T4 Sacrifices',
        flat=AddStats(
            hp=-30,
            hpr=-4
        ),
        multi=MultiStats(
            dmg=1.65
        ),
        tier=4,
        rarity=2
    )
    T4_PACIFIST = Scroll(
        'T4 Pacifist',
        multi=MultiStats(
            dmg=0.5
        ),
        pet_multi=MultiStats(
            dmg=0.85,
            hp=1.8
        ),
        tier=4,
        rarity=2
    )
    T4_HANDS_OF_GOLD = Scroll(
        'T4 Hands of Gold',
        bonus=BonusStats(
            stars=1.35,
            ruby_generation_speed=1.4
        ),
        tier=4,
        rarity=2
    )
    T4_IRRIGATION = Scroll(
        'T4 Irrigation',
        bonus=BonusStats(
            farm_size=0.3,
            food_effectiveness=0.4
        ),
        tier=4,
        rarity=2
    )
    T4_ELEMENT_OF_SURPRISE = Scroll(
        'T4 Element of Surprise',
        enemy_multi=MultiStats(
            hp=0.6
        ),
        bonus=BonusStats(
            time=-5
        ),
        tier=4,
        rarity=2
    )
    T4_COMPANION_XP_BOOST = Scroll(
        'T4 Companion XP Boost',
        bonus=BonusStats(
            companion_xp=1.75
        ),
        tier=4,
        rarity=2
    )
    T4_LONE_WOLF = Scroll(
        'T4 Lone Wolf',
        flat=AddStats(
            dmg=12,
            hp=80
        ),
        pet_multi=MultiStats(
            dmg=0
        ),
        tier=4,
        rarity=3
    )
    T4_OUTSOURCING = Scroll(
        'T4 Outsourcing',
        multi=MultiStats(
            dmg=0.9
        ),
        bonus=BonusStats(
            mine_collector_speed=0.5,
            wood_collector_speed=0.4
        ),
        tier=4,
        rarity=3
    )
    T4_ASSASSIN = Scroll(
        'T4 Assassin',
        multi=MultiStats(
            dmg=1.2
        ),
        bonus=BonusStats(
            speed=3
        ),
        tier=4,
        rarity=3
    )
    T4_GREED = Scroll(
        'T4 Greed',
        enemy_multi=MultiStats(
            hp=1.1
        ),
        bonus=BonusStats(
            stars=1.7
        ),
        tier=4,
        rarity=3
    )
    T4_HEART_BOUND = Scroll(
        'T4 Heart-bound',
        multi=MultiStats(
            hp=1.4,
            hpr=1.3
        ),
        pet_multi=MultiStats(
            hp=1.4,
            hpr=1.3
        ),
        tier=4,
        rarity=4
    )
    T4_VEGETARIAN = Scroll(
        'T4 Vegetarian',
        multi=MultiStats(
            dmg=0.8,
            hpr=1.55
        ),
        tier=4,
        rarity=4
    )
    T4_RALLY = Scroll(
        'T4 Rally',
        multi=MultiStats(
            dmg=1.3,
            hp=0.8
        ),
        pet_multi=MultiStats(
            dmg=1.5
        ),
        tier=4,
        rarity=4
    )
    T4_FRIENDS_FOR_LIFE = Scroll(
        'T4 Friends for Life',
        bonus=BonusStats(
            stars=0.7,
            companion_xp=3
        ),
        tier=4,
        rarity=4
    )
    T4_SUPERNOVA = Scroll(
        'T4 Supernova',
        multi=MultiStats(
            dmg=1.2
        ),
        pet_multi=MultiStats(
            dmg=1.2
        ),
        bonus=BonusStats(
            time=-15,
            stars=2.5
        ),
        tier=4,
        rarity=4
    )

class Weapons:
    OAK_SWORD = Item(
        'Oak Sword',
        flat=AddStats(
            dmg=3
        )
    )
    STONE_SWORD = Item(
        'Stone Sword',
        flat=AddStats(
            dmg=5
        )
    )
    PUMPKIN_BLADE = Item(
        'Pumpkin Blade',
        flat=AddStats(
            dmg=18
        ),
        add=AddStats(
            hp=-0.3
        )
    )
    SHARPENED_STICK = Item(
        'Sharpened Stick',
        flat=AddStats(
            dmg=8
        )
    )
    IRON_SWORD = Item(
        'Iron Sword',
        flat=AddStats(
            dmg=7
        )
    )
    DIAMOND_SWORD = Item(
        'Diamond Sword',
        flat=AddStats(
            dmg=10
        )
    )
    SHINING_SWORD = Item(
        'Shining Sword',
        flat=AddStats(
            dmg=12
        ),
        add=AddStats(
            hp=0.2
        )
    )
    BOULDER = Item(
        'Boulder',
        flat=AddStats(
            dmg=20
        ),
        add=AddStats(
            hpr=-0.5
        )
    )
    DIAMOND_SPEAR = Item(
        'Diamond Spear',
        flat=AddStats(
            dmg=23
        )
    )
    POISONED_BLADE = Item(
        'Poisoned Blade',
        flat=AddStats(
            dmg=33
        ),
        add=AddStats(
            hp=-0.3,
            hpr=-0.4
        )
    )
    TOOTHED_DAGGER = Item(
        'Toothed Dagger',
        flat=AddStats(
            dmg=58
        ),
        add=AddStats(
            hp=-0.7
        )
    )
    CACTUS_BLADE = Item(
        'Cactus Blade',
        flat=AddStats(
            dmg=24
        ),
        add=AddStats(
            hpr=-1
        )
    )
    ANCIENT_SWORD = Item(
        'Ancient Sword',
        flat=AddStats(
            dmg=17
        ),
        add=AddStats(
            hp=0.75
        )
    )
    ICE_SHARD = Item(
        'Ice Shard',
        flat=AddStats(
            dmg=25
        ),
        add=AddStats(
            hp=-0.15
        )
    )
    STEEL_SWORD = Item(
        'Steel Sword',
        flat=AddStats(
            dmg=15
        ),
        add=AddStats(
            hp=0.5
        )
    )
    AMETHYST_SWORD = Item(
        'Amethyst Sword',
        flat=AddStats(
            dmg=21
        ),
        add=AddStats(
            hpr=0.4
        )
    )
    FRUITFUL_BLADE = Item(
        'Fruitful Blade',
        flat=AddStats(
            dmg=20
        ),
        add=AddStats(
            hp=0.35,
            hpr=0.8
        )
    )
    ORANGE_BLADE = Item(
        'Orange Blade',
        flat=AddStats(
            dmg=38
        ),
        add=AddStats(
            hpr=-0.2
        )
    )
    SLIME_SLICER = Item(
        'Slime Slicer',
        flat=AddStats(
            dmg=46
        ),
        add=AddStats(
            hp=-0.4,
            hpr=0.5
        )
    )
    SHINING_SCEPTER = Item(
        'Shining Scepter',
        flat=AddStats(
            dmg=29
        ),
        add=AddStats(
            hp=0.65
        )
    )
    CURSED_RING = Item(
        'Cursed Ring',
        flat=AddStats(
            dmg=8
        ),
        add=AddStats(
            hp=0.5,
            hpr=2
        )
    )
    BURNING_EMBER = Item(
        'Burning Ember',
        flat=AddStats(
            dmg=40
        ),
        add=AddStats(
            hp=0.2,
            hpr=-0.3
        )
    )

class Helmets:
    OAK_HELMET = Item(
        'Oak Helmet',
        flat=AddStats(
            hp=15,
            hpr=1
        )
    )
    SUGAR_HELMET = Item(
        'Sugar Helmet',
        flat=AddStats(
            hp=35,
            hpr=-2
        ),
        add=AddStats(
            dmg=0.4
        )
    )
    SPRUCE_HELMET = Item(
        'Spruce Helmet',
        flat=AddStats(
            hp=100
        )
    )
    COAL_HELMET = Item(
        'Coal Helmet',
        flat=AddStats(
            hp=10,
            hpr=3
        )
    )
    GOLDEN_HELMET = Item(
        'Golden Helmet',
        flat=AddStats(
            hp=60,
            hpr=2
        )
    )
    SPARKLING_HELMET = Item(
        'Sparkling Helmet',
        flat=AddStats(
            hp=150,
            hpr=7
        )
    )
    ABYSSAL_MASK = Item(
        'Abyssal Mask',
        flat=AddStats(
            hp=-50,
            hpr=-10
        ),
        add=AddStats(
            dmg=1.2
        )
    )
    REDWOOD_HELMET = Item(
        'Redwood Helmet',
        flat=AddStats(
            hp=90
        ),
        add=AddStats(
            dmg=0.45
        )
    )
    CHERRY_HELMET = Item(
        'Cherry Helmet',
        flat=AddStats(
            hp=60,
            hpr=10
        )
    )
    FUNGAL_HELMET = Item(
        'Fungal Helmet',
        flat=AddStats(
            hp=65,
            hpr=18
        ),
        add=AddStats(
            dmg=0.35
        )
    )
    FLORAL_CROWN = Item(
        'Floral Crown',
        flat=AddStats(
            hp=375,
            hpr=20
        ),
        add=AddStats(
            dmg=-0.15
        )
    )
    GRANITE_HELMET = Item(
        'Granite Helmet',
        flat=AddStats(
            hp=335
        ),
        add=AddStats(
            dmg=0.15
        )
    )

class Chestplates:
    OAK_CHESTPLATE = Item(
        'Oak Chestplate',
        flat=AddStats(
            hp=15,
            hpr=1
        )
    )
    CARROT_CHESTPLATE = Item(
        'Carrot Chestplate',
        flat=AddStats(
            hp=50,
            hpr=6
        )
    )
    WOODEN_CHESTPLATE = Item(
        'Wooden Chestplate',
        flat=AddStats(
            hp=115
        ),
        add=AddStats(
            dmg=0.2
        )
    )
    IRON_CHESTPLATE = Item(
        'Iron Chestplate',
        flat=AddStats(
            hp=80
        )
    )
    ROCKY_CHESTPLATE = Item(
        'Rocky Chestplate',
        flat=AddStats(
            hp=250,
            hpr=-5
        )
    )
    STRIPED_CHESTPLATE = Item(
        'Striped Chestplate',
        flat=AddStats(
            hp=30,
            hpr=18
        ),
        add=AddStats(
            dmg=0.25
        )
    )
    RED_SAND_CHESTPLATE = Item(
        'Red Sand Chestplate',
        flat=AddStats(
            hp=80,
            hpr=4
        ),
        add=AddStats(
            dmg=0.2
        )
    )
    SNOW_CHESTPLATE = Item(
        'Snow Chestplate',
        flat=AddStats(
            hp=120,
            hpr=5
        ),
        add=AddStats(
            dmg=-0.1
        )
    )
    AMETHYST_CHESTPLATE = Item(
        'Amethyst Chestplate',
        flat=AddStats(
            hp=100,
            hpr=3
        ),
        add=AddStats(
            dmg=0.3
        )
    )
    BLUE_ICE_CHESTPLATE = Item(
        'Blue Ice Chestplate',
        flat=AddStats(
            hp=550,
            hpr=8
        ),
        add=AddStats(
            dmg=-0.25
        )
    )
    CHESTPLATE_OF_FEAR = Item(
        'Chestplate of Fear',
        flat=AddStats(
            hp=-150,
            hpr=30
        ),
        add=AddStats(
            dmg=0.65
        )
    )

class Leggings:
    OAK_LEGGINGS = Item(
        'Oak Leggings',
        flat=AddStats(
            hp=15,
            hpr=1
        )
    )
    COBBLESTONE_LEGGINGS = Item(
        'Cobblestone Leggings',
        flat=AddStats(
            hp=35,
            hpr=1
        )
    )
    PUMPKIN_PANTS = Item(
        'Pumpkin Pants',
        flat=AddStats(
            hp=120,
            hpr=7
        ),
        add=AddStats(
            dmg=-0.15
        )
    )
    BIRCH_LEGGINGS = Item(
        'Birch Leggings',
        flat=AddStats(
            hp=50,
            hpr=2
        )
    )
    EMERALD_LEGGINGS = Item(
        'Emerald Leggings',
        flat=AddStats(
            hp=25,
            hpr=8
        )
    )
    DIAMOND_LEGGINGS = Item(
        'Diamond Leggings',
        flat=AddStats(
            hp=200
        ),
        add=AddStats(
            dmg=0.25
        )
    )
    COD_TROUSERS = Item(
        'Cod Trousers',
        flat=AddStats(
            hp=45,
            hpr=10
        )
    )
    SAND_LEGGINGS = Item(
        'Sand Leggings',
        flat=AddStats(
            hp=130
        ),
        add=AddStats(
            dmg=0.15
        )
    )
    ICE_LEGGINGS = Item(
        'Ice Leggings',
        flat=AddStats(
            hp=90,
            hpr=12
        )
    )
    PURE_PURPLE_PANTS = Item(
        'Pure Purple Pants',
        flat=AddStats(
            hp=100,
            hpr=40
        )
    )
    SPARKLING_LEGGINGS = Item(
        'Sparkling Leggings',
        flat=AddStats(
            hp=100,
            hpr=12
        ),
        add=AddStats(
            dmg=0.35
        )
    )
    PLATED_DIORITE_LEGGINGS = Item(
        'Plated Diorite Leggings',
        flat=AddStats(
            hp=480,
            hpr=5
        ),
        add=AddStats(
            dmg=-0.1
        )
    )

class Boots:
    OAK_BOOTS = Item(
        'Oak Boots',
        flat=AddStats(
            hp=15,
            hpr=1
        )
    )
    COBBLESTONE_BOOTS = Item(
        'Cobblestone Boots',
        flat=AddStats(
            hp=35,
            hpr=1
        )
    )
    WHEAT_BOOTS = Item(
        'Wheat Boots',
        flat=AddStats(
            hp=20,
            hpr=3
        )
    )
    POPPY_BOOTS = Item(
        'Poppy boots',
        flat=AddStats(
            hpr=10
        ),
        add=AddStats(
            dmg=0.25
        )
    )
    DIAMOND_BOOTS = Item(
        'Diamond Boots',
        flat=AddStats(
            hp=70,
            hpr=4
        )
    )
    ROYAL_SHOES = Item(
        'Royal Shoes',
        flat=AddStats(
            hp=60,
            hpr=2
        ),
        add=AddStats(
            dmg=0.3
        )
    )
    SCALY_BOOTS = Item(
        'Scaly Boots',
        flat=AddStats(
            hp=125,
            hpr=-6
        ),
        add=AddStats(
            dmg=0.5
        )
    )
    SAND_BOOTS = Item(
        'Sand Boots',
        flat=AddStats(
            hp=100
        ),
        add=AddStats(
            dmg=0.15
        )
    )
    SNOWSHROOM_BOOTS = Item(
        'Snowshroom Boots',
        flat=AddStats(
            hp=320,
            hpr=10
        ),
        add=AddStats(
            dmg=-0.2
        )
    )
    SLIME_BOOTS = Item(
        'Slime Boots',
        flat=AddStats(
            hp=210,
            hpr=5
        ),
        add=AddStats(
            dmg=0.1
        )
    )
    BOOTS_OF_WRATH = Item(
        'Boots of Wrath',
        flat=AddStats(
            hp=320,
            hpr=-25
        ),
        add=AddStats(
            dmg=0.9
        )
    )
    IMMOVABLE_BOOTS = Item(
        'Immovable Boots',
        flat=AddStats(
            hp=950,
            hpr=-10
        ),
        add=AddStats(
            dmg=-0.25
        )
    )

class Pets:
    BEE = Pet(
        'Bee',
        base=AddStats(
            3, 2, 100
        ),
        buff_pet_add=AddStats(
            dmg=0.5
        )
    )
    OAK_PET = Pet(
        'Oak Pet',
        base=AddStats(
            2, 30, 2
        )
    )
    WHEAT_PET = Pet(
        'Wheat Pet',
        base=AddStats(
            0, 60, 5
        )
    )
    RABBIT_PET = Pet(
        'Rabbit Pet',
        base=AddStats(
            6, 50, 1
        )
    )
    MINT_ICECREAM_PET = Pet(
        'Mint Icecream Pet',
        base=AddStats(
            3, 80, 3
        ),
        buff_flat=AddStats(
            hpr=4
        )
    )
    ROSE_GOLD_PET = Pet(
        'Rose Gold Pet',
        base=AddStats(
            2, 120, 6
        ),
        buff_pet_flat=AddStats(
            hpr=1
        )
    )
    CHARCOAL_PET = Pet(
        'Charcoal Pet',
        base=AddStats(
            0, 75, 3
        ),
        buff_add=AddStats(
            dmg=0.2
        ),
        buff_pet_add=AddStats(
            dmg=0.2
        )
    )
    COD_PET = Pet(
        'Cod Pet',
        base=AddStats(
            7, 40, 6
        )
    )
    PUFFERFISH_PET = Pet(
        'Pufferfish Pet',
        base=AddStats(
            15, 60, 3
        ),
        buff_pet_flat=AddStats(
            hpr=-2
        )
    )
    GLOW_SQUID_PET = Pet(
        'Glow Squid Pet',
        base=AddStats(
            0, 85, 4
        ),
        buff_pet_flat=AddStats(
            hpr=5
        ),
        buff_pet_add=AddStats(
            dmg=-0.1
        )
    )
    AXOLOTL_PET = Pet(
        'Axolotl Pet',
        base=AddStats(
            5, 140, 10
        ),
        buff_add=AddStats(
            dmg=0.45
        ),
        buff_pet_add=AddStats(
            dmg=-0.2
        )
    )
    SNOWMAN_PET = Pet(
        'Snowman Pet',
        base=AddStats(
            3, 75, 1
        ),
        buff_pet_flat=AddStats(
            hpr=2
        )
    )
    YETI_PET = Pet(
        'Yeti Pet',
        base=AddStats(
            16, 200, 5
        ),
        buff_add=AddStats(
            dmg=-0.25
        )
    )
    MAGICAL_SHEEP_PET = Pet(
        'Magical Sheep Pet',
        base=AddStats(
            4, 45, 7
        ),
        buff_pet_add=AddStats(
            dmg=0.35
        )
    )
    OWL_PET = Pet(
        'Owl Pet',
        base=AddStats(
            10, 175, 8
        ),
        buff_pet_flat=AddStats(
            hpr=-1
        )
    )
    ZOMBIE_PET = Pet(
        'Zombie Pet',
        base=AddStats(
            8, 115, 1
        ),
        buff_flat=AddStats(
            hpr=3
        )
    )
    RED_SANDSTONE_PET = Pet(
        'Red Sandstone Pet',
        base=AddStats(
            0, 300, 6
        )
    )
    RADIOACTIVE_ELEPHANT_PET = Pet(
        'Radioactive Elephant Pet',
        base=AddStats(
            10, 120
        ),
        buff_flat=AddStats(
            hpr=-5
        ),
        buff_add=AddStats(
            dmg=40
        ),
        buff_pet_flat=AddStats(
            hpr=-2
        ),
        buff_pet_add=AddStats(
            dmg=40
        )
    )
    FLAMING_SLIME_PET = Pet(
        'Flaming Slime Pet',
        base=AddStats(
            13, 160, 7
        )
    )
    SLIME_DRAGON_PET = Pet(
        'Slime Dragon Pet',
        base=AddStats(
            8, 360, 3
        ),
        buff_add=AddStats(
            dmg=0.35
        ),
        buff_pet_add=AddStats(
            dmg=0.15
        )
    )
    ICE_PHOENIX_PET = Pet(
        'Ice Phoenix Pet',
        base=AddStats(
            4, 280
        ),
        buff_pet_flat=AddStats(
            hpr=3
        )
    )
    GUARDIAN_PET = Pet(
        'Guardian Pet',
        base=AddStats(
            0, 150, 6
        ),
        buff_flat=AddStats(
            hpr=18
        ),
        buff_pet_add=AddStats(
            dmg=-0.15
        )
    )
    TIGER_PET = Pet(
        'Tiger Pet',
        base=AddStats(
            30, 450, 8
        ),
        buff_pet_add=AddStats(
            dmg=-0.35
        )
    )
    HAPPY_ROCK_PET = Pet(
        'Happy Rock Pet',
        base=AddStats(
            6, 1200, 4
        ),
        buff_add=AddStats(
            dmg=-0.1
        )
    )
    CRYING_OBSIDIAN_PET = Pet(
        'Crying Obsidian Pet',
        base=AddStats(
            2, 175, 9
        ),
        buff_add=AddStats(
            dmg=0.3
        ),
        buff_pet_flat=AddStats(
            hpr=2
        )
    )
    DINOSAUR_PET = Pet(
        'Dinosaur Pet',
        base=AddStats(
            27, 320, 10
        ),
        buff_flat=AddStats(
            hpr=-0.1
        )
    )

class Foods:
    BREAD = Food(
        'Bread',
        add=AddStats(
            hp=0.25
        ),
        duration=60
    )
    CARROT_CAKE = Food(
        'Carrot Cake',
        flat=AddStats(
            dmg=4
        ),
        duration=120
    )
    COOKIE = Food(
        'Cookie',
        flat=AddStats(
            hpr=7
        ),
        duration=60
    )
    GOLDEN_PUMPKIN = Food(
        'Golden Pumpkin',
        add=AddStats(
            hp=0.5
        ),
        duration=180
    )
    PUMPKIN_PIE = Food(
        'Pumpkin Pie',
        add=AddStats(
            dmg=0.4
        ),
        duration=120
    )
    SANDWICH = Food(
        'Sandwich',
        add=AddStats(
            hpr=0.6
        ),
        duration=180
    )
    ICE_CREAM = Food(
        'Ice Cream',
        add=AddStats(
            dmg=0.8,
            hp=-0.25
        ),
        duration=60
    )
    MUSHROOM_SOUP = Food(
        'Mushroom Soup',
        add=AddStats(
            hp=0.65
        ),
        duration=240
    )
    STRAWBERRY = Food(
        'Strawberry',
        flat=AddStats(
            hp=100,
            hpr=15
        ),
        duration=120
    )
    MELON_PIE = Food(
        'Melon Pie',
        add=AddStats(
            dmg=-0.2,
            hpr=1
        ),
        duration=180
    )
    SALAD = Food(
        'Salad',
        add=AddStats(
            dmg=0.2,
            hp=0.3,
            hpr=0.25
        ),
        duration=300
    )
    COOKED_COD = Food(
        'Cooked Cod',
        pet_add=AddStats(
            hp=0.3
        ),
        duration=120
    )
    SALMON_SUSHI = Food(
        'Salmon Sushi',
        pet_add=AddStats(
            hpr=0.45
        ),
        duration=60
    )
    COOKED_PUFFERFISH = Food(
        'Cooked Pufferfish',
        pet_add=AddStats(
            dmg=0.6,
            hpr=-0.25
        ),
        duration=120
    )
    COOKED_CLOWNFISH = Food(
        'Cooked Clownfish',
        pet_add=AddStats(
            dmg=-0.15,
            hp=0.4,
            hpr=0.3
        ),
        duration=180
    )
    SUSHI_ROLL = Food(
        'Sushi Roll',
        pet_add=AddStats(
            hp=-0.15,
            hpr=0.75
        ),
        duration=60
    )
    CANDIED_FISH = Food(
        'Candied Fish',
        pet_add=AddStats(
            dmg=0.55
        ),
        duration=180
    )
    GRILLED_GIANT_SALMON = Food(
        'Grilled Giant Salmon',
        pet_add=AddStats(
            dmg=0.1,
            hp=0.45,
            hpr=0.2
        ),
        duration=300
    )

class Waves:
    EASY = Wave(
        'Easy',
        max=30,
        base=AddStats(
            dmg=4,
            hp=20
        )
    )
    MEDIUM = Wave(
        'Medium',
        max=50,
        base=AddStats(
            dmg=7,
            hp=40
        )
    )
    HARD = Wave(
        'Hard',
        max=75,
        base=AddStats(
            dmg=12,
            hp=80
        )
    )
    ENDLESS = Wave(
        'Endless',
        max=-1,
        base=AddStats(
            dmg=20,
            hp=150
        )
    )