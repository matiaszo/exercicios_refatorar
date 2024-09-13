import sys

def sum(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b



while True:
    op = input("Digite qual operacao deseja realizar\n S - SOMA / U - SUBTRACAO / X - MULTIPLICACAO / D - DIVISAO\nOu digite # para sair do sistema: ")
    
    if op == "#":
        print("Saindo do sistema")
        sys.exit()
    
    op = op.lower()
    
    a = int(input("Digite o primeiro numero: "))
    b = int(input("Digite o segundo numero: "))
    
    if op == "s":
        print(f"Resposta de {a} + {b} = {sum(a,b)}")
    elif op == "u":
        print(f"Resposta de {a} - {b} = {subtraction(a,b)}")
    elif op == "x":
        print(f"Resposta de {a} * {b} = {multiplication(a,b)}")
    elif op == "d":
        print(f"Resposta de {a} / {b} = {division(a,b):.3}")
    else:
        print("Voce precisa digitar uma das letras especificadas")
        
    print()

    