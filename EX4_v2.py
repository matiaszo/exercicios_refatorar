rows = int(input("Digite a quantidade de linhas da matriz: "))
cols = int(input("Digite a quantidade de colunas da matriz: "))

ans = 0
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        ans += j
    
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(f"{j}\t", end= "")  
    print()  
    
print(f"O resultado da soma da matriz eh de: {ans}")
        