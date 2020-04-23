"""
Estrutura Sequencial
1. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

Valor de teste: 
Entrada: 
10 
9.6 
7 
3.2

Saída: 
Média = 7.45se qu

"""

"""
Solução: 
- Entrada - Receber 4 notas pelo teclado, sendo do tipo float. 
- Processamento - Calcular a média (soma as notas e divide pela quantidade de notas)
- Saída - Exibir a média (print)
"""

nota1 = float(input('Informe a 1a nota: '))
nota2 = float(input('Informe a 2a nota: '))
nota3 = float(input('Informe a 3a nota: '))
nota4 = float(input('Informe a 4a nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'Media = {media}')