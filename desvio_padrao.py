'''
# disponibilidade com ataque = 90.62,94.08
# disponibilidade sem ataque = 100,100
dados = [100,100]
d = []
# media dos dados da lista
media = sum(dados)/len(dados)
# coeficiente de variacao dos dados da lista
for i in dados:
    v = i-media
    d.append(v)
# variancia dos dados da lista
variancia = sum([i ** 2 for i in d]) / len(d)
# desvio padrao dos dados da lista
desvio_padrao = variancia ** 0.5

# escreva o valor de desvio_padrao no arquivo desvio_dos_dados.txt
with open('desvio.txt', 'a') as desvio:
    desvio.write(str(desvio_padrao) + '\n') 
'''

import math

# disponibilidade com ataque = 90.62,94.08
# dados = [90.62,94.08]
# disponibilidade sem ataque = 100,100
# dados = [100,100]
# tempo de resposta com ataque = 1.64,2.07
# dados = [1.64,2.07]
# tempo de resposta sem ataque = 0.33,0.01
# dados = [0.33,0.01]
# tempo de resposta mais longa com ataque = 83.76, 77.06
# dados = [83.76, 77.06]
# tempo de resposta mais longa sem ataque = 1.38,0.12
# dados = [1.38,0.12]


# Calculando a média dos dados da lista
media = sum(dados) / len(dados)

# Calculando o desvio padrão dos dados da lista
desvio_padrao = math.sqrt(sum([(x - media) ** 2 for x in dados]) / (len(dados) - 1))

# Escrevendo o valor de desvio_padrao no arquivo desvio_dos_dados.txt
with open('valor_desvio.txt', 'a') as desvio:
    desvio.write(str(desvio_padrao) + '\n')
