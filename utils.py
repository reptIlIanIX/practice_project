import json
from flask import Flask, request, render_template

app = Flask(__name__)

with open('candidates.json') as f:
    data = json.load(f)

items = []


def load_candidates_from_json(path):
    for item in data:
        path.append([item['name']])
    return path


print(load_candidates_from_json(items))
