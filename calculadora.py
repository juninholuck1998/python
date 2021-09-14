resposta1 = input('Digite um número: ')
resposta2 = input('Digite um número: ')
resposta3 = input('Digite um operador: ')

if resposta1.isnumeric() and resposta2.isnumeric():
    resposta1 = int(resposta1)
    resposta2 = int(resposta2)
    if resposta3 == '+' :
        print(resposta1 + resposta2)
    elif resposta3 == '-' :
        print(resposta1 - resposta2)
    elif resposta3 == '*' :
        print(resposta1 * resposta2)
    elif resposta3 == '/' :
        print(resposta1 / resposta2)
    else:
        print('Por favor digite um operador válido.')
else:
    print('Por favor digite um número válido')