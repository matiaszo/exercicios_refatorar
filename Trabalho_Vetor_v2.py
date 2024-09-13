presidentes = [0,0,0]

while True:
    vote = input("Digite S para ou N para sair: ").lower()
    
    if vote == "n":
        break
    
    number = int(input("Digite o numero do seu candidato (0 a 2): "))
    presidentes[number] += 1
    print(f"Seu voto no candidato {number} foi contabilizado!")
    
    
biggest = 0
for i in presidentes:
    if i > biggest:
        biggest = presidentes.index(i)
        
print(f"O candidato {biggest} ganhou!")