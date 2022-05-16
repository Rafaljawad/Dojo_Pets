
class Ninga:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        return f"{self.first_name} walked {self.pet.name} "
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        return f"{self.pet.name} has been fed "

# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        return f"{self.first_name} is bathing  {self.pet.name}, {self.pet.name} is making {self.pet.noise()} "

