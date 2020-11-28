import pygame as pg

class Fish:
    def __init__(self,mass,age,health,name):
        #fish birth )
        #mass - mass of fish
        #age - age of fish
        #health - helth of fish
        self.mass = mass
        self.age = age
        self.health = health
        self.name = name
       
    def eat(self):
        # all fish can eat)
        pass
    
    def swim(self):
        print('i can swim')
    
    def fish_dead(self):
        #fish dead
        pass

class Bream(Fish):
    pass
class Roach(Fish):
    pass
class Skremers(Fish):
    pass


b = Bream()




    