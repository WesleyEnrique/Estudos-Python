'''Crie um algoritmo que receba um número, conte o número total de dígitos e mostre o resultado.
Por exemplo, se o número é 2021 , então a saída deve ser 4'''

print('\t ----Contagem dos dígitos---- ')
digitos = int(input("Digite um número para contar seus dígitos : "))
contador = 0
while digitos != 0:
    digitos //= 10
    contador+= 1
print("Total de dígitos = ", contador)