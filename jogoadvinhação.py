import random
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Será que voce consegue acertar qual foi?')
x = int(input('Qual é o seu palpite: '))
y = random.randint(0,10)
while x != y:
    if y > x:
       print('Mais ... Tente mais uma vez...')
       x = int(input('Qual o seu palpite? '))
    else:
       print('Menos ... Tente mais uma vez...')
       x = int(input('Qual o seu palpite? '))
print("Parabens voce acertou!!!")

    