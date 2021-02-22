from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import requests
import json
import os
import shutil

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.route("/surah/<id>")
def surah(id):
	if id.isdigit():
		id = int(id)
		if id > 114 or id < 1:
			return render_template("404.html")
		else:
			file = open("data/" + str(id) + ".json", "rb").read()
			ayat = []
			for i in json.loads(file):
				ayat.append(i)
			return render_template("surah.html", value=ayat)
	else:
		return render_template("404.html")

	
@app.route("/")
def index():
	file = open("data/surat.json", "rb").read()
	surah = []
	for i in json.loads(file):
		surah.append(i)
	return render_template("index.html", value=surah)

@app.route("/search", methods=["POST", "GET"])
def search():
	return render_template("search.html")
		


if __name__ == '__main__':
	try: shutil.rmtree("__pycache__")
	except: pass
	app.run(debug=True)
