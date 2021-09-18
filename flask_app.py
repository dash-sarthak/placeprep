from flask import Flask, render_template, request
from calculate_score import prob_percent

app = Flask(__name__)


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


# <input type="text" placeholder="Full Name" name="full_name">
#     <input type="text" placeholder="College Name" name="college">
#     <input type="text" placeholder="Stream" name="stream">
#     <input type="text" placeholder="CGPA" name="cgpa">
#     <input type="text" placeholder="Backlogs (History + Active)" name="backlogs">
#     <input type="text" placeholder="Number of Internships" name="internships">
#     <button type="submit" class="btn-grad">See the results</button>
