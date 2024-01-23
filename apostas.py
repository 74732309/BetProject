from random import sample
import time 

resp = str(input("WELCOME TO LOTOFÁCIL, WOULD YOU LIKE TO PLAY? "))

if resp == 'S' or 's' or 'Sim' or 'SIM':
    print("Okay, wait a few seconds, we are generating your numbers...")
    time.sleep(0.5)
    jogador = sample(range(0, 61), 5)
    print("GOOD GAMES AND MAY LUCK ALWAYS BE IN YOUR FAVOR!")
    print(jogador, end=" ")
else:
    print("Okay, come next time you play!")



