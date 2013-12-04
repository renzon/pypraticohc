def cifra_caracter_rot42(caracter):
    "Essa funcao deve receber apenas um caracter como parametro"

    caracter_codigo = ord(caracter)
    caracter_normalizado = caracter_codigo - ord('A')
    caracter_mais_42 = caracter_normalizado + 42
    caracter_codigo_cifrado_normalizado = caracter_mais_42 % 26
    caracter_codigo_cifrado = caracter_codigo_cifrado_normalizado + ord('A')
    return chr(caracter_codigo_cifrado)

def rot42(texto):
    texto_cifrado=''
    for caracter in texto:
        texto_cifrado+=cifra_caracter_rot42(caracter)
    return texto_cifrado

print(rot42('ABC'))

