n=int(input("Enter the number \n"))
if n%2 !=0:
    print ("wired")
elif n%2==0 and 2<=n<=5:
    print ("not wired")
elif n%2==0 and 6<=n<=20:
    print ("wired")
else:
    print("Not wired")