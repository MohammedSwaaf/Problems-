class Human:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def measureTemp(temp):
        if (temp == 37):
            print("Normal")
        else:
            print ("Not Normal")
Human.measureTemp(int(input()))