from random import randint
from time import sleep
from pygame import mixer

mixer.init()
mixer.music.load('fundo.mp3')
mixer.music.play()

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print("-=-" * 6, "BEM VINDO!! JOGUE COMIGO JOKENPO!", "-=-" * 6)
print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador = int(input("Qual a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("-=-" * 10)
print("O jogador jogou {} ".format(itens[jogador]))
print("O computador jogou {} ".format(itens[computador]))

while True:
    if computador == 0:                         #computador jogou pedra
        if jogador == 0:
            print('\033[7mEMPATE')
            mixer.init()
            mixer.music.load('erro.mp3')
            mixer.music.play()
            n1 = str(input(' '))
        elif jogador == 1:
            print("\033[1;32mJOGADOR GANHOU")
            mixer.init()
            mixer.music.load('parabains.mp3')
            mixer.music.play()
            n1 = str(input(' '))
        elif jogador == 2:
            mixer.init()
            mixer.music.load('naruto-sad-music-instant.mp3')
            mixer.music.play()
            print("\033[1;31mCOMPUTADOR GANHOU")
            n1 = str(input(' '))
        elif jogador > 3:
            print('JOGADA INVÁLIDA')

    elif computador == 1:                       #computador jogou papel
        if jogador == 0:
            print('\033[1;31mCOMPUTADOR GANHOU')
            mixer.init()
            mixer.music.load('naruto-sad-music-instant.mp3')
            mixer.music.play()
            n1 = str(input(' '))
        elif jogador == 1:
            print('\033[7mEMPATE')
            mixer.init()
            mixer.music.load('erro.mp3')
            mixer.music.play()
            n1 = str(input(' '))
        elif jogador == 2:
            print('\033[1;32mJOGADOR GANHOU')
            mixer.init()
            mixer.music.load('parabains.mp3')
            mixer.music.play()
            n1 = str(input(' '))
        elif jogador > 3:
            print('JOGADA INVÁLIDA')

    elif computador == 2:                       #computador jogou tesoura
        if jogador == 0:
            print('\033[1;32mJOGADOR GANHOU')
            mixer.init()
            mixer.music.load('parabains.mp3')
            mixer.music.play()
            n1 = str(input(' '))
        elif jogador == 1:
            print('\033[1;31mCOMPUTADOR GANHOU')
            mixer.init()
            mixer.music.load('naruto-sad-music-instant.mp3')
            mixer.music.play()
            n1 = str(input(' '))
        elif jogador == 2:
            print('\033[7mEMPATE')
            mixer.init()
            mixer.music.load('erro.mp3')
            mixer.music.play()
            n1 = str(input(' '))
        elif jogador > 3:
            print('JOGADA INVÁLIDA')

