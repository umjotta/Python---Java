sala = int(input('Quantidade de sala: '))
alun = int(input('Quanidade total de alunos: '))
media = alun/sala
print('Alguma sala tem mais de 40 Alunos?')
print(' [ 1 ] SIM \n [ 2 ] NÃO')
qua = int(input())
print ('A media de lunos é {}'.format(media))
if qua == 1:
    print('Existe sala com quantidade superior a 40 alunos')
elif qua == 2:
    print ('Obrigrado por verificar')