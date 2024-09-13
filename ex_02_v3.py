def calculate(a, b):
    sum = a + b
    mult = a * b

    return sum, mult

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

result_sum = calculate(a, b)[0]
result_mult = calculate(a,b)[1]

print(f"The sum of the two numbers is: {result_sum}")
print(f"The multiplication of the two numbers is: {result_mult}")