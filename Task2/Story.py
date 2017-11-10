class pesron:
    def __init__(self,**kwargs):
        self.attPsn=kwargs
    def setName(self,name):
        self.attPsn["name"]=name
    def getName(self):
       return self.attPsn.get("name","Null")

    def setMoney(self,money):
        self.attPsn["money"]=money
    def getMoney(self):
       return self.attPsn.get("money",0)

    def setMood(self,mood):
        self.attPsn["mood"]=mood
    def getMood(self):
     return self.attPsn.get("mood","Normally")

    def setHealthRate(self,health):
        self.attPsn["health"]=health
    def getHealthRate(self):
        return self.attPsn.get("health",0)
    def sleep(self,hours):
        self.hours=hours
        print("Please Enter the hours you slept \n")
        if hours==7:
            print("Happy")
        elif hours>7:
            print("Tired")
        else:
            print("lazy")

    def eat(self,meals):
        self.meals=meals
        #print("Please Enter the meals you ate")
        if meals==3:
            return ("hth = 100%")
        elif meals==2:
            return ("hth = 75%")
        elif meals==1:
            return ("hth = 50%")
        else:
            return ("Try again")
    def buy(self,items):
        self.items=items
        #print("please Enter the numbers of items")
        NumItem=items*10
        return self.getMoney()-NumItem

        #Class Employee
class Employee(pesron):
    def __init__(self,**kwargs):
        self.attEmp=kwargs
    def setId(self,id):
        self.attPsn["id"]=id
    def getId(self):
       return self.attEmp.get("id",0)

    def setCar(self,car):
        self.attEmp["car"]=car
    def getCar(self):
       return self.attEmp.get("car","fiat")

    def setSalary(self,salary=1000):
        self.attEmp["salary"]=salary
    def getSalary(self):
     return self.attEmp.get("salary",1000)

    def setDTW(self,DistTW):
        self.attEmp["DistTW"]=DistTW
    def getDTW(self):
        return self.attEmp.get("DistTW",0)

    def work(self,Hours):
        self.Hours=Hours
        if Hours==8:
            return "Happy"
        elif Hours>8:
            return  "Tired"
        else:
            return "lazy"

    def drive(self,distance): #Method of distance
        self.distance=distance

    def refuel (self,gasAmount=1000): #Method of refuel
        self.fuelRate=gasAmount








class car(Employee,pesron):
    def __init__(self,**kwargs):
        self.attCar=kwargs

    def setName(self,name):
        self.attCar["name"]=name
    def getName(self):
       return self.attCar.get("name","Null")

    def setVelocity(self,velocity):
        self.attCar["velocity"]=velocity
    def getVelocity(self):
       return self.attCar.get("velocity",0)

    def setFR(self,FuelRate):
        self.attCar["FuelRate"]=FuelRate
    def getFR(self):
       return self.attCar.get("FuelRate",0)

    def run(self,velocity, distance):
        self.velocity=velocity
        self.distance=distance

    def stop(self):
        self.velocity=0
        return "that you arrive the destintation"
class office(car):
    def __init__(self,name,employees=[]):
        self.name=name
        self.employees=employees
        office.changeEmpysNum(office.employeesNum)
    def get_all_employees(self):
        return self.employees
    def get_employee(self,empld):
        self.empld=empld
        for self.employee in self.employees:
            if self.employee.getId() == empld:
                return self.employee
    def hire(self,employee):
        self.employees.append(employee)
    def fire(self,empld):
        for self.employee in self.employees:
            if self.employee == empld:
                self.employees.remove(self.employee)
    def deduct(self,deduction):
        self.deduction=deduction
        deduction-self.getSalary()
    def reward(self,reward):
        self.reward=reward
        reward+self.getSalary()
    def checkLatness(self,moveHour,targethour):
        self.moveHour=moveHour
        self.targethour=targethour
        targethour=self.getDTW()/20+moveHour
        if targethour<9:
            return "false"
        else:
            return "True"













#obj2=pesron(money=1000)
#print(obj2.buy(10))
#print(obj2.eat(2))




#obj=pesron(name="Mohammed",money=1000,mood="Good",health=70)
#print(obj.getName())
#print(obj.getMoney())
#print(obj.getMood())
#print(obj.getHealthRate())
#obj.buy()


