y = int(input("Digite um número: "))
con = 0
for p in range(1,y+1):
    if y % p == 0:
        con += 1
print(f'O numero {y} foi divisivel {con}')  
if con == 2:
    print('Esse numero é primo')  
else:
    print("Esse numero nao é primo")    



   

    

#para ser primo y tem que ser maior que 1 é divisivel por si proprio e por 1


