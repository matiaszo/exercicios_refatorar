import sys

def imc_calc(height, gender):
    
    if gender == 'm':
        value = (72.7 * height) - 58
        return value
    elif gender == 'f':
        value = (62.1 * height) - 44.7
        return value
    else:
        return False



gender = input("Informe seu sexo((M) Masculino ou (F) Feminino)): ").lower()
height = float(input("Informe sua altura (com (.) separando metros de centimetros): "))

ans = imc_calc(height, gender)

if not ans: 
    print("Voce precisa digitar M ou F para o genero")
    sys.exit()
    
print("Resposta: ")
print(f"Seu peso ideal eh de {ans}")

