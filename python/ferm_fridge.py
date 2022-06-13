import serial
import json
import requests
import os
from datetime import datetime
from dotenv import dotenv_values

env_values = dotenv_values('.env')
api_key = env_values['BLYNK_KEY'] 

dateFormat = '%a %H:%M'
ser = serial.Serial(env_values['DEVICE_PORT'])
#Get Setpoint value
getSetPointURL=f'https://blynk.cloud/external/api/get?token={api_key}&dataStreamId=5'
while 1:   
    try:
        data=ser.readline().decode("utf-8")
        response = requests.get(getSetPointURL)
        appSetPoint=response.text
        json_response = json.loads(data)
        beerTemp=json_response['beerTemp']
        fridgeTemp=json_response['fridgeTemp']
        state=json_response['state']
        setPoint=json_response['setPoint']
        if float(setPoint)!=float(appSetPoint):
            jsonString=f'{{"setPoint":{appSetPoint}}}'
            ser.write(jsonString.encode())
            ser.flush()
        updatedTime=datetime.now().strftime(dateFormat)
        api_url=f'https://blynk.cloud/external/api/batch/update?token={api_key}&v2={beerTemp}&v4={fridgeTemp}&v1={state}&v3={appSetPoint}&v5={updatedTime}'
        response = requests.get(api_url)
    except Exception as e:
        print (e)
        pass

    
