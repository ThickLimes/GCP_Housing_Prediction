import pandas as pd
import requests
import io

url = "REPLACE-THIS-WITH-THE-URL-OF-THE-CSV-FILE" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')))
test_len=len(df)
print(df)
