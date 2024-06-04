from flask import Flask
import pymongo

app = Flask('app')

@app.route('/')
def home():
  return "HI"

app.run(host='0.0.0.0', port=8080)
