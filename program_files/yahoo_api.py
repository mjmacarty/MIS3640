# conda install -c pandas-datareader
import pandas_datareader as pdr
from time import time, sleep
start_time = time()
while True:
    print(pdr.get_quote_yahoo('GOOG')['price'])
    elapsed = time() - start_time
    print(elapsed)
    if elapsed >= 10:
        prompt = input("Would you like to continue? y/n: ")
        if prompt == 'n':
            break
        start_time = time()
        elapsed = 0
    sleep(1)