""" from math import sqrt, ceil, floor

num = float(input('Digite um número\n'))

print('O número arredondado é {}'.format(floor(num))) """

""" import random

al1 = str(input('Aluno 1: \n'))
al2 = str(input('Aluno 2: \n'))
al3 = str(input('Aluno 3: \n'))
al4 = str(input('Aluno 4: \n'))

array = [al1, al2, al3, al4]

random.shuffle(array)

print('A ordem vai ser: {}'.format(array)) """

import vlc
import time

mp3 = vlc.MediaPlayer('C:/Users/gzrei/Documents/PROGRAMACAO/PYTHON/Aprendendo/Guanabara/playthis.mp3')
mp3.play()
time.sleep(5)
mp3.stop()

