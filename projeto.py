#Projeto PY POO - João Manetti

## Descrição:
### Implementar uma aplicação para uma Farmácia que vende produtos através de e-commerce.

## Instruções:
### Como Banco de dados temporário para armazenar os dados sugerimos listas ou dicionários (o que for mais simples de implementar).
### 5 classes obrigatórias no seu projeto: Clientes, Medicamentos Quimioterápicos, Medicamentos Fitoterápicos, Laboratórios e Vendas

## Funcionalidades:
### *Descritas com comentário em cada classe

class Clientes: #classe obrigatória
    base = [[9000000001,"nome1","data_nasc1"],[9000000002,"nome2","data_nasc2"],[9000000003,"nome3","data_nasc3"]] #base em forma de lista

    def __init__(self, cpf:int, nome:str, data_nasc:str):
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc
    
    @classmethod
    def search(cls, cpfs:int):
        for i in len(cls.base):
            if cpfs == cls.base[i-1][0]:
                print("Cliente encontrado: \n"+f"CPF - {cls.base[i-1][0]}"+"\n"+f"NOME - {cls.base[i-1][1]}"+"\n"+f"DATA NASC. - {cls.base[i-1][2]}")
            else:
                print("Usuário não encontrado")

    def adicionar(cls, self):
        cls.base.append([self.cpf,self.nome,self.data_nasc])

class Medicamentos: #classe auxiliar superior
    def __init__(self, nome:str, princ_comp:str, lab:str, desc:str, receita=False):
        self.nome = nome
        self.princ_comp = princ_comp
        self.lab = lab
        self.desc = desc
        self.receita = receita

class Med_Qui(Medicamentos): #classe obrigatória
    pass

#q1 = Med_Qui('medqui1','comp1','lab1','desc1')
#q2 = Med_Qui('medqui2','comp2','lab2','desc2',True)

#print(q1.receita)
#print(q2.receita)

class Med_Fit(Medicamentos): #classe obrigatória
    pass
      
class Lab: #classe obrigatória
    def __init__(self, nome:str, end:str, tel:str, cid:str, est:str):
        self.nome = nome
        self.end = end
        self.tel = tel
        self.cid = cid
        self.est = est
        
class Vendas: #classe obrigatória
    def __init__(self, datahora:str, prod:str, cliente, valor:str):
        self.datahora = datahora
        self.prod = prod
        self.cliente = cliente
        self.valor = valor


i = 1
while i != 0:

    print("\nMENU: \n[1] - Cadastro de clientes \n[2] - Cadastro de medicamentos \n[3] - Efetuar venda \n[4] - Emissão de relatório \n[9] - Sair do menu")
    a = int(input("Insira a opção: "))

    if a == 1:
        print("\nMENU - [1]: \n[1] - Consulta por CPF")
        b = int(input("Insira a opção: "))
        if b == 1:
            cpfs = input("\nDigite o CPF: ")
            print(Clientes.search(cpfs))
#        elif b == 2:
#            print("entrou menu 2")
#        elif b == 3:
#            print("entrou menu 3")
#        elif b == 4:
#            print("entrou menu 4")
#        elif b == 9:
#            print("Você saiu... ")
#            break
        else:
            print("Incorrect value")
    elif a == 2:
        print("entrou menu 2")
    elif a == 3:
        print("entrou menu 3")
    elif a == 4:
        print("entrou menu 4")
    elif a == 9:
        print("Você saiu... ")
        break
    else:
        print("Valor incorreto")

