# phrase=input("Veuillez entrez une phrase svp")
# last_charactere = ""
# res = ""
# for c in phrase:
#     if c != "" and last_charactere == " " :
#         res+= c
#         last_charactere = c

# print(res)

phrase=input("Veuillez entrez une phrase svp")
phrase_clean = ""
last_caractere = ""

for c in phrase:
    if not (c == " " and last_caractere == " "):
        phrase_clean += c 

    last_caractere = c 

print(f"La réponse : '{phrase_clean}'")