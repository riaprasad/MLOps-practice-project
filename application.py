from flask import Flask,request,render_template, jsonify
import numpy as np
import pandas as pd
from flask_cors import CORS,cross_origin

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(

            squareMeters = request.form.get('squareMeters'),
            numberOfRooms = request.form.get('numberOfRooms'),
            hasYard = request.form.get('hasYard'),
            hasPool = request.form.get('hasPool'),
            floors = request.form.get('floors'),
            cityCode = request.form.get('cityCode'),
            cityPartRange = request.form.get('cityPartRange'),
            numPrevOwners = request.form.get('numPrevOwners'),
            made = request.form.get('made'),
            isNewBuilt = request.form.get('isNewBuilt'),
            hasStormProtector = request.form.get('hasStormProtector'),
            basement = request.form.get('basement'),
            attic = request.form.get('attic'),
            garage = request.form.get('garage'),
            hasStorageRoom = request.form.get('hasStorageRoom'),
            hasGuestRoom = request.form.get('hasGuestRoom')

            
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

@app.route('/predictPostmanApi', methods=['POST']) 
@cross_origin()
def predict_PostmanApi():
    if request.method == 'POST':
        data = CustomData(
            squareMeters = request.json['squareMeters'],
            numberOfRooms = request.json['numberOfRooms'],
            hasYard = request.json['hasYard'],
            hasPool = request.json['hasPool'],
            floors = request.json['floors'],
            cityCode = request.json['cityCode'],
            cityPartRange = request.json['cityPartRange'],
            numPrevOwners = request.json['numPrevOwners'],
            made = request.json['made'],
            isNewBuilt = request.json['isNewBuilt'],
            hasStormProtector = request.json['hasStormProtector'],
            basement = request.json['basement'],
            attic = request.json['attic'],
            garage = request.json['garage'],
            hasStorageRoom = request.json['hasStorageRoom'],
            hasGuestRoom = request.json['hasGuestRoom']
        )
    
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(pred_df)

        d = {'price' : pred}
        return jsonify(d)

    

if __name__=="__main__":
    app.run(host="0.0.0.0")        