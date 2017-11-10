Maximam = None
Minimam = None

while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        if Maximam is None:
            Maximam = int(num)
        if int(num) > Maximam:
            Maximam = int(num)
        if Minimam is None:
            Minimam = int(num)
        if int(num) < Minimam:
            Minimam = int(num)
    except:
        print ("Invalid input")

print ("Maximum is", Maximam)
print ("Minimum is", Minimam)