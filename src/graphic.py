# plot the graph from the data in the text file
import matplotlib.pyplot as plt

# Read data from the text file


def read_data(file_name):
    x_a = []
    y_a = []
    x_v = 0
    with open(file_name, 'r') as file:
        for line in file:
            values = line.split()

            x_v += 5
            y_a.append(float(values[0]))
            x_a.append(float(x_v))
    return x_a, y_a

# Plot the graph


def plot_graph(x, y, x_label='', y_label='', title='titulo'):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()

# Main function


def main(path, output):
    # file_name = './metrics/memoria-2023-05-24.csv'  # Update with your file name
    file_name = path
    x, y = read_data(file_name)
    plot_graph(x, y)
    # plt.savefig(output)


if __name__ == '__main__':
    main()
