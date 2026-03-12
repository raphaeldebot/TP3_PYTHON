phrase = input("Entrez une phrase : ")
mot = ""
res = ""

for c in phrase:
    if c == " ":
        res = mot + " " + res 
        mot = ""
    else:
        mot += c

res = mot + " " + res 

print(f"Résultat :{res}")