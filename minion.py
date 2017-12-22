# Minion class

class minion:
    health = 0
    name = ""
    
    def __init__(self, health, name):
        self.health = health
        self.name = name
    
    def __str__(self):
        return "(Name: " + str(self.name) + ", Health: " + str(self.health) + ")"
    
    def isDead(self):
        if (self.health == 0): 
            return True
        else:
            return False

    
    