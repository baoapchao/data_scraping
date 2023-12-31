import os
import pandas as pd

directory = r'C:\Users\ADMIN\OneDrive\__Study\Python\Side Projects\Scraping\Crawl Stock Data\data\historical_price\fireant'
df = None
for dirpath, dirs, files in os.walk(directory):
    if files != []:
        for file in files[:1]:
            filepath = os.path.join(dirpath,file)
            df1 = pd.read_csv(filepath)
            df = pd.concat([df, df1])
print(df.tail())