from datetime import date
import json
import logging
import time
from urllib import request
import os
from dotenv import dotenv_values

CPU = dotenv_values(".env")['CPU']
MEMORIA = dotenv_values(".env")['MEMORIA']
FSREADS = dotenv_values(".env")['FSREADS']
FSWRITES = dotenv_values(".env")['FSWRITES']
PACKETSREC = dotenv_values(".env")['PACKETSREC']
PACKETSTRANS = dotenv_values(".env")['PACKETSTRANS']
BYTESREC = dotenv_values(".env")['BYTESREC']
BYTESTRANS = dotenv_values(".env")['BYTESTRANS']

URLS = [CPU, MEMORIA, FSREADS, FSWRITES,
        PACKETSREC, PACKETSTRANS, BYTESREC, BYTESTRANS]


def ReqMetrics(url, output, type='metric'):
    res: str = request.urlopen(url).read()
    json_dict: dict = json.loads(res.decode('utf-8'))
    out_dict: dict = [x for x in json_dict['data']
                      ['result'][0]['value']]
    value_zero = str(out_dict[1])
    WriteMetricsOnFile(value=value_zero, locale=output, metric_name=type)


def WriteMetricsOnFile(value, locale='.', metric_name="metric",):
    if locale:
        os.makedirs(f'{locale}/metrics', exist_ok=True)

        with open(f'{locale}/metrics/{metric_name}-{date.today()}.csv', "+a") as file:
            # file.write(f'cpu,memoria,fsreads,fswrites,packetsrec,packetstrans,bytesrec,bytestrans\n')
            # after test check if the loop is here.
            file.write(f'{value}\n')


if __name__ == "__main__":
    while True:
        ReqMetrics(CPU, '.', 'cpu')
        ReqMetrics(MEMORIA, '.', 'memoria')
        ReqMetrics(FSREADS, '.', 'fsreads')
        ReqMetrics(FSWRITES, '.', 'fswrites')
        ReqMetrics(PACKETSREC, '.', 'pkgrec')
        ReqMetrics(PACKETSTRANS, '.', 'pkgtrans')
        ReqMetrics(BYTESREC, '.', 'byrec')
        ReqMetrics(BYTESTRANS,  '.', 'bytrans')
        time.sleep(5)
