from flask import render_template
from flask import request
from app import app
import urllib.request
import urllib.parse 
import json

@app.route('/')
@app.route('/index')
def index():
    url = 'http://bartender.whitestelephant.net:3500/make_drink'
    drink = urllib.request.urlopen(url).read()
    drink_dict = json.loads(drink)
    ingredient_strings = drink_dict['ingredients']
    encoded_str = drink_dict['encoded string']
    return render_template('index.html', ingredients = ingredient_strings, encoded_str = encoded_str)

@app.route('/link')
def link():
    code = request.args.get('code')
    
    url = 'http://bartender.whitestelephant.net:3500/get_drink'
    args = {'code': code}
    arg_str = urllib.parse.urlencode(args)
    url = url + '?' + arg_str

    drink = urllib.request.urlopen(url).read()
    drink_dict = json.loads(drink)
    ingredient_strings = drink_dict['ingredients']
    return render_template('index.html', ingredients = ingredient_strings)