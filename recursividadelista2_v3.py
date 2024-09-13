def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return factorial(n - 1) * n


number = int(input("Digite um numero inteiro positivo: "))
ans = factorial(number)

print(f"Fatorial de {number} = {ans}")