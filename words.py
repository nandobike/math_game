#!/usr/bin/env python3

import random
import os
import pyttsx3

engine = pyttsx3.init()

word_list = ['they', 'want', 'here', 'me', 'help', 'too',
             'this', 'what', 'play', 'has', 'where', 'look',
             'good', 'who', 'come', 'of', 'out', 'went',
             'our', 'him', 'put', 'got', 'and', 'by',
             'up', 'ball', 'some', 'so', 'us', 'does',
             'the', 'can', 'see', 'like', 'I', 'a',
             'at', 'to', 'am', 'in', 'you', 'on',
             'go', 'not', 'do', 'did', 'my', 'it',
             'had', 'is', 'he', 'are', 'little', 'with',
             'for', 'was', 'she', 'have', 'said', 'we']
random.shuffle(word_list)

# Clearing the Screen
os.system('clear')

print('Juego de Leer Palabras de Blanca\n')

questions = int(input(f'Cuantas palabras (menos que {len(word_list)})? '))
print('')

for i in range(questions):

    a = word_list[i]

    print(f'\n{a}    ', end="")
    _ = input('')
    
    engine.say(a)
    engine.runAndWait()