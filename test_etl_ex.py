import pandas as pd
import requests
import io

url = "https://raw.githubusercontent.com/ThickLimes/GCP-application-chile/main/train.csv?token=ASPTH5CG4Y6CXGK6RB7A6T3AIOVVA" 
download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')))
test_len=len(df)
def test_data():
  assert test_len==1461
  
