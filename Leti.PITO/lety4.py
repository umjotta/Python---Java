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

km = float(input(' KMs rodados:{} '.format(c['vermei'])))
sleep(0.6)
print('{}ANALISANDO...{}'.format(c['asul'],c['alinpi']))
sleep(1)
diaria = 90
if km > 100:
    taxa = (km-100) * 12 + 90
    print (' {}Valor sofrera reajuste de kms rodados{}'.format(c['vermei'],c['alinpi']))
    sleep(0.6)
    print('{}CALCULANDO NOVO VALOR...{}'.format(c['asul'],c['alinpi']))
    sleep(1)
    print('Pagamento: {}{:.2f}R${}'.format(c['vermei'],  taxa, c['alinpi']))
else:
    print('Pagamento: {}90R${}'.format(c['verdinha'], c['alinpi']))
print (' {}OBRIADO POR CONTRATAR NOSSA COMPAINHA!!!{}'.format(c['amarrelo'],c['alinpi']))