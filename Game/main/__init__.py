from enemy import Enemy, Troll

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

#Note in python when over loading a constructor you do not have to write a new constructor 
#with set nuber of args for each case. Below three object are instantiated from Troll
#all with diffrent number of paramerters but only one constructor is write fro Troll in Enemy modual  

#instantiate object ugly_troll from sub class Troll 
#Note no args are given therefor enemy super class args are used by default
ugly_troll = Troll()
print(f"Ugly Troll - {ugly_troll}")

#instantiate object another_troll from sub class Troll 
#Note new args are passed in
another_troll = Troll("Ug", 18, 1)
print(f"another Troll - {another_troll}")

brother = Troll("Urg", 23)
print(f"brother - {brother}")