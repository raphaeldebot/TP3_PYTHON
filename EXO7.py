phrase=input("Veuillez entrez unee phrase svp")

res = ""
for c in phrase:
    if c != " " or res != "":
        res+= c


res2 = ""
dernier = ""

for c in res:
    res2 += c
    if c != " ":
        dernier = res2

print(dernier)