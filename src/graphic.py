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
            try:
                y_a.append(float(values[0])-float(values[0-1])
            else:
		y_a.append(float(values[0]))
	    except Exception as e:
        	os.makedirs("logs", exist_ok=True)
        	logging.basicConfig(
            	level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='logs/errors.log')
        	logging.error("Error: {}".format(e))
            
            
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


def main(path, label_x='', label_y='', title='', output='.'):
    # file_name = './metrics/memoria-2023-05-24.csv'  # Update with your file name
    file_name = path
    x, y = read_data(file_name)
    plot_graph(x, y, x_label=label_x, y_label=label_y, title=title)
    # plt.savefig(output)


if __name__ == '__main__':
    main(path="./metrics/pkgtrans-2023-05-24.csv",
         label_x="tempo (s)", label_y="packets", title="PACKETS TRANSMITTED (%)")
