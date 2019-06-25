def EsPalindrome(palabra):
    for i in range(int(len(palabra)/2)):
        if palabra[i] != palabra[int(len(palabra)-1-i)]:
            return False

    return True

palabra = input("Digite la palabra o frase: ")
#palabraInvertida = palabra[::-1]

#print("Es palíndrome" if palabra == palabraInvertida else "No es palíndrome")

print("Es palíndrome" if EsPalindrome(palabra) else "No es palíndrome")
