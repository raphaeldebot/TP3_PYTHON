phrase = input("Veuillez entrer une phrase svp : ")

mot = ""
plus_long = ""

taille = 0
taille_max = 0

for c in phrase:
    if c != " ":
        mot += c
        taille += 1
    else:
        if taille > taille_max:
            plus_long = mot
            taille_max = taille
        mot = ""
        taille = 0

if taille > taille_max:
    plus_long = mot


    print(f"{plus_long} est la plus longue")