from flask import Flask, render_template, request
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        # Load the dataset
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        df = data.getDataAsDataFrame()
        
        pipeline = PredictPipeline()
        prediction = pipeline.predict(df)

        return render_template('home.html', results=prediction[0])
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

