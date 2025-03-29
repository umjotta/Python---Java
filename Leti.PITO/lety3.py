from time import sleep
c = {'esp':' '*15,
     'sep':'-=-'*15,
    'vermei':'\033[31m',
    'verdinha':'\033[32m',
    'amarrelo':'\033[33m',
    'asul':'\033[34m',
    'rocxu':'\033[36m',
    'negralhada':'\033[1m',
    'alinpi':'\033[m'
}
valor = float(input('Informe o valor da compra: R$ '))
sleep(0.6)
print('{}VERIFICANDO TARIFA DE IMPOSTO...{}'.format(c['rocxu'],c['alinpi']))
sleep(1)
if valor <= 500.00:
    print('{}Você não sofrera imposto{}'.format(c['amarrelo'],c['alinpi']))
else:
    impost = (valor-500) * (50/100) + valor
    print('{}Você sofreu imposto{}'.format(c['vermei'],c['alinpi']))
    sleep(0.5)
    print ('Novo preço: {}{:.2f}{}'.format(c['asul'], impost, c['alinpi']))