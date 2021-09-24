def ispalindrome(userinput):
    return userinput == userinput[::-1]


userinput = input("Anna palindrome: ")
answ = ispalindrome(userinput)

if answ:
    print(f"Sana {userinput}, on palindrome")
else:
    print(f"Sana {userinput}, ei ole palindrome")
