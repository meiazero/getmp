import os
import sys
import argparse
import logging
from datetime import date


class GetMetrics:

    CLI_VERSION = "0.0.1"

    def __init__(self):
        self.__run()

    def __run(self):

        self.parser = argparse.ArgumentParser(
            prog="Request the metrics of the Kubernetes API",
            description="Request the metrics of the Kubernetes API and save stdin on text file.",
            epilog="Made with love by @meiazero",
            usage="%(prog)s [options]")

        self.parser.version = self.CLI_VERSION

        self.parser.add_argument("-v", "--version", action="version")

        self.parser.add_argument(
            "-u", "--url", type=str, default="", required=True, help="URL if the json response. ")

        self.parser.add_argument(
            "-o", "--output", type=str, default=".", required=False, help="Path to save the stdin")

        args_parser = self.__args()

        if args_parser:
            try:
                if args_parser.output:
                    os.makedirs(f'{args_parser.output}/metrics', exist_ok=True)

                    with open(f'{args_parser.output}/metrics/{date.today()}.txt', "w") as f:
                        f.write(
                            f'cpu,memoria,fsreads,fswrites,packetsrec,packetstrans,bytesrec,bytestrans\n')
                        # change to reponse in json
                        for i in range(0, 5):
                            f.write(self.__getMetrics())

                else:
                    print(args_parser.url)  # change to reponse in json

            except Exception as e:
                os.makedirs("logs", exist_ok=True)
                logging.basicConfig(
                    level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='logs/errors.log')
                logging.error("Error: {}".format(e))

    def __args(self):
        return self.parser.parse_args()

    def __getMetrics(self):
        return f'1, 2, 3, 4, 5, 6, 7, 8\n'
