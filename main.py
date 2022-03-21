HT = float(input("Quantidade de horas trabalhadas no mês: "))
VH = float(input("Valor da hora trabalhada: "))
PD = float(input("Qual o percentual de desconto: "))
salarioBruto = HT*VH
Desconto = (PD/100)*salarioBruto
liquido = salarioBruto - Desconto
print(" As horas trabalhadas são {},\n salario bruto é {},\n total de desconto {}\n e salario liquido {}".format(HT, salarioBruto, Desconto, liquido))