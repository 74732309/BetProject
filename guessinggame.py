import random
print('I'm your computer...')
print('I just thought of a number between 0 and 10.')
print('Can you guess which one it was?')
x = int(input('What is your guess: '))
y = random.randint(0,10)
while x != y:
     if y > x:
        print('More... Try again...')
        x = int(input('What's your guess? '))
     else:
        print('Less... Try again...')
        x = int(input('What's your guess? '))
print("Congratulations, you got it right!!!")
    
