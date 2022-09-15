import json
from flask import Flask, request, render_template

app = Flask(__name__)


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id: int):
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name: str):
    result = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            result.append(candidate)
            return result


def get_candidates_by_skill(skill_name: str):
    result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate["skills"].lower():
            result.append(candidate)
    return result


print(get_candidates_by_skill('python'))


@app.route('/')
def hello():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:idx>')
def candidate_list(idx: int):
    candidate = get_candidate(idx)
    if not candidate:
        return "Кандидат не найден"
    return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_names>')
def candidate_name(candidate_names):
    candidates = get_candidates_by_name(candidate_names)
    count = len(candidates)
    return render_template('search.html', candidates=candidates, count=count)


@app.route('/skill/<skill_name>')
def candidate_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    count = len(candidates)
    return render_template('skill.html', candidates=candidates, count=count)


app.run()
