from matplotlib.pyplot import savefig, subplots
from pandas import read_csv


class GraphPlotter:
    def __init__(self, input_file, output_path):
        self.input_file = input_file
        self.output_path = output_path
        self.title = "Variação do uso de memória - Pod Observado"
        self.xlabel = "Tempo (s)"
        self.ylabel = "Uso de memória"

    def read_data(self):
        # Ler os dados do arquivo CSV
        self.df = read_csv(self.input_file)

    def plot_graph(self):
        # Criar uma figura e eixos
        fig, ax = subplots()
        time = [i for i in range(len(self.df['time']))]

        # posiciona as legendas do scarter no gráfico

        # Plotar o gráfico de dispersão
        ax.scatter(time, self.df['memory_with_attack'],
                     marker='.')
        ax.scatter(time, self.df['memory_without_attack'],
                   marker='.')
        
        # Plotar o gráfico de linhas
        ax.plot(time, self.df['memory_with_attack'], label='cenario 1', color='blue')
        ax.plot(time, self.df['memory_without_attack'],  label='cenario 2', color='orange')

        ax.grid(True)

        # Definir o título do gráfico
        ax.set_title(self.title)

        # Definir os rótulos dos eixos
        ax.set_xlabel(self.xlabel)

        ax.set_ylabel(self.ylabel)

        # Definir a legenda
        ax.legend(loc='upper left', frameon=False, fontsize=8)

        # Salvar o gráfico no caminho especificado
        savefig(self.output_path)


