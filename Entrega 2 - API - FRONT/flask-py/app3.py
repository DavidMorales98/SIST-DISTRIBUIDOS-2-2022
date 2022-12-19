from flask import Flask, jsonify
from cassandra.cluster import Cluster
import json
import cassandra.auth
import ssl
from flask_cors import CORS


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.verify_mode = ssl.CERT_NONE
auth_provider = cassandra.auth.PlainTextAuthProvider(username='climappuser', password='IVuMTDjsjIZZPUeFfgELtPmPWQoPtCk6GkceUD88DMULU2295IikgzibOIyvfdz8Us5mdzJrqXGQACDbPlb4tg==')
cluster = Cluster(['climappuser.cassandra.cosmos.azure.com'], port = '10350', auth_provider=auth_provider,ssl_context=ssl_context)
session = cluster.connect()
session.execute('USE weather')
app = Flask(__name__)
CORS(app)

@app.route('/alldata')
def getAllCountries():
    countries1 = session.execute('SELECT JSON * FROM africa')
    countries2 = session.execute('SELECT JSON * FROM america')
    countries3 = session.execute('SELECT JSON * FROM oceania')
    countries4 = session.execute('SELECT JSON * FROM europa')
    countries5 = session.execute('SELECT JSON * FROM asia')
    countriesObj = []
    for country in countries1:
        countriesObj.append(json.loads(country.json))
    for country in countries2:
        countriesObj.append(json.loads(country.json))
    for country in countries3:
        countriesObj.append(json.loads(country.json))
    for country in countries4:
        countriesObj.append(json.loads(country.json))
    for country in countries5:
        countriesObj.append(json.loads(country.json))
    return countriesObj
    
@app.route('/countrydata/<string:country_name>')
def getCountry(country_name):
    countries1 = session.execute('SELECT JSON * FROM africa')
    countries2 = session.execute('SELECT JSON * FROM america')
    countries3 = session.execute('SELECT JSON * FROM oceania')
    countries4 = session.execute('SELECT JSON * FROM europa')
    countries5 = session.execute('SELECT JSON * FROM asia')
    countriesObj = []
    for country in countries1:
        countriesObj.append(json.loads(country.json))
    for country in countries2:
        countriesObj.append(json.loads(country.json))
    for country in countries3:
        countriesObj.append(json.loads(country.json))
    for country in countries4:
        countriesObj.append(json.loads(country.json))
    for country in countries5:
        countriesObj.append(json.loads(country.json))
    for country in countriesObj:
        if (country['name'] == country_name):
            return country
    

@app.route('/africadata')
def getCountriesAfrica():
    countries = session.execute('SELECT JSON * FROM africa')
    countriesObj = []
    for country in countries:
        countriesObj.append(json.loads(country.json))
    return countriesObj

@app.route('/americadata')
def getCountriesAmerica():
    countries = session.execute('SELECT JSON * FROM america')
    countriesObj = []
    for country in countries:
        countriesObj.append(json.loads(country.json))
    return countriesObj

@app.route('/oceaniadata')
def getCountriesOceania():
    countries = session.execute('SELECT JSON * FROM oceania')
    countriesObj = []
    for country in countries:
        countriesObj.append(json.loads(country.json))
    return countriesObj

@app.route('/europadata')
def getCountriesEuropa():
    countries = session.execute('SELECT JSON * FROM europa')
    countriesObj = []
    for country in countries:
        countriesObj.append(json.loads(country.json))
    return countriesObj

@app.route('/asiadata')
def getCountriesAsia():
    countries = session.execute('SELECT JSON * FROM asia')
    countriesObj = []
    for country in countries:
        countriesObj.append(json.loads(country.json))
    return countriesObj
if __name__ == '__main__':
        app.run(debug = True, port = 4000)