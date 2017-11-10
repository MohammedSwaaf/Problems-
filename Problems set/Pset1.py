#The number from user
X=int(input("Please Enter your number \n "))
print("The factorial = ")
#the loop for passing in input
for i in range(X+1):
    if i==0:
        fact=1
    else:
        fact=fact*i
        print(fact)


