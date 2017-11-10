f=open("iLearned.txt","w")
class django:
    def __init__(self,name="no name"):
        self.name=name

    def myWork(self):
        f.write("I learned from {} at Youtube\n"
                "I'm learning Django framework\n"
                "I finished from Models\n"
                "Now i can do new fields , after finish of it \nI do migration "
                "to my project and i can add pages to admin\n"
                "This my pictures for show you what i did . ".format(self.name))
        f.close()

mess=django("Mohammed Essa")
mess.myWork()
