class Person:
    def __init__(self,**kwargs):
        self.info=kwargs
    def setName(self,name):
        self.info['name']=name
    def getName(self):
        return self.info.get('name',"Null")

    def setDept(self,dept):
        self.info['dept']=dept
    def getDep(self):
       return self.info.get('dep',"No Dep")

    def setSalary(self,salary):
        self.info['salary']=salary
    def getSalary(self):
        return self.info.get('salary',"No Salary")
    def buy(self,items):
        self.items=items
        print("please Enter the numbers of items")
        items-self.getMoney()

prop = Person(name="Mohammed Swaaf",dep="Programming",salary="7000")
print(prop.getName())
print(prop.getSalary())
print(prop.getDep())