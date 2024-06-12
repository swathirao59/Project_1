# -*- coding: utf-8 -*-
"""
Created on Wed May 15 00:10:46 2024

@author: swath
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from BirdFlu import BirdFlu
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

##model=pickle.load(open("model.pkl","rb"))

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')

def get_name(name: str):
    
    return {'Welcome To this API': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and returns the output
@app.post('/predict')
def predict(Data:BirdFlu):
    Data = Data.dict()
    Scientific_Name=Data['Scientific_Name']
    Common_Name=Data['Common_Name']
    Date=Data['Date']
    Year=Data['Year']
    Month=Data['Month']
    Day=Data['Day']
    Time=Data['Time']
    Country=Data['Country']
    Country_State_County=Data['Country_State_County']
    State=Data['State']
    County=Data['County']
    Locality=Data['Locality']
    Latitude=Data['Latitude']
    Longitude=Data['Longitude']
    Parent_Species=Data['Parent_Species'] 
    features=list([Scientific_Name,Common_Name,Date,Year,Month,Day,Time,Country,Country_State_County
    ,State,County,Locality,Latitude,Longitude,Parent_Species])
   
    predict=model.predict([features])
    probab=model.predict_proba([features])
    if(predict==1):
        return {"ans":"Bird has Flu with {} probability".format(probab[0][1])}
    else:
        return {"ans":"Bird is not having flu with {} probability".format(probab[0][0])}

    

if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)