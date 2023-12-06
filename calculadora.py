def calculadora():
  x = float(input('Digite um numero para realizar uma operacao : '))
  y = float(input('Digite um numero para realizar uma operacao : '))
  print("As operçãoes disponiveis no momento sao adição(+), subtração(-), divisão(/) e multiplicação(*)")
  operador = input("Digite o 1 operados para realizarmos a sua operação: ")

  if operador == '+':
    print(f"A soma entre {x} e {y} é de {x+y}")
  elif operador == '-':
    print(f"A subtração entre {x} e {y} é {x-y}")
  elif operador == '/':
    print(f"A divisão de {x} e {y} é {x/y}")
  elif operador == '*':
    print(f"A multiplicação de {x} e {y} é de {x*y}")
  else:
    print(" Tente digitar um dos operadores indicados para a operacao, +, -, / ou * :")

calculadora()

