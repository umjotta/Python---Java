num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))
maior = 0
menor = 0
if num2 and num3 < num1:
    maior = num1
elif num1 and num3 < num2:
    maior = num2
elif num1 and num2 < num3:
    maior = num3
if num3 and num2 > num1:
    menor = num1
elif num1 and num3 > num2:
    menor = num2
elif num1 and num2 > num3:
    menor = num3   
print (' Maior: {} \n Menor: {}'.format(maior, menor))