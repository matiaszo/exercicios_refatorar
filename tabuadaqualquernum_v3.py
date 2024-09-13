number = int(input("Digite um numero inteiro: "))

print(f"TABUADA DE 1 ATÉ {number}")

for i in range(1, number + 1):
    for j in range(1,11):
        ans = i * j
        print(f"{i} * {j} = {ans}")
    print()
