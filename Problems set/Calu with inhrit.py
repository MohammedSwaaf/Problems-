class cal:
    def __init__ (self,a,b):
        self.a = a
        self.b = b
        print ("Welcome . It's small Calculator Enter the name of ur opearation ")
    #Function for addtion     
    def add (self):
        return self.a+self.b
        
    #Function for subtract     
    def sub (self):
        return self.a-self.b
        
    #Function for multiply     
    def mul (self):
        return self.a*self.b
        
    #Function for divion     
    def div (self):
        return self.a/self.b
        
        # Inheritance 
class sci (cal):
    def power(self):
        return pow(self.a , self.b)
    


        
        