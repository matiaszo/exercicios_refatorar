class Ficha_candidato:
    def __init__(self, codigo, salario, email) -> None:
        self.codigo = codigo
        self.salario = salario
        self.email = email
        
candidatos = [0,0,0]

for i in range(3):
    codigo = input(f"Digite o codigo do candidato {i + 1}: ")
    salario = int(input(f"Digite o salario do candidato {i + 1}: "))
    email = int(input(f"Digite o email do candidato {i + 1}: "))
    
    candidato = Ficha_candidato(codigo, salario, email)  
    candidatos[i] = candidato  
    
for candidato in candidatos:
    print(f"Codigo do candidato: {candidato.codigo}")
    print(f"Salario do candidato: {candidato.salario}")
    print(f"Email do candidato: {candidato.email}")
    print()
