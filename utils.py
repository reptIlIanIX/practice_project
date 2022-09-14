import json
from flask import Flask, request, render_template

app = Flask(__name__)

with open('candidates.json') as f:
    data = json.load(f)


def load_candidates_from_json(path):
    for item in data:
        path.append(item['name'])
    return path


def get_candidate(candidate_id):
    for item in data:
        if candidate_id == item['id']:
            candidate_id += 1
    return item['name']


@app.route('/')
def hello():
    items = []
    items = load_candidates_from_json(items)

    return render_template('list.html', items=items)


app.run()
