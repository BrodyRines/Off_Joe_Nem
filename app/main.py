from flask import Flask, render_template
import configparser
import requests
import os



app = Flask(__name__)

@app.route('/')
def index():
    config = configparser.ConfigParser()
    config.read('.env')

    key = config['MY_KEY']['KEY'] 
    url = 'https://csfloat.com/api/v1/listings/324288155723370196'
    headers = {'Authorization': key}
    resp = requests.get(url, headers=headers)
    data = resp.json() if resp.status_code == 200 else {'error': 'API failed'}
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

##print(resp.json())
