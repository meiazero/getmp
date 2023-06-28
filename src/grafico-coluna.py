import matplotlib.pyplot as plt

# Valores das barras
valores = [100, 90.62]

# Rótulos das barras
labels = ['100%', '90.62%']

# Desvio padrão
desvio_padrao = [0, 2.446]

# Configuração do gráfico
plt.bar(labels, valores)

# Legenda
plt.legend(['Pod observado'], loc='best')

# Título do gráfico
plt.title('Disponibilidade do Pod')

# Mostrar o desvio padrão como linha centralizada em cada barra
for i in range(len(valores)):
    plt.errorbar(labels[i], valores[i], yerr=desvio_padrao[i], color='black', linewidth=2, capsize=8)

    # Mostrar o valor do desvio padrão no topo da barra
    plt.text(i, valores[i] + 2, desvio_padrao[i], ha='center')

plt.ylabel('Disponibilidade (%)')

plt.show()

# Mostrar o gráfico
# plt.savefig('grafico-disponibilidade.png')
