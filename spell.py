#!/usr/bin/env python3

import random
import os
import pyttsx3

def say_word(word: str):
    """ Say the word """
    engine.say(word) #Say the word
    engine.runAndWait()

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

print('Juego de Deletrear Palabras de Blanca\n')

questions = int(input(f'Cuantas palabras (menos que {len(word_list)})? '))
print('')
score = 0

for i in range(questions):

    a = word_list[i]

    while True:
        say_word(a)

        print(f'\nDeletrea la palabra: ', end="")
        spelled = input('')
        if spelled != '':
            break
    
    if spelled.lower() == a.lower():
        print("Si")
        score += 1
    else:
        print(f'No, la palabra era "{a}".')

    #engine.say(a)
print(f'Puntaje final: {score}/{questions} ({score/questions*100:.1f}%)')