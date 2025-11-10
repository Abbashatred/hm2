from flask import Flask, render_template
import utils

app = Flask(__name__)

candidates = utils.load_candidates_from_json("candidates.json")  
@app.route("/")
def main_page():
    return render_template("list.html", candidates=candidates)

@app.route("/candidate/<x>")
def card_page(x):
    candidate = utils.get_candidates(x, candidates)
    return render_template("card.html", candidate=candidate)

@app.route("/search/<candidate_name>")
def search_page(candidate_name):
    candidate_found = utils.get_candidates_by_name(candidate_name, candidates)
    return render_template("search.html", candidates=candidate_found)

@app.route("/skill/<skill_name>")
def skill_page(skill_name):
    candidate_found = utils.get_candidates_by_skill(skill_name, candidates)
    return render_template("skill.html", candidates=candidate_found, skill_name=skill_name)

if __name__ == "__main__":
    app.run()
    