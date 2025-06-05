import flask
from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_foir(income, fixed_obligations):
    return fixed_obligations / income * 100

@app.route("/", methods=["GET", "POST"])
def index():
    foir = None
    if request.method == "POST":
        income = float(request.form["income"])
        fixed_obligations = float(request.form["fixed_obligations"])
        foir = round(calculate_foir(income, fixed_obligations), 2)
    return render_template("index.html", foir=foir)

if __name__ == "__main__":
    app.run(debug=True)
