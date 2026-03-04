mot=input("Veuillez entrez un mot svp")

res = 0
for c in mot:
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "y":
        res+= 1

print(res) 