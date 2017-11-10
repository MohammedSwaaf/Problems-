f=open("file.txt","r+")
class print:
    def __init__(self,of="No one",to="Null",name="no name",subj="None"):
        self.of = of
        self.to = to
        self.name=name
        self.subj=subj
    def se(self):
        f.write("From:{}\n".format(self.of))
        f.write("To:{}\n\n".format(self.to))
        f.write("Hi,{}\nThis is an email tamplate\nthanks\n".format(self.name))
        f.write("{}\n".format(self.subj))
        f.close()
email=print(str(input()),str(input()),str(input()),str(input()))
email.se()

