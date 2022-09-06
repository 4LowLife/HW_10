from flask import Flask
from utils import *

app = Flask(__name__)

@app.route('/')
def page_name():
    """Главная страница"""
    candidates: list[dict] = get_all_candidates()
    result: str = format_candidates(candidates)
    return result

@app.route('/skills/<skill>')
def page_skills(uid):
    candidate: dict = get_candidate_id(uid)
    result = f"<img src={candidate['picture']}>"
    result += format_candidates([candidate])
    return result

@app.route('/skills/<skill>')
def page_skills(skill):
    skill_lower = skill.lower()
    candidates: list[dict] = get_candidate_skill(skill_lower)
    result = format_candidates()
    return result

app.run()


