class Animal:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species

    
    def speak(self):
        return "bark"
    
    def __str__(self):
        return f"{self.name} the {self.species} is running around the yard"
    
    
class Mammal(Animal):
    
    def give_birth(self):
        print(f"The {self.name}  gave birth")
        

class Bird(Animal):
    
    def __init__(self,name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

class Reptile(Animal):
    
    def bask_in_sun(self):
        print(f"The {self.name} is basking in the sun.")
        
        
class Primate(Mammal):
    
    def climb_trees(self):
        print(f"This {self.name} can climb trees.")
        
        
class Marsupial(Mammal):
    
    def carry_baby(self):
        print(f"This {self.name} is carrying it's baby.")
        

class Aviary:
    
    def __init__(self):
        self.birds = []
        
    def add_bird(self, bird):
        self.birds.append(bird)
        
class ReptileEnclosure:
    
    def __init__(self):
            self.reptiles = []
            
    def add_reptile(self, reptile):
            self.reptiles.append(reptile)
            
            
class Zoo:
    
    def __init__(self, name):
        self.name = name
        self.aviary = Aviary()
        self.reptile_enclosure = ReptileEnclosure()
        
        
    
reptile = Reptile("Charles", "lizard")

bird = Bird("Bobbie", "Pelican", "ten feet")          
zoo = Zoo("Dallas")
zoo.aviary.add_bird(bird)
zoo.reptile_enclosure.add_reptile(reptile)
print(zoo.aviary.birds[0])
print(zoo.reptile_enclosure.reptiles[0])

 
           
animal = Animal("bob", "pig")
print(animal)