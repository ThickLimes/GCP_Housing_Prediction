from google.cloud import automl_v1beta1 as automl
import google.auth
from google.oauth2 import service_account
import pandas as pd
import json
import re
import requests
project_id = 'gcp-chili-project'
compute_region = 'us-central1'
model_display_name = 'backup_plan_20210227040744'

t=service_account.Credentials.from_service_account_file("ACC CRED HERE")
model_id = 'backup_plan_20210227040744'



url = 'https://github.com/caminofinancial/data-eng-take-home/blob/master/prequalresult.json'

resp = requests.get(url)
resp_parsed = re.sub(r'^jsonp\d+\(|\)\s+$', '', resp.text)
inputs = json.load(resp_parsed)

client = automl.TablesClient(project=project_id, region=compute_region, credentials=t)
response = client.predict(model_display_name=model_display_name, inputs=inputs[0])

print("Prediction results:")
for result in response.payload:
    print("Predicted class name: {}".format(result.tables.value))
    
def test_prediction:
    assert result.tables.value == 126043.5625
