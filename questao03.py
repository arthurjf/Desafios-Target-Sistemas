#   3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#   	• O menor valor de faturamento ocorrido em um dia do mês;
#   	• O maior valor de faturamento ocorrido em um dia do mês;
#   	• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#   
#   IMPORTANTE:
#   	a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#   	b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json
  
file = open('faturas.json')
  
faturas = json.load(file)

faturas.sort(key=lambda x: x['fatura'], reverse=True)

file.close()

#   	• O menor valor de faturamento ocorrido em um dia do mês;
menorFatura = faturas[len(faturas)-1]
print("Menor fatura: {0} no dia {1}".format(menorFatura['fatura'], menorFatura['dia']))

#   	• O maior valor de faturamento ocorrido em um dia do mês;
maiorFatura = faturas[0]
print("Maior fatura: {0} no dia {1}".format(maiorFatura['fatura'], maiorFatura['dia']))

faturaTotal = 0.0
diasFaturados = 0
for tempFatura in faturas:
    faturaValor = float(tempFatura['fatura'])
    if faturaValor > 0:
        faturaTotal += faturaValor
        diasFaturados += 1
mediaFatura = faturaTotal / diasFaturados

#   	• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
diasFaturaAcimaMedia = 0
for tempFatura in faturas:
    faturaValor = float(tempFatura['fatura'])
    if faturaValor > mediaFatura:
        diasFaturaAcimaMedia += 1
    else:
        print("Dias de fatura acima da média mensal: {0}".format(diasFaturaAcimaMedia))
        exit()