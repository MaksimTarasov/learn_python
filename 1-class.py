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
    def fishStatus(self):
        print("Hello my name is", self.name)
        print("my age:", self.age)
        print("my mass:", self.mass)
        print("my health:", self.health)

class Bream(Fish):
    pass
   
class Roach(Fish):
    pass
class Skremers(Fish):
    pass


bream1 = Bream(2,1,100,"Bream")

bream1.fishStatus()




    