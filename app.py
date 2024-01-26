from flask import Flask, render_template, request, jsonify
import requests
app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weatherapp',methods=['POST'])
def get_weather_data():
    url="https://api.openweathermap.org/data/2.5/weather"
    city= request.form['city']
    units=request.form['units']
    api=request.form['api']
    param={
        'q':city,
        'units':units,
        'appid':api
    }
    response = requests.get(url,params=param)
    data=response.json()
    return f"data:{data}"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)


