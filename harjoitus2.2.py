'''
Created on 30.8.2021 15.35

author: sakukarttunen
'''

userinput = input("just mash your keyboard here: ")

print("let's digest", userinput)

chars = list(userinput)
unique = len(set(chars))

print("unique characters:", unique)

