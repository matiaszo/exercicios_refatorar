peso = float(input("Digite o seu peso: "))

maior = peso * 0.15
maior += peso

menor = peso * 0.20
menor = peso - menor

print(f"Seu peso: {peso:5}")
print(f"Seu peso mais 15%: {maior:5}")
print(f"Seu peso menos 20%: {menor:5}")