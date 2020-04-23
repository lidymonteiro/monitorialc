"""
Estrutura Sequencial
2. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

Valor de teste: 
Entrada: 
4

Saída: 
4 Fahrenheit = -15.56 Celsius

"""

"""
Solução: 
- Entrada - Receber o valor da temperatura em graus Fahrenheit
- Processamento - Converter a temperatura para graus Celsius
- Saída - Exibir a temperatura em graus Celsius (print)
"""

tf = float (input('Informe a temperatura em Fahrenheit: '))
tc = (5 * (tf-32) / 9)
print(f'{tf} Fahrenheit = {tc:.2f} Celsius')