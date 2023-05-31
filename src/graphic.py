import matplotlib.pyplot as plt


def read_data(file_name):
    x = []
    y = []

    try:
        with open(file_name, 'r') as file:
            for line in file:
                values = line.split()
                x_value = float(values[0])
                y_value = float(values[1])
                x.append(x_value)
                y.append(y_value)
    except FileNotFoundError:
        print("Arquivo não encontrado:", file_name)

    return x, y


def plot_graph(x, y, x_label='', y_label='', title='titulo'):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    # plt.savefig(output)
    plt.show()


def main(path, label_x='', label_y='', title='', output='.'):
    file_name = path
    x, y = read_data(file_name)
    plot_graph(x, y, x_label=label_x, y_label=label_y, title=title)


if __name__ == '__main__':
    main(
        path="./metrics/pkgtrans-2023-05-24.csv",
        label_x="tempo (s)",
        label_y="packets",
        title="PACKETS TRANSMITTED (%)"
    )
