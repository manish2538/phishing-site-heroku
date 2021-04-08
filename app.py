from django.http import HttpResponse
from django.shortcuts import render
import joblib,os
import numpy as np
from flask import Flask , request , jsonify , render_template
import pickle

app = Flask(__name__)

phish_model = open('phishing.pkl','rb')
phish_model_ls = joblib.load(phish_model)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods = ['POST'])
def predict():
	#x_predict = []
	#x_predict.append(str(experience))
	x_features = [str(x) for x in request.form.values()]

	y_predict = phish_model_ls.predict(x_features)
	if y_predict =='bad':
		result = 'Phising site'
	elif y_predict =='good':
		result = "legit site"

	return render_template('home.html' ,prediction_text = result)

    	
if __name__ == "__main__":
    app.run(debug = True)
