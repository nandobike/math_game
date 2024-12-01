#!/usr/bin/env python3

import random
import os
import pyttsx3

engine = pyttsx3.init()



# Clearing the Screen
os.system('clear')

print('Juego de Fry words de Blanca\n')

level = int(input(f'Que nivel (1-10)? '))
print('')


with open('data/frywords.txt', 'r') as f:
    lines = f.readlines()
    line_num = level  # adjust this to the desired line number
    line = lines[line_num].strip()
    word_list = line.split(',')
random.shuffle(word_list)

questions = int(input(f'Cuantas preguntas (1-100)? '))
print('')
#questions = len(word_list)



for i in range(questions):

    a = word_list[i]

    print(f'\n{a}    ', end="")
    _ = input('')
    
    engine.say(a)
    engine.runAndWait()