import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('./metrics/cpu_alvo-2023-06-06.csv')
timestamps = [i for i in range(1, len(data)+1)]

plt.plot(timestamps, data)
plt.xlabel('Tempo')
plt.ylabel('Valor Métrico')
plt.title('Gráfico de Métricas do Kubernetes')
plt.xticks(rotation=45)
plt.show()
