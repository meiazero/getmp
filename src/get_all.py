from datetime import date
import json
import logging
import time
from urllib import request
import os
from dotenv import dotenv_values

CPU_ALVO = dotenv_values(".env")['CPU_ALVO']
MEMORIA_ALVO = dotenv_values(".env")['MEMORIA_ALVO']
FSREADS_ALVO = dotenv_values(".env")['FSREADS_ALVO']
FSWRITES_ALVO = dotenv_values(".env")['FSWRITES_ALVO']
PACKETSREC_ALVO = dotenv_values(".env")['PACKETSREC_ALVO']
PACKETSTRANS_ALVO = dotenv_values(".env")['PACKETSTRANS_ALVO']
BYTESREC_ALVO = dotenv_values(".env")['BYTESREC_ALVO']
BYTESTRANS_ALVO = dotenv_values(".env")['BYTESTRANS_ALVO']


# URLS = [CPU, MEMORIA, FSREADS, FSWRITES,
#         PACKETSREC, PACKETSTRANS, BYTESREC, BYTESTRANS]


def ReqMetrics(url, output, type='metric'):
    res = request.urlopen(url).read()
    json_dict = json.loads(res.decode('utf-8'))
    out_dict = [x for x in json_dict['data']
                ['result'][0]['value']]
    value = out_dict[1]

    WriteMetricsOnFile(value=value, locale=output, metric_name=type)
    print(f'{type}: {value}')


def WriteMetricsOnFile(value, locale='.', metric_name="metric",):
    if locale:
        try:
            os.makedirs(f'{locale}/metrics', exist_ok=True)

            with open(f'{locale}/metrics/{metric_name}-{date.today()}.csv', "+a") as file:
                # file.write(f'cpu,memoria,fsreads,fswrites,packetsrec,packetstrans,bytesrec,bytestrans\n')
                # after test check if the loop is here.
                file.write(f'{value}\n')
        except Exception as e:
            os.makedirs("logs", exist_ok=True)
            logging.basicConfig(
                level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='logs/errors.log')
            logging.error("Error: {}".format(e))


if __name__ == "__main__":
    print("Coletando métricas do alvo (apenas usuários)...")
    while True:
        ReqMetrics(CPU_ALVO, '.', 'cpu_alvo')
        ReqMetrics(MEMORIA_ALVO, '.', 'memoria_alvo')
        ReqMetrics(FSREADS_ALVO, '.', 'fsreads_alvo')
        ReqMetrics(FSWRITES_ALVO, '.', 'fswrites_alvo')
        ReqMetrics(PACKETSREC_ALVO, '.', 'pkgrec_alvo')
        ReqMetrics(PACKETSTRANS_ALVO, '.', 'pkgtrans_alvo')
        ReqMetrics(BYTESREC_ALVO, '.', 'byrec_alvo')
        ReqMetrics(BYTESTRANS_ALVO,  '.', 'bytrans_alvo')
        print("*" * 50)
        time.sleep(5)
