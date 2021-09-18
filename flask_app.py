from flask import Flask, render_template, request
import pandas as pd
import random
import pickle

FILE_NAME = (
    "/home/sarthak/Desktop/Personal Projects/Placeprep/Website/finalized_model.sav"
)

app = Flask(__name__)


def prob_percent(value_list):
    value_dict = {
        "Age": int(value_list[0]),
        "Internships": int(value_list[1]),
        "CGPA": int(float(value_list[2])),
        "HistoryOfBacklogs": int(value_list[3]),
        "Gender": int(value_list[4]),
        "Stream": int(value_list[5]),
    }

    val_df = pd.DataFrame(value_dict, index=[1])
    predictor = pickle.load(open(FILE_NAME, "rb"))
    prob_percent = round(predictor.predict_proba(val_df)[0][1] * 100, 2)

    if prob_percent == 100.0:
        return f"{10*value_dict['CGPA'] + random.randint(10-value_dict['CGPA'], value_dict['CGPA'])} %"

    return f"{prob_percent} %"


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/details")
def details():
    return render_template("details.html", title="Details")


@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":
        age = request.form["age"]
        internships = request.form["internships"]
        cgpa = request.form["cgpa"]
        backlogs = request.form["backlogs"]
        gender = request.form["gender"]
        stream = request.form["stream"]
        full_name = request.form["full_name"]

        value_list = [age, internships, cgpa, backlogs, gender, stream, full_name]

        result = prob_percent(value_list)

        return render_template("result.html", title="Result", sum=result)

    else:
        return render_template("result.html", title="Result", sum=0)


if __name__ == "__main__":
    app.run(debug=True)

