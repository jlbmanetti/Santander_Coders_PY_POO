#Projeto PY POO - João Manetti

## Descrição:
### Implementar uma aplicação para uma Farmácia que vende produtos através de e-commerce.

## Instruções:
### Como Banco de dados temporário para armazenar os dados sugerimos listas ou dicionários (o que for mais simples de implementar).
### 5 classes obrigatórias no seu projeto: Clientes, Medicamentos Quimioterápicos, Medicamentos Fitoterápicos, Laboratórios e Vendas

## Funcionalidades:
### *Descritas com comentário em cada classe





class Clientes: #classe obrigatória
    base = [] #base em forma de lista

    def __init__(self,cpf,nome,data_nasc):
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc

    def add(self):
        Clientes.base.append(self)

a = Clientes(1111,'str','11/02')
a.add()
print(Clientes.base)


class Medicamentos: #classe auxiliar superior
    def __init__(self,nome, princ_comp,lab,desc,receita=False):
        self.nome = nome
        self.princ_comp = princ_comp
        self.lab = lab
        self.desc = desc
        self.receita = receita

class Med_Qui(Medicamentos): #classe obrigatória
    pass

q1 = Med_Qui('medqui1','comp1','lab1','desc1')
q2 = Med_Qui('medqui2','comp2','lab2','desc2',True)

print(q1.receita)
print(q2.receita)

class Med_Fit(Medicamentos): #classe obrigatória
    pass
      
class Lab: #classe obrigatória
    def __init__(self,nome,end,tel,cid,est):
        self.nome = nome
        self.end = end
        self.tel = tel
        self.cid = cid
        self.est = est
        
class Vendas: #classe obrigatória
    def __init__(self,datahora,prod,cliente,valor):
        self.datahora = datahora
        self.prod = prod
        self.cliente = cliente
        self.valor = valor

