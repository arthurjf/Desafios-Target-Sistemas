#   4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#   
#   	SP – R$67.836,43
#   	RJ – R$36.678,66
#   	MG – R$29.229,88
#   	ES – R$27.165,48
#   	Outros – R$19.849,53
#   
#   Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

faturamentlMensalEstados = [["SP", 67836.43], ["RJ", 36678.66], ["MG", 29229.88], ["ES", 27165.48], ["Outros", 19849.53]]

print("Segue abaixo as faturas de cada estado do mês:")

faturaTotal = 0.0
for tempFatura in faturamentlMensalEstados:
    dinheiroFormatado = "${:,.2f}".format(tempFatura[1])
    print("{0}: R$ {1}".format(tempFatura[0], dinheiroFormatado))
    fatura = tempFatura[1]
    faturaTotal += fatura

print("")

for tempFatura in faturamentlMensalEstados:
    faturaVez = tempFatura[1]
    porcentagemVez = (faturaVez / faturaTotal) * 100
    porcentagemFormatada = "{:.2f}".format(porcentagemVez)
    print("{0} é {1}% do valor total".format(tempFatura[0], porcentagemFormatada))

print("")