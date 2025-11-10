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

if __name__ == "__main__":
    app.run(debug=True)
    