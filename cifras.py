def cifra_caracter_rot42(caracter, delta=42):
    "Essa funcao deve receber apenas um caracter como parametro"
    if caracter.upper() not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return caracter
    eh_minuscula = caracter.islower()
    caracter = caracter.upper()
    caracter_codigo = ord(caracter)
    caracter_normalizado = caracter_codigo - ord('A')
    caracter_mais_42 = caracter_normalizado + delta
    caracter_codigo_cifrado_normalizado = caracter_mais_42 % 26
    caracter_codigo_cifrado = caracter_codigo_cifrado_normalizado + ord('A')
    caracter_cifrado = chr(caracter_codigo_cifrado)
    return caracter_cifrado.lower() if eh_minuscula else caracter_cifrado


def rot42(texto):
    texto_cifrado = ''
    for caracter in texto:
        texto_cifrado += cifra_caracter_rot42(caracter)
    return texto_cifrado


def decifrar_rot42(texto):
    texto_cifrado = ''
    for caracter in texto:
        texto_cifrado += cifra_caracter_rot42(caracter=caracter, delta=42)
    return texto_cifrado


def cifrar_cesar(texto, delta):
    texto_cifrado = ''
    for caracter in texto:
        texto_cifrado += cifra_caracter_rot42(caracter, delta)
    return texto_cifrado

def decifrar_cesar(texto, delta):
    cifrar_cesar(texto,-delta)


print(rot42('ABC'))
print(rot42('abc'))
print(rot42('1234567890çá'))

print(decifrar_rot42('QRS'))
print(decifrar_rot42('qrs'))
print(decifrar_rot42('1234567890çá'))

print(cifrar_cesar('ABC',1))
print(decifrar_cesar('BCD',1))

