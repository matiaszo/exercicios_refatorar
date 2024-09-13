class Imovel_dados:
    def __init__(self, cadastro, iptu, meses_atrasado, multa) -> None:
        self.cadastro = cadastro
        self.iptu = iptu
        self.meses_atrasado = meses_atrasado
        self.multa = multa
        
imoveis = [0,0,0]

for i in range(3):
    cad = input(f"Digite o numero do cadastro do imovel {i + 1}: ")
    iptu = int(input(f"Digite o iptu do imovel {i + 1}: "))
    atraso = int(input(f"Digite a quantidade de meses de atraso do imovel {i + 1}: "))
    
    multa_imovel = 50 * atraso
    
    imovel = Imovel_dados(cad, iptu, atraso, multa_imovel)
    imoveis[i] = imovel
    # print(imoveis[i].cadastro)
    
    
for imovel in imoveis:
    print(f"Cadastro: {imovel.cadastro}")
    print(f"Iptu: {imovel.iptu}")
    print(f"Meses de atraso: {imovel.meses_atrasado}")
    print(f"Multa: {imovel.multa}")
    print()
