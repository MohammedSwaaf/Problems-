Sentence= str(input("Enter The Sentence\n"))
Char = str(input("Enter the char\n"))
IND=[n for n in range(len(Sentence)) if Sentence.startswith(Char,n)]
print(IND)