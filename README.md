# GCP-application-chile
This application was developed to be able to perform housing price predictions based on a variety of factors. The model was developed by using a dataset of housing prices from Ames, Iowa. This data set contains around 80 variables that are used in the model. The model was developed using Google's AutoML Tables which handled the model developement, processing and feature engineering. It is deployed to my GCP account and has an R^2 score of around .83. The training data is stored in Cloud Storage. 

The model is able to serve out predictions via a flask server that is hosted in the Google App Engine. It accepts json formatted data at the address of https://gcp-chili-project.uc.r.appspot.com/results. It will serve out a prediction for the house price based on the input variables (example of the variables in the tes_ex2.json file). 

The CI testing for the application is handled by GitHub actions. Currently only 1 test is activated, however there is code for several more tests. The reason these are tests are not activated is because they require credentials to access the model and test the deployment and predictions. I had to remove the credential file from GitHub in order to make it public for viewing. Under normal *production* circumstances, the repo would be made private and the credential would be stored here so the extra tests could be run. Deployment is handled through CloudBuild. 

The developement environment was primarily on my local machine where I have a service account credential file. 


