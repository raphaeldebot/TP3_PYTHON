mot=input("Veuillez entrez un mot svp")
lettre=input("Veuillez entrer une lettre svp")
res = 0
for c in mot:
    if c == lettre:
        res+= 1

print(res)