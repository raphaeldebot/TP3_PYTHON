mot=input("Veuillez entrez une phrase svp : ")

res = 1
for c in mot:
    if c == " ":
        res+= 1

print(res)