#Projeto PY POO - João Manetti

## Descrição:
### Implementar uma aplicação para uma Farmácia que vende produtos através de e-commerce.

## Instruções:
### Como Banco de dados temporário para armazenar os dados sugerimos listas ou dicionários (o que for mais simples de implementar).
### 5 classes obrigatórias no seu projeto: Clientes, Medicamentos Quimioterápicos, Medicamentos Fitoterápicos, Laboratórios e Vendas

## Funcionalidades:
### *Descritas com comentário em cada classe

class Clientes: #classe obrigatória
    base_c = [[9000000001,"nome1","da/ta/nasc1"],[9000000002,"nome2","da/ta/nasc2"],[9000000003,"nome3","da/ta/nasc3"]] #base em forma de lista

    def __init__(self, cpf:int, nome:str, data_nasc:str):
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc
    
    @classmethod
    def search(cls, cpfs:int):
        cpfs=int(cpfs)
        n = 0
        i = 0
        while i < len(cls.base_c) and n == 0:
                if cpfs == cls.base_c[i][0]:
                    print("\nCliente encontrado: \n"+f"CPF - {cls.base_c[i][0]}"+"\n"+f"NOME - {cls.base_c[i][1]}"+"\n"+f"DATA NASC. - {cls.base_c[i][2]}")
                    n +=1
                i +=1       
        if n == 0:
            print(f"Cliente com CPF {cpfs} não foi encontrado")

    def adicionar(cls, self):
        cls.base_c.append([self.cpf,self.nome,self.data_nasc])

class Medicamentos: #classe auxiliar superior
    base_mf = [["med1f", "comp1f", "lab1f", "desc1f", False], ["med2", "comp2", "lab2", "desc2f", False], ["med3f", "comp3f", "lab3f", "descf3", False]]
    base_mq = [["med1q", "comp1q", "lab1q", "desc1q", False], ["med2", "comp2", "lab2", "desc2q", False], ["med3q", "comp3q", "lab3q", "desc3q", True]]

    def __init__(self, nome:str, princ_comp:str, lab:str, desc:str, receita=False):
        self.nome = nome
        self.princ_comp = princ_comp
        self.lab = lab
        self.desc = desc
        self.receita = receita

    def adicionar_quimioterapico(cls, self):
        cls.base_mq.append([self.nome, self.princ_comp, self.lab, self.desc, self.receita])

    def adicionar_fitoterapico(cls, self):
        cls.base_mf.append([self.nome, self.princ_comp, self.lab, self.desc, self.receita])

class Med_Qui(Medicamentos): #classe obrigatória
    pass

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
        print("\nMENU - Cadastro de clientes: \n[1] - Consulta por CPF")
        b = int(input("Insira a opção: "))
        if b == 1:
            cpfs = input("\nDigite o CPF: ")
            Clientes.search(cpfs)
#        elif b == 2:
#            print("entrou menu 2")
        else:
            print("Incorrect value")
    elif a == 2:
        print("\nMENU - Cadastro de medicamentos: \n[1] - Consulta por NOME \n[2] - Consulta por FABRICANTE \n[3] - Consulta por DESCRIÇÃO")
        c = int(input("Insira a opção: "))
        if c == 1:
            cpfs = input("\nDigite o NOME: ")
            Clientes.search(cpfs)
#        elif c == 2:
#            print("entrou menu 2")
#        elif c == 3:
#            print("entrou menu 3")
        else:
            print("Incorrect value")
    elif a == 3:
        print("entrou menu 3")
    elif a == 4:
        print("entrou menu 4")
    elif a == 9:
        print("Você saiu... \n")
        i=0
    else:
        print("Valor incorreto... Tente novamente.")

