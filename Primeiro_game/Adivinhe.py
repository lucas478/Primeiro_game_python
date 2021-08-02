from random import randint
from time import sleep

def linha():
    print('-=-'*20)
r = 'S'
while r != 'N':
        computador = randint (1, 5)
        print('-------------------------- TENTE ADIVINHAR!--------------------------')
        print('------------------------------- inicio! --------------------------')
        nome = str(input('Digite seu nome aqui: '))
        linha()
        sleep(0.5)
        pensmento = str(input('{} vou pensar em um número inteiro entre 1 e 5. Tente adivinhar... (aperte enter)'.format(nome)))
        linha()
        jogador = int(input('{}, em que número eu pensei?: '.format(nome)))#jogador tenta adivinhar  while jogador not in '1 2 3 4 5':
        linha()
        if jogador == computador:
            print('{} PARABÉNS, você conseguiu me vencer! Raramente isso acontece :-('.format(nome))
            print('-=-'*20)    
        else:
            print('GAME OVER {}. Eu pensei no número {} e não no número {}!'.format(nome, computador, jogador))
            print('-=-'*20)
        r = str(input('{} quer jogar novamente? [S/N]: '.format(nome))).upper()
        while r not in 'SsimSIMSim NnãoNÃO':
            r = str(input('Dado invalido!! [S/N]: ')).strip()
        linha()
        if r == 'N'.upper():
            print('FIM DE JOGO {}!'.format(nome))
print('Volte sempre! ')
