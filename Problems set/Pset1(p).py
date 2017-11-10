#The degree from user
x=int(input("Please enter your degree"))
#if student got degree less than 50 he been fail
if x<=49:
    print("Fail")
elif x>=50 and x<=64: #if student got degree less than 65 and more than 50 he got Acsaptable
    print("Acsaptable")
elif x>=65 and x<=74: #if student got degree less than 75 and more than 65 he got good
    print(" Good")
elif x >=75 and x <=84: #if student got degree less than 85 and more than 75 he got very good
    print("Very Good")
else: #if student got degree  more than 85 he got Exelant
    print("Exelant")

