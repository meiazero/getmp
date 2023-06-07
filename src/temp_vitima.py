from get_all import ReqMetrics
from dotenv import dotenv_values
import time

CPU_VITIMA = dotenv_values(".env")['CPU_VITIMA']
MEMORIA_VITIMA = dotenv_values(".env")['MEMORIA_VITIMA']
FSREADS_VITIMA = dotenv_values(".env")['FSREADS_VITIMA']
FSWRITES_VITIMA = dotenv_values(".env")['FSWRITES_VITIMA']
PACKETSREC_VITIMA = dotenv_values(".env")['PACKETSREC_VITIMA']
PACKETSTRANS_VITIMA = dotenv_values(".env")['PACKETSTRANS_VITIMA']
BYTESREC_VITIMA = dotenv_values(".env")['BYTESREC_VITIMA']
BYTESTRANS_VITIMA = dotenv_values(".env")['BYTESTRANS_VITIMA']

if __name__ == "__main__":
    print("Coletando métricas da vitima (apenas ataque)...")
    while True:
        ReqMetrics(CPU_VITIMA, '.', 'cpu_vitima')
        ReqMetrics(MEMORIA_VITIMA, '.', 'memoria_vitima')
        ReqMetrics(FSREADS_VITIMA, '.', 'fsreads_vitima')
        ReqMetrics(FSWRITES_VITIMA, '.', 'fswrites_vitima')
        ReqMetrics(PACKETSREC_VITIMA, '.', 'pkgrec_vitima')
        ReqMetrics(PACKETSTRANS_VITIMA, '.', 'pkgtrans_vitima')
        ReqMetrics(BYTESREC_VITIMA, '.', 'byrec_vitima')
        ReqMetrics(BYTESTRANS_VITIMA,  '.', 'bytrans_vitima')
        print("*" * 50)
        time.sleep(5)
