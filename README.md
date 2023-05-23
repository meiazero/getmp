# getmp
this repo is for request the metrics of pod using prometheus on cluster kubernetes.

## To use this project see the step-by-step

# Requirements

- python3
- pipenv

## Environment

```bash
git clone https://github.com/meiazero/getmp.git
```

```bash
cd getmp
```

```bash
pipenv install
```

```bash
pipenv shell
```

```bash
cp .env.example .env
```

> edit the .env file with your URLs valids

```bash
CPU=http://<ip>:<port>/<others>
MEMORIA=http://<ip>:<port>/<others>
FSREADS=http://<ip>:<port>/<others>
FSWRITES=http://<ip>:<port>/<others>
PACKETSREC=http://<ip>:<port>/<others>
PACKETSTRANS=http://<ip>:<port>/<others>
BYTESREC=http://<ip>:<port>/<others>
BYTESTRANS=http://<ip>:<port>/<others>
```

## Run

```bash
python3 src/main.py
```

## Contributing

