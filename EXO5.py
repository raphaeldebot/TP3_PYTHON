mot=input("Veuillez entrez un mot svp")
motInverser=""
for c in mot:
    motInverser= c + motInverser

if mot == motInverser:
    print("C'est un palindrome")
else:
    print("C'est pas un palindrome")
