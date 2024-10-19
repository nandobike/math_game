import random
import os

# Clearing the Screen
os.system('clear')

score = 0

print('Juego de Matematicas de Blanca\n')

maxn = int(input('Maximo numero? '))
questions = int(input('Cuantas preguntas? '))

operations_list = ['+', '-']
print('')

for i in range(questions):

    a = random.randrange(0, maxn+1, 1)
    b = random.randrange(0, maxn+1, 1)

    operation = random.choice(operations_list)

    if (operation == '-') & (a < b): #Avoid negative numbers as a result
        a, b = b, a

    while True: #Handle exceptions such as empty input or letters
        try:
            user_entered = input(f'{a} {operation} {b} = ')
            m = int(user_entered)
            break
        except ValueError:
            print('   Ups! Ese no es un numero') 

    if (m == (a+b)) & (operation == '+') ^ (m == (a-b)) & (operation == '-'):
        print('   Si! Correcto.')
        score += 1
    else:
        print('   No.')

print(f'\nPUNTAJE FINAL = {score}/{questions} ({score/questions*100:.0f}%)')