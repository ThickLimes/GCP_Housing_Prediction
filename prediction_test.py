from google.cloud import automl_v1beta1 as automl
import google.auth
from google.oauth2 import service_account
import pandas as pd
import json
project_id = 'gcp-chili-project'
compute_region = 'us-central1'
model_display_name = 'backup_plan_20210227040744'
#t=google.auth.load_credentials_from_file(r'C:\Users\logan\PycharmProjects\GCP-application-chile\gcp-chili-project-da83c37a90e5.json')
t=service_account.Credentials.from_service_account_file(r'C:\Users\logan\PycharmProjects\GCP-application-chile\gcp-chili-project-da83c37a90e5.json')
model_id = 'backup_plan_20210227040744'
f=open(r'C:\Users\logan\PycharmProjects\GCP-application-chile\test_ex2.json')
inputs=json.load(f)
print(inputs)
client = automl.TablesClient(project=project_id, region=compute_region, credentials=t)
response = client.predict(model_display_name=model_display_name, inputs=inputs[0])

print("Prediction results:")
for result in response.payload:
    print("Predicted class name: {}".format(result.tables.value))
