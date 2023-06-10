# getmp

this repo is for request the metric of pod using prometheus on cluster kubernetes.

## To use this project see the step-by-step

# Requirements

-   python3
-   pipenv
-   docker

## Running the project

```bash
git clone https://github.com/meiazero/getmp.git
```

```bash
cd getmp
```

## Building the docker image

```bash
docker build -t getmp-grafana .
```

## Running the docker container

> Note: the container will be running grafana on the port 3000

```bash
docker run -it -p 3000:3000 --name getmp getmp-grafana
```

## Setup the grafana

-   Access the grafana on the port 3000
-   Login with the user: admin and password: admin
-   Add the prometheus datasource
-   Import the dashboard on the file dashboard.json in grafana folder
-   Configure the graph with the metrics
    -   container_cpu_usage_seconds_total
    -   container_memory_usage_bytes
    -   container_fs_reads_total
    -   container_fs_writes_total
    -   container_network_receive_packets_total
    -   container_network_transmit_packets_total
    -   container_network_receive_bytes_total
    -   container_network_transmit_bytes_total

## Running the graph plotter

### Install the dependencies

```bash
pipenv install
```

### Enter in the virtualenv

```bash
pipenv shell
```

### Run the script

```bash
python3 main.py
```

## Contributing

clone this repo and send your PR

## License

[MIT](LICENSE)

[Go to top](#getmp)
