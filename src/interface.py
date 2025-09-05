import json

from registry import Specializations, Companions, Pets, Waves
from levels import Levels
from build import Build
from player import Player, Pet
from enemy import Enemy
from run import Run

class Interface:
    def __init__(self):
        self.players: list[Levels] = self.load_players()

        self.builds: list[Build] = self.load_builds()
        self.build: Build = None

    @staticmethod
    def load_players():
        try:
            players = []
            with open('data/levels.json', 'r') as f:
                for line in f:
                    players.append(Levels(**json.loads(line)))
            return players
        except FileNotFoundError:
            return []

    @staticmethod
    def load_builds():
        try:
            builds = []
            with open('data/builds.json', 'r') as f:
                for line in f:
                    builds.append(Build(**json.loads(line)))
            return builds
        except FileNotFoundError:
            return []

    def start(self):
        self.set_levels()
        self.set_build()

        player = Player(self.build)

        seen_pets = set()
        first = Pet(self.build, self.get_pet(seen_pets))
        second = Pet(self.build, self.get_pet(seen_pets))
        third = Pet(self.build, self.get_pet(seen_pets))
        fourth = Pet(self.build, self.get_pet(seen_pets))

        enemy = Enemy(self.build, self.get_enemy())

        run = Run(enemy, player, first, second, third, fourth)
        end = run.start()
        if end[1]:
            print(f'Cleared {enemy.name.capitalize()} (Wave {end[0]})')
        elif not end[1]:
            print(f'Failed to clear {enemy.name.capitalize()} (Wave {end[0]})')

    def set_levels(self):
        levels = None
        if self.players:
            print(self.players)
            while not levels:
                userinput = input("Select a Player or enter 'new' to create a new Player: ")
                if userinput.lower() == 'new':
                    levels = Levels.manual()
                else:
                    for player in self.players:
                        if userinput == player.name:
                            levels = player
                if not levels:
                    print(f"Invalid selection: '{userinput}'")
        else:
            print('No existing players. Creating a new Player...')
            levels = Levels.manual()

        Specializations(**levels.specializations())
        Companions(**levels.companions())

    def set_build(self):
        if self.builds:
            print(self.builds)
            while not self.build:
                userinput = input("Select a Build or enter 'new' to create a new Build: ")
                if userinput.lower() == 'new':
                    self.build = Build.manual()
                else:
                    for build in self.builds:
                        if userinput == build.name:
                            self.build = build
                if not self.build:
                    print(f"Invalid selection: '{userinput}'")
        else:
            print('No existing builds. Creating a new Build...')
            self.build = Build.manual()

    @staticmethod
    def get_pet(seen):
        ordinals = ['First', 'Second', 'Third', 'Fourth']
        while True:
            try:
                ordinal = ordinals[len(seen)]
                userinput = input(f'{ordinal} Pet: ').upper().replace(' ', '_')
                if not hasattr(Pets, userinput) or userinput in seen:
                    raise ValueError
                seen.add(userinput)
                return userinput
            except ValueError:
                print(f"Invalid value: '{userinput}'")

    @staticmethod
    def get_enemy():
        while True:
            try:
                difficulties = ['Easy', 'Medium', 'Hard', 'Endless']
                userinput = input(f'\n{difficulties}\nSelect a difficulty: ')
                if userinput.capitalize() not in difficulties:
                    raise ValueError
                return userinput.upper()
            except ValueError:
                print(f"Invalid value: '{userinput}'")

interface = Interface()
interface.start()