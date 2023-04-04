#   3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#   	• O menor valor de faturamento ocorrido em um dia do mês;
#   	• O maior valor de faturamento ocorrido em um dia do mês;
#   	• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#   
#   IMPORTANTE:
#   	a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#   	b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def carregarJson(nomeArquivo):
  with open(nomeArquivo) as arquivoJson:
      faturamentos = json.load(arquivoJson)
      faturamentos.sort(key=lambda x: x['valor'], reverse=True)
      return faturamentos
  
def getMediaFaturamentoMeses(faturas):
    faturaTotal = 0.0
    diasFaturados = 0
    for tempFatura in faturas:
        faturaValor = float(tempFatura['valor'])
        if faturaValor > 0:
            faturaTotal += faturaValor
            diasFaturados += 1
    mediaFatura = faturaTotal / diasFaturados
    return mediaFatura

def getNumeroDiasFaturamentoAcimaMedia(faturas, mediaFaturamento):
    diasFaturaAcimaMedia = 0
    for tempFatura in faturas:
        faturaValor = float(tempFatura['valor'])
        if faturaValor > mediaFaturamento:
            diasFaturaAcimaMedia += 1
        else:
            return diasFaturaAcimaMedia
    return 0

def getMenorFaturamento(faturas):
    qtdFaturamentos = len(faturamentos) - 1
    return faturas[qtdFaturamentos]

def getMaiorFaturamento(faturas):
    return faturas[0]
  
faturamentos = carregarJson("dados.json")

#   	• O menor valor de faturamento ocorrido em um dia do mês;
menorFatura = getMenorFaturamento(faturamentos)
print("Menor faturamento: {0} no dia {1}".format(menorFatura['valor'], menorFatura['dia']))

#   	• O maior valor de faturamento ocorrido em um dia do mês;
maiorFatura = getMaiorFaturamento(faturamentos)
print("Maior faturamento: {0} no dia {1}".format(maiorFatura['valor'], maiorFatura['dia']))

mediaFatura = getMediaFaturamentoMes(faturamentos)

#   	• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
print("Dias de faturamento acima da média mensal: {0}".format(getNumeroDiasFaturamentoAcimaMedia(faturamentos, mediaFatura)))