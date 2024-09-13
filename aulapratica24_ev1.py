salario = float(input("Digite o salario: "))

aumento = salario * 0.15
aumento += salario

desconto = aumento* 0.08
desconto = aumento - desconto


print(f"Salario inicial: {salario:5}")
print(f"Salario com aumento: {aumento:5}")
print(f"Salario com desconto: {desconto:5}")


