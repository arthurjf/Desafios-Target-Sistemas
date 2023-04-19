#   4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#   
#   	SP – R$67.836,43
#   	RJ – R$36.678,66
#   	MG – R$29.229,88
#   	ES – R$27.165,48
#   	Outros – R$19.849,53
#   
#   Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

MENSAGEM_FATURAS_MES_ESTADOS = "Segue abaixo as faturas de cada estado no mês:"
MENSAGEM_PERCENTUAL_MES_ESTADOS= "Segue abaixo o percentual de cada estado no mês:"
MENSAGEM_ESTADO_FATURA = "{0}: R$ {1}"
MENSAGEM_ESTADO_PORCENTAGEM_TOTAL = "{0} é {1}% do valor total"
MENSAGEM_FORMATO_PORCENTAGEM = "{:,.2f}"
MENSAGEM_LINHA_DIVISORIA = "=============================================="

class Estado:
    def __init__(self, nome : str, faturamento : float, percentual = 0.0):
        self.__nome = nome
        self.__faturamento = faturamento
        self.__percentual = percentual
    
    def __str__(self):
        return MENSAGEM_ESTADO_FATURA.format(self.__nome, self.__faturamento)
    
    def getNome(self):
        return self.__nome

    def getFaturamento(self):
        return self.__faturamento
    
    def setPercentual(self, percentual : float):
        self.__percentual = percentual

    def getPercentual(self):
        return self.__percentual
    
class Distribuidora:
    def __init__(self, estados):
        self.__estados = estados
        self.atualizarFaturaTotal()
        self.atualizarPercentuais()

    def __str__(self):
        temp = ""
        for estado in self.__estados:
            temp += str(estado) + "\n"
        novoTemp = temp[:-1] 
        return novoTemp
    
    def atualizarFaturaTotal(self):
        self.__faturamentoTotal = 0.0
        for estado in self.__estados:
            self.__faturamentoTotal += estado.getFaturamento()

    def atualizarPercentuais(self):
        for estado in self.__estados:
            porcentagem = (estado.getFaturamento() / self.__faturamentoTotal) * 100
            estado.setPercentual(porcentagem)

    def imprimirPercentuais(self):
        for estado in self.__estados:
            porcentagemMensagem = MENSAGEM_FORMATO_PORCENTAGEM.format(estado.getPercentual())
            print(MENSAGEM_ESTADO_PORCENTAGEM_TOTAL.format(estado.getNome(), porcentagemMensagem))

sp = Estado("SP", 67836.43)
rj = Estado("RJ", 36678.66)
mg = Estado("MG", 29229.88)
es = Estado("ES", 27165.48)
outros = Estado("Outros", 19849.53)

distribuidora = Distribuidora([sp, rj, mg, es, outros])

print("\n" + MENSAGEM_FATURAS_MES_ESTADOS + "\n")

print(distribuidora)

print("\n" + MENSAGEM_PERCENTUAL_MES_ESTADOS + "\n")

distribuidora.imprimirPercentuais()

print("\n" + MENSAGEM_LINHA_DIVISORIA + "\n")