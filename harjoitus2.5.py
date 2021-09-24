'''
Created on 13.9.2021
@author: sakuk
'''
player0_char = 'X'  # Pelaajan 0 merkki
player1_char = 'O'  # Pelaajan 1 merkki
gameRunning = True
# available_inputs = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'C0', 'C1', 'C2', ]
# aseta tässä 0.pelaaja aktiiviseksi
player = 0


def printGameboard():
    print(gameboard['A'])
    print(gameboard['B'])
    print(gameboard['C'])


def setUserPointTo(alpha, number, player):
    if player == 0:
        player_char = player0_char
    else:
        player_char = player1_char
    gameboard[alpha][number] = player_char

    
# tarkista seuraavassa funktiossa, että haluttu pelipositio on käytettävissä
def checkValidPoint(row, col):
    if row in gameboard and 0 <= col <= 2:
        if gameboard[row][col] == " ":
            return True
        else:
            print("* Virhe, ruutu on jo valittuna")
            return False
        

# tarkista seuraavassa, onko jompi kumpi pelaajista voittanut
def checkWin():
    if player == 0:
        mark = "X"
    else:
        mark = "O"
        
    # vaakatasossa
    for row in gameboard:
        if gameboard[row][0] == mark and gameboard[row][1] == mark and gameboard[row][2] == mark:
            print("* Vaakatasolla")
            return True
        
    # Pystytasossa
    for i in range(0, 2):
        if gameboard['A'][i] == mark and gameboard['B'][i] == mark and gameboard['C'][i] == mark:
            print("* Pystysuorasssa")
            return True
        
    # Ristiin
    if gameboard['A'][0] == mark and gameboard['B'][1] == mark and gameboard['C'][2] == mark:
        print("* Vinossa #1")
        return True
        
    if gameboard['C'][0] == mark and gameboard['B'][1] == mark and gameboard['A'][2] == mark:
        print("* Vinossa #2")
        return True
    
    return False

"""
 Kuvitteellinen pelilauta
 Ajatellaan että koordinaatit ovat ensimmäisellä rivillä     A0, A1 ja A2
 toisella rivillä     B0, B1 ja B2
 kolmannella rivillä  C0, C1 ja C2
"""
gameboard = {'A': [" ", " ", " "],
             'B': [" ", " ", " "],
             'C': [" ", " ", " "]}

player0_name = input("Pelaaja 0, anna nimesi: ")
player1_name = input("Pelaaja 1, anna nimesi: ")
print("* Huomio: anna syöte muodossa esim. A0, C2, B1")

while gameRunning:

    # pyydä tässä inputilla halutun pelaajan seuraava pelipostio
    if player == 0:
        action = input(f"pelaajan {player0_name}, vuoro: ")
        
    else:
        action = input(f"pelaajan {player1_name}, vuoro: ")
    
    # kutsu seuraavassa sopivan position tarkistusta ja jos niin, aseta uusi pelimerkki laudalle
    if checkValidPoint(action[0], int(action[1])):
        setUserPointTo(action[0], int(action[1]), player)
        
        # pelilauta printtaus
        printGameboard()

        # tarkista mahdollinen voitto
        if checkWin():
            if player == 0:
                input(f"Onneksi olkoon {player0_name}, voitit! Paina mitä vaan näppäintä lopettaaksesi pelin")
                break
        
            if player == 1:
                input(f"Onneksi olkoon {player1_name}, voitit! Paina mitä vaan näppäintä lopettaaksesi pelin")
                break

        # tarkista onko kaikki pelipositiot käytetty. Jos on niin lopeta peli!
        if not ' ' in gameboard['A'] and not ' ' in gameboard['B'] and not ' ' in gameboard['C']:
            print("Peli päättyi. Sillä tila loppui")
            break
        
        # vaihda pelaajaa seuraavaa kierrosta varten (0->1 tai 1->0)
        player = 1 - player
