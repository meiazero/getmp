import matplotlib.pyplot as plt


def get_values_from_file(path):
    values = []
    with open(path, 'r') as file:
        for line in file:
            values.append(float(line.split()[0]))
    return values


def plot_variation_graph(values_incremented):
    values = []
    time = [i for i in range(len(values))]

    for i in range(len(values)):
        temp = values[i-1]
        values.append(values_incremented[i] - temp)

    # plt.scatter(time, values)
    plt.xlabel('Tempo (s)')
    plt.ylabel('Uso de cpu')
    plt.title('Uso de cpu')
    plt.grid(True)
    plt.plot(time, values)
    plt.show()


def main():
    file_path = './metrics/cpu_alvo-2023-06-06.csv'
    values = get_values_from_file(file_path)
    plot_variation_graph(values)


if __name__ == '__main__':
    main()
