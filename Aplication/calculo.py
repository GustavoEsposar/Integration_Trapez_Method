from math import *
from decimal import Decimal
import re

class calculos:
     def calcular(a , b , t, c, input):

        # Estruturação da função de entrada
        def f(x):
            input.replace("x", str(x))
            funcao_text = re.sub("|".join(["√", "log10", "log", "π", "sen"]), lambda x: {"log10": "log10", "log": "log", "√": "sqrt", "π": "pi", "sen": "sin"}[x.group()], input)
            return eval(funcao_text)

        # Intervalo de integração
        a2 = float(a)
        b2 = float(b)

        # Número de trapézios
        n = int(t)

        # Número de casas decimais para arredondamento
        ndec = int(c)

        # Cálculo do tamanho de cada subintervalo
        h = (b2-a2)/n

        # Cálculo dos pontos de integração
        x = [a2 + i*h for i in range(n+1)]

        # Cálculo das áreas dos trapézios
        area = sum([f(x[i])+f(x[i+1]) for i in range(n)]) * h / 2

        # Delimitação do erro de arredondamento
        unidadeErro = 0.5 / 10**(ndec)
        erro = unidadeErro * n * h

        # Impressão da tabela
        resposta = "x \t f(x)"
        for i in range(n+1):
            resposta = resposta + "\n" + str(round(x[i], ndec)) + "\t" + str(round(f(x[i]), ndec))

        resposta = resposta + "\n" + "Área Total: " + str(round(area, ndec))
        resposta = resposta + "\n" + "Erro de arredondamento: " + str(round(Decimal(erro), ndec+1))
        return resposta