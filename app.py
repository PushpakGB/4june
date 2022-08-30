# hello dear
import numpy as np
import pandas as pd
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "default api"
@app.route('/predict', methods=['GET','POST'])
def predict(    ):
    #Prediction logic
    return " api"




if __name__=="__main__":
    app.run(debug=='True')
