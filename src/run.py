from stats import AddStats, BonusStats
from player import Pet

class Run:
    def __init__(self, enemy, player, first = Pet(), second = Pet(), third = Pet(), fourth = Pet()):
        self.enemy = enemy
        self.player = player
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

        self.wave = 1
        self.time = player.bonus.time
        self.tick = 0

    def start(self):
        all = [self.first, self.second, self.third, self.fourth]

        player_flat = AddStats()
        player_add = AddStats()
        pet_flat = AddStats()
        pet_add = AddStats()

        for pet in all:
            player_flat += pet.buff_flat
            player_add += pet.buff_add
            pet_flat += pet.buff_pet_flat
            pet_add += pet.buff_pet_add

        self.player.final = (self.player.base + player_flat) * (self.player.add + player_add)
        self.player.current = self.player.final.hp

        for pet in all:
            pet.final = (pet.base + pet_flat) * (pet.add + pet_add)
            pet.current = pet.final.hp

        while self.wave <= self.enemy.max or self.enemy.max == -1:
            active = {pet for pet in [self.first, self.second, self.third, self.fourth] if pet.is_alive()}

            self.fight(active)

            if not self.player.is_alive():
                return self.wave, False

            # time scaling for hpr (player + pets)
            self.rest(active)

            self.tick = 0
            self.wave += 1
            self.enemy.final = self.enemy.base * self.wave * self.enemy.multi

        return self.wave, True

    def fight(self, active):
        while self.enemy.is_alive() and self.player.is_alive():
            self.tick += 1

            if self.tick >= self.time:
                self.player.kill()
                break

            player_flat = AddStats()
            player_add = AddStats()
            pet_flat = AddStats()
            pet_add = AddStats()

            for pet in active:
                player_flat += pet.buff_flat
                player_add += pet.buff_add
                pet_flat += pet.buff_pet_flat
                pet_add += pet.buff_pet_add

            self.player.final = (self.player.base + player_flat) * (self.player.add + player_add)
            for pet in active:
                pet.final = (pet.base + pet_flat) * (pet.add + pet_add)

            self.enemy.final.hp -= self.player.final.dmg + sum(pet.final.dmg for pet in active)

            overflow = self.enemy.final.dmg

            # dmg tick
            while overflow != 0:
                pets_alive = set(active)
                n = len(pets_alive) + 1

                if overflow < n:
                    break

                distributed_dmg = overflow // n
                overflow = overflow % n

                self.player.current -= distributed_dmg
                if not self.player.is_alive():
                    break

                for pet in pets_alive:
                    pet.current -= distributed_dmg
                    if not pet.is_alive():
                        overflow += 0 - pet.current
                        pet.current = 0
                        active.remove(pet)

            if not self.player.is_alive():
                break

            # hpr tick
            self.player.current = min(self.player.current + self.player.final.hpr, self.player.final.hp)
            if not self.player.is_alive():
                break

            copy = set(active)
            for pet in active:
                if pet.is_alive():
                    pet.current = min(pet.current + pet.final.hpr, pet.final.hp)
                if not pet.is_alive():
                    copy.remove(pet)
            active = set(copy)

    def rest(self, active):
        while self.tick < self.time:
            self.tick += 1

            player_flat = AddStats()
            player_add = AddStats()
            pet_flat = AddStats()
            pet_add = AddStats()

            for pet in active:
                player_flat += pet.buff_flat
                player_add += pet.buff_add
                pet_flat += pet.buff_pet_flat
                pet_add += pet.buff_pet_add

            self.player.final = (self.player.base + player_flat) * (self.player.add + player_add)
            self.player.current = min(self.player.current + self.player.final.hpr, self.player.final.hp)

            all = [self.first, self.second, self.third, self.fourth]

            for pet in all:
                pet.final = (pet.base + pet_flat) * (pet.add + pet_add)
                pet.current = min(pet.current + pet.final.hpr, pet.final.hp)
                if pet.is_alive():
                    active.add(pet)
                elif not pet.is_alive():
                    active.remove(pet)