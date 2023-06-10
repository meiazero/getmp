from matplotlib.pyplot import savefig, subplots
from pandas import read_csv


class GraphPlotter:
    def __init__(self, input_file, output_path, title='Gráfico', xlabel='Time', ylabel='Value'):
        self.input_file = input_file
        self.output_path = output_path
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def read_data(self):
        # Ler os dados do arquivo CSV
        self.df = read_csv(self.input_file)

    def plot_graph(self):
        # Criar uma figura e eixos
        fig, ax = subplots()
        time = [i for i in range(len(self.df['Time']))]

        # Plotar o gráfico de dispersão
        ax.scatter(time, self.df['Value'],
                   marker='.', color='red', label='Value')

        # Plotar o gráfico de linha
        ax.plot(time, self.df['Value'])

        ax.grid(True)

        # Definir o título do gráfico
        ax.set_title(self.title)

        # Definir os rótulos dos eixos
        ax.set_xlabel(self.xlabel)

        ax.set_ylabel(self.ylabel)

        # Definir a legenda
        ax.legend(loc='upper center', frameon=False, fontsize=8)

        # Salvar o gráfico no caminho especificado
        savefig(self.output_path)

        # Mostrar o gráfico na tela (opcional)
        # show()
