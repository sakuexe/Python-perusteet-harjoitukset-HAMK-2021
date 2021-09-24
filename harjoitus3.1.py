#numeroiden lista
numbers = []

def addNumber(): #Looppi joka lisää käyttäjän inputin numero listaan. lopettaa kun käyttäjä kirjoittaa 0
    while True:
        myNumber = int(input("Anna numero, 0 lopettaa: "))
        numbers.append(myNumber)
        if myNumber == 0:
            break

def sumItAll(numberList):
    sum = 0 #tehdään muuttuja "summa"
    for x in numberList: #numerolista käydään numero kerrallaan ja lisätään numerot "summaan" plussaten
        sum += x
    print(f"Listan summa on {sum}") #printataan muuttuja summa

def main():
    addNumber()

    sumItAll(numbers)#lisätään parametri numbers jotta funktio tietää mille muuttujalle asiat tehdään

main()