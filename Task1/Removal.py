name=str(input("enter the name "))
vowles=['a','A','o','O','i','I','u','U','e','E']
for x in name:
    if x in vowles:
        name=name.replace(x,"")
print(name)


