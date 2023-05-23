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


def plot_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('tempo')
    plt.ylabel(f'% de uso')
    plt.title('uso cpu')
    plt.grid(True)
    plt.show()

# Main function


def main():
    file_name = './metrics/cpu-2023-05-23.csv'  # Update with your file name
    x, y = read_data(file_name)
    plot_graph(x, y)


if __name__ == '__main__':
    main()
