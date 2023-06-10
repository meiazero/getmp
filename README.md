# getmp

this repo is for request the metric of pod using prometheus on cluster kubernetes.

## To use this project see the step-by-step

# Requirements

-   python3
-   pipenv

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

```env
CPU=http://localhost:9090/api/v1/query?query=cpu
MEMORIA=http://localhost:9090/api/v1/query?query=memoria
FSREADS=http://localhost:9090/api/v1/query?query=fsreads
FSWRITES=http://localhost:9090/api/v1/query?query=fswrites
PACKETSREC=http://localhost:9090/api/v1/query?query=packetsreceived
PACKETSTRANS=http://localhost:9090/api/v1/query?query=packetstransmitted
BYTESREC=http://localhost:9090/api/v1/query?query=bytesreceived
BYTESTRANS=http://localhost:9090/api/v1/query?query=bytestransmitted
```

## Run

```bash
python3 src/get_all.py
```

## Contributing

clone this repo and send your PR
