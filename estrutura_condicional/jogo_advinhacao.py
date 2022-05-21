#028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário descobrir
# qual foi o número escolhido pelo computador. 
# -O programa deverá escrever na tela se o usuário venceu ou perdeu. 
from random import randint
from time import sleep

print('#Bem vindo ao joguinho da advinhação#')
computador = randint(0,5)
print('Estou pensando um número entre 0 e 5..')
sleep(2)
humano = int(input('Qual foi o númereo que eu pensei? '))
if (computador == humano):
    print(f'Parabéns, você acertou!')
    print(f'Eu tinha pensado no número {computador}')
else :
    print(f'Errou!!!\n Eu pensei no número {computador}')