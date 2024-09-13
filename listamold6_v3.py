def calc(s,m,l):
    s*= 10
    m *= 12
    l*= 15
    return s + m + l


print("Loja de camisetas")

user_name = input("Digite o seu nome: ")

small = int(input("Digite a quantidade de camisetas pequenas: "))
medium = int(input("Digite a quantidade de camisetas medias: "))
large = int(input("Digite a quantidade de camisetas grandes: "))


ans = calc(small,medium,large)

print(f"{user_name}, o valor arrecadado foi de = {ans}")