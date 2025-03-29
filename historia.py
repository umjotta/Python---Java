nome = input('Qual o nome do Heroi: ')
idade = int(input('Idade do Heroi: '))
poder = input('Poder do Heroi: ')
combate = input('Estilo de combate: ')
mestre = input('Nome do Mestre: ')
nome_he = input ('Nome de Heroi(Apelido): ')
sus1 = input('Apelido do suspeito 1: ')
sus2 = input ('Apelido do suspeito 2: ')
print ('''
       O aprendiz {} estava em seu 4° ano de treinamento com seu mestre {}, o Mestre Kid tinha um exelente dominio na arte de dominação do gelo!
       todos os dias era desafiado por varios especialistas renomados.. por isso ele enviou seu aorendiz de codinome {} que acabara de completar {} em uma missão para caçar os suspeitos que o ameaçam constantemente:  
        {} e {} (Tinham bastante inveja do Mestre {}) seu aprendiz {} sai em caçada para realizar a missão que seu mestre {} o designou ... '''
       .format(nome,mestre, nome_he, idade, sus1, sus2, mestre, nome_he, mestre))
