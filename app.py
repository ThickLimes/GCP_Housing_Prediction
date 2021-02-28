from flask import Flask, escape, request, jsonify
import numpy as np
from google.cloud import automl_v1beta1 as automl
import google.auth
from google.oauth2 import service_account
# (developer): Uncomment and set the following variables
project_id = 'gcp-chili-project'
compute_region = 'us-central1'
model_display_name = 'backup_plan_20210227040744'
#t=google.auth.load_credentials_from_file(r'C:\Users\logan\PycharmProjects\GCP-application-chile\gcp-chili-project-da83c37a90e5.json')
t=service_account.Credentials.from_service_account_file(r'C:\Users\logan\PycharmProjects\GCP-application-chile\gcp-chili-project-da83c37a90e5.json')
model_id = 'backup_plan_20210227040744'
client = automl.TablesClient(credentials=t,project=project_id, region=compute_region)
model = client.get_model(model_display_name=model_display_name)


app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get("name", "This is the front page")
    return f'Hello, {escape(name)}!'

@app.route('/results',methods=['POST'])

def results():

    data = request.get_json(force=True)
    inputs=data
    response = client.predict(model_display_name=model_id, inputs=inputs)
    for result in response.payload:
        print("Predicted class score: {}".format(result.tables.score))
        output = result.tables.score
    return jsonify(output)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)