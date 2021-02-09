from enemy import Enemy, Troll

#object instantiated from Enemy class using default args
basic_enemy = Enemy()
print(basic_enemy)

#object instantiated from Enemy class using new args passed to constructor
random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

#call to take_damage method in Enemy class
random_monster.take_damage(4)
print(random_monster)
 

#instantiate objects from sub class Troll 
#Note only name arg is requierd. enemy super class args for hit_points and lives are used
ugly_troll = Troll("Pug")
print(f"Ugly Troll - {ugly_troll}")

#instantiate object another_troll from sub class Troll 
#Note new args are passed in
another_troll = Troll("Ug")
print(f"another Troll - {another_troll}")

brother = Troll("Urg")
print(f"brother - {brother}")

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

