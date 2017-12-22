# Hero class

class hero:
    health = 30
    
    def isDead(self):
        if (self.health == 0): 
            return True
        else:
            return False
