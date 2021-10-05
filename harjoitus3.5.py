#Tehtävä 3.5 / noppapeli DLC
import random
import time

points = [0,0]

def findMin(a,b):
    return min(a,b)

def findMax(a,b):
    return max(a,b)

def rollDice():
    return random.randint(1,6)

def round():
    player1DieValue = rollDice()
    player2DieValue = rollDice()
    print(f"Pelaaja 1 heitti: {player1DieValue}.")
    print(f"Pelaaja 2 heitti: {player2DieValue}.")

    if player1DieValue == findMax(player1DieValue, player2DieValue):
        print("Pelaaja 1 voitti")
        points[0] += 1

    elif player2DieValue == findMax(player1DieValue, player2DieValue):
        print("Pelaaja 2 voitti")
        points[1] += 1
    else:
        print("Tasapeli, ei pisteitä")

def main():
    rounds = int(input("Montako kierrosta pelataan? "))
    roundCounter = 1

    while rounds > 0:
        print("Kierros", roundCounter)
        time.sleep(3)
        round()
        print(f"Pelitilanne on {points[0]} - {points[1]}")
        rounds -= 1
        roundCounter += 1
    if points[0] > points[1]:
        print(f"Pelaaja 1 Voitti {points[0]} pisteellä")
    elif points[0] < points[1]:
        print(f"Pelaaja 2 Voitti {points[1]} pisteellä")
    else:
        print(f"Tasapeli, ei voittajaa {points[0]} - {points[1]}")
main()