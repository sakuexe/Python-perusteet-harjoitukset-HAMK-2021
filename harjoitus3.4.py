#Tehtävä 3.4 / noppapeli vastakkain
import random

def findMin(a,b):
    return min(a,b)

def findMax(a,b):
    return max(a,b)

def rollDice():
    print("the die gets cast")
    return random.randint(1,6)

def main():
    player1DieValue = rollDice()
    player2DieValue = rollDice()
    print(f"Pelaaja 1 heitti: {player1DieValue}.")
    print(f"Pelaaja 2 heitti: {player2DieValue}.")
    if player1DieValue > player2DieValue:
        print(f"Voittaja on Pelaaja 1, {findMax(player1DieValue, player2DieValue)} -pisteellä")
    
    elif player1DieValue < player2DieValue:
        print(f"Voittaja on Pelaaja 2, {findMax(player1DieValue, player2DieValue)} -pisteellä")
    
    else:
        print(f"tasapeli {player1DieValue} -pisteellä")

main()