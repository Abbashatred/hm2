from flask import Flask
import json
import utils

app = Flask(__name__)

with open("candidates.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    