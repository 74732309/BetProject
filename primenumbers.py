y = int(input("enter a number "))
con = 0
for p in range(1,y+1):
    if y % p == 0:
        con += 1
print(f'The number {y} was divisible {con}')  
if con == 2:
    print('this number is prime')  
else:
    print("this number is odd")    



   

    

#para ser primo y tem que ser maior que 1 é divisivel por si proprio e por 1


