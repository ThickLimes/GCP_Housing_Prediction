import pandas as pd
df=pd.read_csv('https://github.com/guga31bb/nflfastR-data/blob/master/data/play_by_play_2000.csv.gz?raw=True',compression='gzip', 
        low_memory=False)
print(df)