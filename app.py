# this file runs the application, it doesn't require an authentication method because it uses the native Google Authentication when deployed in the App Engine
from flask import Flask, escape, request, jsonify
#import numpy as np
from google.cloud import automl_v1beta1 as automl
#import google.auth
#from google.oauth2 import service_account

project_id = 'gcp-chili-project'
compute_region = 'us-central1'
model_display_name = 'backup_plan_20210227040744'

client = automl.TablesClient(project=project_id, region=compute_region)
model = client.get_model(model_display_name=model_display_name)

app = Flask(__name__)

@app.route('/')
def hello_world():
    # this provides a simple front page to view the application, just functions as a check for the application being online
    name = request.args.get("name", "This is the front page")
    return f'Hello, {escape(name)}!'

@app.route('/results',methods=['POST'])

def results():
    #this takes the request in a json form and delivers it to the AutoML model which returns a prediction
    data = request.get_json(force=True)
    inputs=data
    response = client.predict(model_display_name=model_display_name, inputs=inputs)
    for result in response.payload:
        print("Predicted class score: {}".format(result.tables.score))
        output = result.tables.score
    return jsonify(output)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
