class Enemy:
    
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        
    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f"I took {damage} points and have {self.hit_points} left")
        else:
            self.lives -= 1
    
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)

#class Troll inherits from Enemy
class Troll(Enemy):
    
    def __init__(self, name):
        super().__init__(name=name, hit_points=23, lives=1)
        
    def grunt(self):
        print(f"Me {self.name}. {self.name} stomp you")