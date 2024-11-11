#!/usr/bin/env python3

import random
import os
import pyttsx3

engine = pyttsx3.init()



def read_random_sentence(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    sentences = [sentence.strip() for sentence in text.split('.') if sentence.strip()]
    random_index = random.randint(0, len(sentences) - 1)
    return sentences[random_index]

file_path = "data/cleaned_merged_fairy_tales_without_eos.txt"



# Clearing the Screen
os.system('clear')

print('Juego de Leer Oraciones de Blanca\n')

n_words = int(input('Cuantas palabras por oracion? '))
questions = int(input('Cuantas oraciones? '))

print('')

for i in range(questions):

    sentence = read_random_sentence(file_path)
    sentence_list = sentence.split(' ')
    sentence_short = sentence_list[:n_words]
    sentence_short_joined = " ".join(sentence_short)


    #a = word_list[i]

    print(f'\n{sentence_short_joined}    ', end="")
    _ = input('')

    
    
    engine.say(sentence_short_joined)
    engine.runAndWait()