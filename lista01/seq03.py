"""
Estrutura Sequencial
3. Faça um programa para uma loja de tintas. O programa deverá pedir o
tamanho em metros quadrados da área a ser pintada. Considere que a
cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
quantidades de latas de tinta a serem compradas e o preço total.

Valor de teste: 
Entrada: 
200

Saída: 
Latas = 4
Preço total = R$ 320

"""

"""
Solução: 
- Entrada - Receber o valor da área ser pintada em metros quadrados
- Processamento
    1. Separar os dados fornecidos pelo problema que serão úteis no cálculo
    2. Calcular quantos litros de tinta são necessários para pintar a área
    3. Calcular quantas latas de tintas precisa comprar
    4. Calcular o valor a ser pago pelas latas de tinta
- Saída - Exibir a quantidade de latas e o preço total
"""

metros = float(input('Informe a área a ser pintada(m²): '))

rendimento_litro = 3 
preco_lata = 80.0
capacidade_lata = 18

litros = metros / rendimento_litro 

'''
Ao calcular a quantidade de latas precisaremos arredondar para cima caso a quantidade de latas não
for um valor inteiro. Exemplo: Se for necessário 3.5 latas para pintar, precisaremos comprar 4 latas. 
Utilizaremos o método ceil da biblioteca math para isso, caso o valor a ser arrendado não for do tipo 
float ceil() retorna o valor integral.  Saiba mais em: https://docs.python.org/3/library/math.html#math.ceil
'''

from math import ceil
latas = litros / capacidade_lata
latas = ceil(latas)

preco_total = latas * preco_lata

print(f'Latas = {latas}')
print(f'Preço total = R$ {preco_total:.2f}')
