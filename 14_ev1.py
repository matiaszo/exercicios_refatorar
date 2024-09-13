import math

def calculate_area(radius):
    ans = (pow(radius, 2)) * math.pi
    return ans

radius = float(input("Digite o raio do circulo: "))

area = calculate_area(radius)

print(f"A area do circulo eh de: {area:.5} [U.M]")
