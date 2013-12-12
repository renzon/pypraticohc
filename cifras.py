from itertools import cycle


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
    return cifrar_cesar(texto, -delta)


def cifra_caracter_unicode(caracter, delta):
    caracter_codigo = ord(caracter)
    caracter_codigo += delta
    caracter_codigo %= 0x10FFFF
    return chr(caracter_codigo)


def cifrar_unicode(texto, delta):
    texto_cifrado = ''
    for caracter in texto:
        texto_cifrado += cifra_caracter_unicode(caracter, delta)
    return texto_cifrado


print(rot42('ABC'))
print(rot42('abc'))
print(rot42('1234567890çá'))

print(decifrar_rot42('QRS'))
print(decifrar_rot42('qrs'))
print(decifrar_rot42('1234567890çá'))

print(cifrar_cesar('ABC', 1))
print(decifrar_cesar('BCD', 1))

print(cifrar_unicode('ABCD', 1))
print(cifrar_unicode('Renzo Nuccitelli', 0x2800))
print(cifrar_unicode('⡒⡥⡮⡺⡯⠠⡎⡵⡣⡣⡩⡴⡥⡬⡬⡩', -0x2800))


def _cifrar(texto, deltas):
    texto_cifrado = ''
    for caracter in texto:
        delta = next(deltas)
        texto_cifrado += cifra_caracter_rot42(caracter, delta)
    return texto_cifrado


def cifrar(texto, chave_privada):
    deltas = cycle(map(ord, chave_privada))
    return _cifrar(texto, deltas)


def decifrar(texto, chave_privada):
    deltas = cycle(-ord(c) for c in chave_privada)
    return _cifrar(texto, deltas)



print(cifrar('Renzo Nucciiteli', "".join([chr(i) for i in range(1, 3)])))
print(cifrar('Renzo Nucciiteli', "Renzo Nucciiteli"))

print(decifrar('Sgobp Owdejkugmk', "".join([chr(i) for i in range(1, 3)])))
print(decifrar('Vbtrv Nhxxjjfbpj', "Renzo Nucciiteli"))
