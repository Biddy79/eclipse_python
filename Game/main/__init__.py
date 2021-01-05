from player import Player

Adam = Player("Adam")

from enemy import Enemy

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)