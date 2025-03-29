def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
def gerar_primos(quantidade):
    primos = []
    numero = 2
    while len(primos) < quantidade:
        if eh_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

# Gerar os 100 primeiros números primos
primos = gerar_primos(100)
print(primos)
