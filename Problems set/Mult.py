num = int(input())
mul = list(list(range(i,(num+1)*i, i))for i in range (1,num+1))
print(mul)