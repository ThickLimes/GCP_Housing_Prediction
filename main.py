from flask import Flask, escape, request, jsonify
import numpy as np
import os
from google.cloud import automl
from google.auth import compute_engine



# (developer): Uncomment and set the following variables
project_id = 'gcp-chili-project'
compute_region = 'us-central1'
model_id = 'backup_plan_20210227040744'

client = automl.AutoMlClient()
# Get the full path of the model.
model_full_id = client.model_path(project_id, "us-central1", model_id)
response = client.deploy_model(name=model_full_id)

#client = automl.TablesClient(project=project_id, region=compute_region)

# Deploy model
#response = client.deploy_model(model_display_name=model_display_name)

# synchronous check of operation status.
print("Model deployed. {}".format(response.result()))
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get("name", "This is the front page")
    return f'Hello, {escape(name)}!'

#@app.route('/results',methods=['POST'])
#def results():

    #data = request.get_json(force=True)
    #prediction = model.predict([np.array(list(data.values()))])

    #output = prediction[0]
    #return jsonify(output)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
