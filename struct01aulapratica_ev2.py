class Ficha_aluno:
    def __init__(self, nome, codigo, telefone, email) -> None:
        self.nome = nome
        self.codigo = codigo
        self.telefone = telefone
        self.email = email
        
nome = input("Digite o nome: ")
codigo = input("Digite o codigo: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")

ficha = Ficha_aluno(nome, codigo, telefone, email)


print(f"Nome:{ficha.nome}")
print(f"Codigo:{ficha.codigo}")
print(f"Telefone:{ficha.telefone}")
print(f"Email:{ficha.email}")