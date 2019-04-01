
#
#  agregate_csvs.py
#
#  Helper script that joins multiple csvs, representing pdf pages to one csv
#


import os
import pandas as pd


DATA_PATH = 'data/'
OUTPUT_PATH = 'generated_output/'
BIN_NUM = 41

NUM_PAGES = 384
pages = [p + 1 for p in range(NUM_PAGES)]


if __name__ == "__main__":

    output_file = os.path.join(OUTPUT_PATH, str(BIN_NUM) + "_all_pages.csv")

    with open(output_file, mode='w+') as output_csv:
        for p in pages:
            input_file = os.path.join(DATA_PATH, str(BIN_NUM) + "-page-" + str(p) + "-table-1.csv")
            df = pd.read_csv(input_file, header=None)
            df.to_csv(output_csv, mode='a', header=False, index=False)


