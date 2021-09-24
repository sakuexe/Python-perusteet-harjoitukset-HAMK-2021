#tehtävä 2.1. saku karttunen

import time

#aakkoslista
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]

#numerolista
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

#kysyy käyttäjältä kirjainta
käyttäjä_kirjain = input("anna kirjain jota etsitään aakkosista:" )

for i in alphabets:
    if käyttäjä_kirjain == i:
        käyttäjä_numero = alphabets.index(käyttäjä_kirjain)
            
        print("kirjain", käyttäjä_kirjain, "on aakkosten", käyttäjä_numero + 1,". kirjain.")
        break

for x in numbers:
    if käyttäjä_kirjain == x:
        print(käyttäjä_kirjain, "on numero eikä kirjain")
        break

time.sleep(3) #odotus jotta voidaan katsoa löysikö looppi kirjainta listoilta

if käyttäjä_kirjain == i or käyttäjä_kirjain == x:
    print("kiitos, kokeile uudelleen")
    exit()

else:
    print("kirjaintasi ei löydy, yritä uudelleen ja tarkista että se on kirjoitettu pienellä")
    exit()
