# Dados iniciais
salario_inicial = int (input('Informe o salario inicial: '))  # Salário inicial em reais
taxa_aumento = 0.10  # Taxa de aumento inicial (10%)
anos = 5  # Número de anos

# Cálculo do salário após os anos
salario = salario_inicial
for ano in range(anos):
    salario *= (1 + taxa_aumento)
    taxa_aumento *= 2  # Dobrando a taxa de aumento a cada ano

# Exibição do resultado
print(f"O salário após {anos} anos é: R${salario:.2f}")