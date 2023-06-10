import argparse
import matplotlib.pyplot as plt
import pandas as pd


class GraphPlotter:
    def __init__(self, input_file, output_path):
        self.input_file = input_file
        self.output_path = output_path

    def read_data(self):
        # Ler os dados do arquivo CSV
        self.df = pd.read_csv(self.input_file)

    def plot_graph(self):
        # Criar uma figura e eixos
        fig, ax = plt.subplots()
        time = [i for i in range(len(self.df['Time']))]

        # Plotar o gráfico de dispersão
        ax.scatter(time, self.df['Value'],
                   marker='.', color='red', label='Value')

        # Plotar o gráfico de linha
        ax.plot(time, self.df['Value'])

        # Definir o título do gráfico
        ax.set_title('Uso de Memoria')

        # Definir o rótulo do eixo X
        ax.set_xlabel('Tempo')

        # Definir o rótulo do eixo Y
        ax.set_ylabel('Uso de Memoria')

        # diminue a fonte dos ticks
        ax.tick_params(axis='both', which='major', labelsize=8)

        # Salvar o gráfico no caminho especificado
        plt.savefig(self.output_path)

        # Mostrar o gráfico na tela (opcional)
        # plt.show()


if __name__ == '__main__':
    # Configurar os argumentos de linha de comando
    parser = argparse.ArgumentParser(
        description='Plotar um gráfico a partir de um arquivo CSV')
    parser.add_argument('input_file', type=str,
                        help='Caminho para o arquivo CSV de entrada')
    parser.add_argument('output_path', type=str,
                        help='Caminho para salvar o gráfico')
    args = parser.parse_args()

    # Criar uma instância do GraphPlotter
    plotter = GraphPlotter(args.input_file, args.output_path)

    # Ler os dados do arquivo
    plotter.read_data()

    # Plotar o gráfico
    plotter.plot_graph()
