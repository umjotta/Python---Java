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
#Esse dicionario 'C' serve só pra dar cor as letras

seg = float(input('Informe um valor em segunos para converter para dia, hora e minuto: '))
print('-=-'*20)
print('MENU ESCOLHA')
print(' [ 1 ] Dia \n [ 2 ] Hora \n [ 3 ] Minutos \n [ 4 ] Todos de uma vez')
print('-=-'*20)
esc = int(input())
sleep(0.7)
print ('{}CONVERTENDO{}...'.format(c['asul'],c['alinpi']))
sleep(1.5)
min = seg//60
hora = seg//(60*60)
dia = seg/(60*60)/24
if esc == 3:
    print(' Min: {}{:.2f}{}'.format(c['asul'], min, c['alinpi']))
elif esc == 2:
    print(' Hora: {}{:.2f}{}'.format(c['asul'], hora, c['alinpi']))
elif esc == 1:
    print(' Dia: {}{:.2f}{}'.format(c['asul'],dia, c['alinpi']))
elif esc == 4:
    print(' Dia: {}{:.2f}{} \n Hora: {}{:.2f}{} \n Min: {}{:.2f}{}'
          .format(c['asul'], dia, c['alinpi'], c['asul'], hora, c['alinpi'], c['asul'], min, c['alinpi']))
#Esse '.format()' é a mesma coisa que colocar o 'F' antes, Só mudei a estetica