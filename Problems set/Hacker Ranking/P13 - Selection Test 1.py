A=int(input())
B=int(input())
C=int(input())
D=int(input())
if (B > C and D > A and (C+D) > (A+B) and (C and D) >=0 and A%2==0 ):
    print("Valores aceitos\n")
else:
    print("Valores nao aceitos\n")