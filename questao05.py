#   5) Escreva um programa que inverta os caracteres de um string.
#   
#   IMPORTANTE:
#   	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#   	b) Evite usar funções prontas, como, por exemplo, reverse;

textoEntrada = input("Digite um texto: ")

textoInvertido = ""
for i in range(len(textoEntrada) - 1, -1, -1):
    textoInvertido += textoEntrada[i]

print("Seu texto invertido: {0}".format(textoInvertido))