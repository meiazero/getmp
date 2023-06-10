'''

Faz o uso da classe GraphPlotter para plotar um gráfico a partir de um arquivo CSV,
que pode ser passado como argumento de linha de comando.

'''

import argparse

from graphic import GraphPlotter


if __name__ == '__main__':
    # Configurar os argumentos de linha de comando
    parser = argparse.ArgumentParser(
        description='Plotar um gráfico a partir de um arquivo CSV')
    parser.add_argument('-f', '--file', type=str,
                        help='Caminho para o arquivo CSV de entrada', required=True)
    parser.add_argument('-o', '--output', type=str,
                        help='Caminho para salvar o gráfico', required=False,
                        default='graph')
    parser.add_argument('-t', '--title', type=str,
                        help='Título do gráfico', default='Gráfico')
    parser.add_argument('-xl', '--xlabel', type=str,
                        help='Rótulo do eixo X', default='Time')
    parser.add_argument('-yl', '--ylabel', type=str,
                        help='Rótulo do eixo Y', default='Value')
    args = parser.parse_args()

    # Criar uma instância do GraphPlotter
    plotter = GraphPlotter(args.file, args.output)

    # Ler os dados do arquivo
    plotter.read_data()

    # Plotar o gráfico
    plotter.plot_graph()
