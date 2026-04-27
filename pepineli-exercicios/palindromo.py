palavra = input("Digite uma palavra: ")

palavra_limpa = palavra.replace(" ", "").lower()

palavra_invertida = palavra_limpa[::-1]

if palavra_limpa == palavra_invertida:
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo.')