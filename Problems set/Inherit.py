class animal (object):
    def __init__(self,name):
        self.name = name
        print("The name of animal is {} ".format(name))
        
    def eat(self,food):
        print("{} is eating {}".format(self.name,food))    
class dog (animal):
    def fetch (self,thing):
        print("{} is fetching {}".format(self.name,thing))
        
class cat (animal):
    def cat_eat(self, lunch):
        print("{} eats {}".format(self.name,lunch))