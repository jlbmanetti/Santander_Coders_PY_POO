class Fracao:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador

    @staticmethod
    def calcula_mmc(num1, num2):
        maior = max(num1, num2)
        while True:
            if maior % num1 == 0 and maior % num2 == 0:
                return maior
            else:
                maior += 1

    @staticmethod
    def calcula_numerador(mmc, denominador, numerador):
        return (mmc / denominador) * numerador

    # Getters e Setters para numerador
    def get_numerador(self):
        return self.__numerador

    def set_numerador(self, numerador):
        self.__numerador = numerador

    # Getters e Setters para denominador
    def get_denominador(self):
        return self.__denominador

    def set_denominador(self, denominador):
        self.__denominador = denominador

    def soma(self, fracao):
        if self.__denominador == fracao.get_denominador():
            soma = self.__numerador + fracao.get_numerador()
            return f"{soma}/{fracao.get_denominador()}"
        else:
            mmc = Fracao.calcula_mmc(
                self.__denominador, fracao.get_denominador()
            )
            numerador1 = Fracao.calcula_numerador(
                mmc, self.__denominador, self.__numerador
            )
            numerador2 = Fracao.calcula_numerador(
                mmc, fracao.get_denominador(), fracao.get_numerador()
            )
            return f"{numerador1 + numerador2}/{mmc}"

    def subtracao(self, fracao):
        if self.__denominador == fracao.get_denominador():
            subtracao = self.__numerador - fracao.get_numerador()
            return f"{subtracao}/{fracao.get_denominador()}"
        else:
            mmc = Fracao.calcula_mmc(
                self.__denominador, fracao.get_denominador()
            )
            numerador1 = Fracao.calcula_numerador(
                mmc, self.__denominador, self.__numerador
            )
            numerador2 = Fracao.calcula_numerador(
                mmc, fracao.get_denominador(), fracao.get_numerador()
            )
            return f"{numerador1 - numerador2}/{mmc}"

    def multiplicacao(self, fracao):
        numerador = self.__numerador * fracao.get_numerador()
        denominador = self.__denominador * fracao.get_denominador()
        return f"{numerador}/{denominador}"

    def divisao(self, fracao):
        numerador = self.__numerador * fracao.get_denominador()
        denominador = self.__denominador * fracao.get_numerador()
        return f"{numerador}/{denominador}"


print("\n\nUso de getters e setters\n")

fracao1 = Fracao(3, 4)
fracao2 = Fracao(2, 5)

# Exemplo de uso dos getters
print("Numerador da fração 1:", fracao1.get_numerador())
print("Denominador da fração 1:", fracao1.get_denominador())

# Usando os setters para modificar os valores das frações
fracao1.set_numerador(5)
fracao1.set_denominador(8)

# Realizando operações com as frações
resultado_soma = fracao1.soma(fracao2)
resultado_subtracao = fracao1.subtracao(fracao2)
resultado_multiplicacao = fracao1.multiplicacao(fracao2)
resultado_divisao = fracao1.divisao(fracao2)

print("Resultado da soma:", resultado_soma)
print("Resultado da subtração:", resultado_subtracao)
print("Resultado da multiplicação:", resultado_multiplicacao)
print("Resultado da divisão:", resultado_divisao)


# Primeira implementação de decoradores


class Fracao:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador

    @staticmethod
    def calcula_mmc(num1, num2):
        maior = max(num1, num2)
        while True:
            if maior % num1 == 0 and maior % num2 == 0:
                return maior
            else:
                maior += 1

    @staticmethod
    def calcula_numerador(mmc, denominador, numerador):
        return (mmc / denominador) * numerador

    # Getters e Setters para numerador
    @property
    def numerador(self):
        return self.__numerador

    @numerador.setter
    def numerador(self, numerador):
        self.__numerador = numerador

    # Getters e Setters para denominador
    @property
    def denominador(self):
        return self.__denominador

    @denominador.setter
    def denominador(self, denominador):
        self.__denominador = denominador

    def soma(self, fracao):
        if self.__denominador == fracao.denominador:
            soma = self.__numerador + fracao.numerador
            return f"{soma}/{fracao.denominador}"
        else:
            mmc = Fracao.calcula_mmc(self.__denominador, fracao.denominador)
            numerador1 = Fracao.calcula_numerador(
                mmc, self.__denominador, self.__numerador
            )
            numerador2 = Fracao.calcula_numerador(
                mmc, fracao.denominador, fracao.numerador
            )
            return f"{numerador1 + numerador2}/{mmc}"

    def subtracao(self, fracao):
        if self.__denominador == fracao.denominador:
            subtracao = self.__numerador - fracao.numerador
            return f"{subtracao}/{fracao.denominador}"
        else:
            mmc = Fracao.calcula_mmc(self.__denominador, fracao.denominador)
            numerador1 = Fracao.calcula_numerador(
                mmc, self.__denominador, self.__numerador
            )
            numerador2 = Fracao.calcula_numerador(
                mmc, fracao.denominador, fracao.numerador
            )
            return f"{numerador1 - numerador2}/{mmc}"

    def multiplicacao(self, fracao):
        numerador = self.__numerador * fracao.numerador
        denominador = self.__denominador * fracao.denominador
        return f"{numerador}/{denominador}"

    def divisao(self, fracao):
        numerador = self.__numerador * fracao.denominador
        denominador = self.__denominador * fracao.numerador
        return f"{numerador}/{denominador}"


print("\n\nCom uso de decoradores\n")

fracao1 = Fracao(3, 4)
fracao2 = Fracao(2, 5)

# Exemplo de uso dos getters
print("Numerador da fração 1:", fracao1.numerador)
print("Denominador da fração 1:", fracao1.denominador)

# Usando os setters para modificar os valores das frações
fracao1.numerador = 5
fracao1.denominador = 8

# Realizando operações com as frações
resultado_soma = fracao1.soma(fracao2)
resultado_subtracao = fracao1.subtracao(fracao2)
resultado_multiplicacao = fracao1.multiplicacao(fracao2)
resultado_divisao = fracao1.divisao(fracao2)

print("Resultado da soma:", resultado_soma)
print("Resultado da subtração:", resultado_subtracao)
print("Resultado da multiplicação:", resultado_multiplicacao)
print("Resultado da divisão:", resultado_divisao)


# Usando a função property


class Fracao:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador

    @staticmethod
    def calcula_mmc(num1, num2):
        maior = max(num1, num2)
        while True:
            if maior % num1 == 0 and maior % num2 == 0:
                return maior
            else:
                maior += 1

    @staticmethod
    def calcula_numerador(mmc, denominador, numerador):
        return (mmc / denominador) * numerador

    # Getters e Setters para numerador
    def get_numerador(self):
        return self.__numerador

    def set_numerador(self, numerador):
        self.__numerador = numerador

    # Getters e Setters para denominador
    def get_denominador(self):
        return self.__denominador

    def set_denominador(self, denominador):
        self.__denominador = denominador

    def soma(self, fracao):
        if self.__denominador == fracao.denominador:
            soma = self.__numerador + fracao.numerador
            return f"{soma}/{fracao.denominador}"
        else:
            mmc = Fracao.calcula_mmc(self.__denominador, fracao.denominador)
            numerador1 = Fracao.calcula_numerador(
                mmc, self.__denominador, self.__numerador
            )
            numerador2 = Fracao.calcula_numerador(
                mmc, fracao.denominador, fracao.numerador
            )
            return f"{numerador1 + numerador2}/{mmc}"

    def subtracao(self, fracao):
        if self.__denominador == fracao.denominador:
            subtracao = self.__numerador - fracao.numerador
            return f"{subtracao}/{fracao.denominador}"
        else:
            mmc = Fracao.calcula_mmc(self.__denominador, fracao.denominador)
            numerador1 = Fracao.calcula_numerador(
                mmc, self.__denominador, self.__numerador
            )
            numerador2 = Fracao.calcula_numerador(
                mmc, fracao.denominador, fracao.numerador
            )
            return f"{numerador1 - numerador2}/{mmc}"

    def multiplicacao(self, fracao):
        numerador = self.__numerador * fracao.numerador
        denominador = self.__denominador * fracao.denominador
        return f"{numerador}/{denominador}"

    def divisao(self, fracao):
        numerador = self.__numerador * fracao.denominador
        denominador = self.__denominador * fracao.numerador
        return f"{numerador}/{denominador}"

    numerador = property(get_numerador, set_numerador)
    denominador = property(get_denominador, set_denominador)


print("\n\nCom função property\n")
fracao1 = Fracao(3, 4)
fracao2 = Fracao(2, 5)

# Exemplo de uso dos getters
print("Numerador da fração 1:", fracao1.numerador)
print("Denominador da fração 1:", fracao1.denominador)

# Usando os setters para modificar os valores das frações
fracao1.numerador = 5
fracao1.denominador = 8

# Realizando operações com as frações
resultado_soma = fracao1.soma(fracao2)
resultado_subtracao = fracao1.subtracao(fracao2)
resultado_multiplicacao = fracao1.multiplicacao(fracao2)
resultado_divisao = fracao1.divisao(fracao2)

print("Resultado da soma:", resultado_soma)
print("Resultado da subtração:", resultado_subtracao)
print("Resultado da multiplicação:", resultado_multiplicacao)
print("Resultado da divisão:", resultado_divisao)