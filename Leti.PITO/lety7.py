numero = int(input("Digite um número ímpar: "))
if numero % 2 == 0:
    print("O número digitado não é ímpar. Por favor, tente novamente.")
else:
    n_ante = numero - 2
    n_prox = numero + 2
    quad_ante = n_ante ** 2
    quad_prox = n_prox ** 2
    dif = quad_ante - quad_prox
    print('''
          A diferença entre o quadrado do número ímpar anterior ({})
           e do próximo número ímpar ({}) é: {}'''
          .format(n_ante,n_prox,dif))
