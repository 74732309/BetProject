from random import sample
import time 

resp = str(input("BEM VINDO A LOTOFACIL, VOCE GOSTARIA DE JOGAR? "))

if resp == 'S' or 's' or 'Sim' or 'SIM':
    print("Certo, aguarde alguns segundos, estamos gerando seus numeros...")
    time.sleep(0.5)
    jogador = sample(range(0, 61), 5)
    print("BOM JOGOS E QUE A SORTE SEMPRE ESTEJA AO SEU FAVOR!")
    print(jogador, end=" ")
else:
    print("Okay, venha na proxima que voce jogar!")

#tentar aprimorar com while

