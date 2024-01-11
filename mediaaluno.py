a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
c = float(input('Digite a terceira nota: '))

def func(c):
    nf = (c + b) / 2
    print('A menor nota é a {}'.format(a))
    print('A media é {}'.format(nf))
    x = nf - 5.75
    if x > 5.75: 
            print('Aluno Aprovado.')
    else:
            print('Aluno Reprovado.')

nf = (c + b) / 2
if a < b:
     if a < c:
        nf = (c + b) / 2
        print('A menor nota é a {}'.format(a))
        print('A media é {}'.format(nf))
        x = nf - 5.75
        if x > 5.75: 
            print('Aluno Aprovado.')
        else:
            print('Aluno Reprovado.')

     else:
        nf = (a + b) / 2
        new_func(c)
        print('A media é {}'.format(nf))
        x = nf - 5.75
        if x > 5.75: 
            print('Aluno Aprovado.')
        else:
            print('Aluno Reprovado.')

else:
    if b < c:
        nf = (a + c) / 2
        print('A menor nota é a {}'.format(b))
        print('A media é {}'.format(nf))
        x = nf - 5.75
        if x > 5.75: 
            print('Aluno Aprovado.')
        else:
            print('Aluno Reprovado.')

    else:
        x = nf - 5.75
        if x > 5.75: 
            print('Aluno Aprovado.')
        else:
            print('Aluno Reprovado.')

        nf = (a + b) / 2
        print('A menor nota é a {}'.format(c))
        print('A media é {}'.format(nf))




