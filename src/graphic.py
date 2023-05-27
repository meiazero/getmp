# plot the graph from the data in the text file
import matplotlib.pyplot as plt

# Read data from the text file


def CalculateDiferenceValue(value_1, value_2):
    return (value_2 - value_1)


def read_data(file_name):
    x = []
    y = []
    timeInSeconds = 0
    tmp = 0
    with open(file_name, 'r') as file:
        for line in file:
            values = line.split()

            timeInSeconds += 5
            tmp = values[0]
            try:
                y.append(CalculateDiferenceValue(float(tmp), float(values[1])))
            except:
                y.append(float(tmp))

            x.append(float(timeInSeconds))
    return x, y

# Plot the graph


def plot_graph(x, y, x_label='', y_label='', title='titulo'):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()

# Main function


def main(path, label_x='', label_y='', title='', output='.'):
    # file_name = './metrics/memoria-2023-05-24.csv'  # Update with your file name
    file_name = path
    x, y = read_data(file_name)
    plot_graph(x, y, x_label=label_x, y_label=label_y, title=title)
    # plt.savefig(output)


if __name__ == '__main__':
    main(path="./metrics/pkgtrans-2023-05-24.csv",
         label_x="tempo (s)", label_y="packets", title="PACKETS TRANSMITTED (%)")
