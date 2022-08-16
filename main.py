from flask import Flask, redirect, url_for, render_template, request, session, flash

from utils import calculateOutputsMale, calculateAllDataMale, calculateOutputsFemale, calculateAllDataFemale

app = Flask(__name__)

app.config["JSON_SORT_KEYS"] = False
app.jinja_env.globals.update(zip=zip)
app.secret_key = "B6i6zsH!C6ez"

@app.route('/', methods=["GET", "POST"])
def male():
    outputs = None
    all_data = None
    if request.method == 'POST':
        outputs = calculateOutputsMale(request.form)
        all_data = calculateAllDataMale(request.form, outputs)
    return render_template('male.html', outputs=outputs, all_data=all_data)

@app.route('/female', methods=['GET', 'POST'])
def female():
    outputs = None
    all_data = None
    if request.method == 'POST':
        outputs = calculateOutputsFemale(request.form)
        all_data = calculateAllDataFemale(request.form, outputs)
    return render_template('female.html', outputs=outputs, all_data=all_data)

if __name__ == "__main__":
    app.run(debug=True