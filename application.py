from flask import Flask,render_template,request
import  numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData,Predict

app=Flask(__name__)
application=app

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/predictdata',methods=['GET','POST'])
def predictdata():
    if request.method=='GET':
        return render_template('index.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))

        )
        pred_df=data.data_asdf()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=Predict()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('index.html',results=results[0])
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(debug=True)