#  2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#  IMPORTANTE: 
#  Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

TEXTO_PERTENCE_SEQUENCIA = "O número {0} PERTENCE a sequência Fibonacci"
TEXTO_NAO_PERTENCE_SEQUENCIA = "O número {0} NÃO pertence a sequência Fibonacci"

def numeroPertenceFibonacci(numero):
    if numero == 0 or numero == 1:
        return True
    ultimo = 0
    anterior = 1
    while numero > anterior:
        temp = ultimo
        ultimo = anterior
        anterior = temp + anterior
        if(anterior == numero):
            return True
    return False

usuarioNumero = int(input("Digite um número: "))
    
if(numeroPertenceFibonacci(usuarioNumero)):
    print(TEXTO_PERTENCE_SEQUENCIA.format(usuarioNumero))
else:
    print(TEXTO_NAO_PERTENCE_SEQUENCIA.format(usuarioNumero))