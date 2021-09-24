'''
Created on 30.8.2021 15.35

author: sakukarttunen
'''

userinput = input("just mash your keyboard here: ")

print("let's digest", userinput)

specials = set(userinput)

length = len(specials)

print("unique characters: ", length, "\n", "which are: ", specials)

