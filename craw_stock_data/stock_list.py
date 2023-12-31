import pandas as pd

# list symbols to execute

VN30_list = pd.read_csv('VN30 list.csv')

VN30_list = VN30_list['symbol'].tolist()

watching_list = pd.read_csv('Watching list.csv')

watching_list = watching_list['symbol'].tolist()

symbols = []
symbols = VN30_list + watching_list
symbols = list(dict.fromkeys(symbols))

if __name__ == "__main__":
    for i, symbol in enumerate(symbols):
        print(i, ' - ', symbol)