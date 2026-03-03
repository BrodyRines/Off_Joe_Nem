import configparser
import requests

config = configparser.ConfigParser()
config.read('.env')


key = config['MY_KEY']['KEY'] 
url = 'https://csfloat.com/api/v1/listings/324288155723370196'
headers = {'Authorization': key}
resp = requests.get(url, headers=headers)

print(resp.json())
