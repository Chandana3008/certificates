import json
import requests
from flask import Flask, render_template
import urllib

app = Flask(__name__)

@app.route('/<rid>')
def home(rid):
	rid = str(rid)
	try:
		with urllib.request.urlopen('https://cdn.talentsprint.com/portfolios/profile_json/'+ rid +'.json') as url:
			data = json.loads(url.read().decode())
	except Exception as err:
		return "Unable to find your Trainee ID!!"
	try:
		with urllib.request.urlopen('https://cdn.talentsprint.com/portfolios/profile_json/desc.json') as url_desc:
			desc_data = json.loads(url_desc.read().decode())
	except Exception as err:
		return "Check the json file name"
	return render_template('output.html', data = data, rid = rid, desc_data = desc_data)
if __name__ == '__main__':
   app.run(debug=True)