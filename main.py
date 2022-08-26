from flask import Flask, url_for, render_template, request

from utils import calculateOutputsMale, calculateAllDataMale, calculateOutputsFemale, calculateAllDataFemale, male_labels, female_labels

from shap_exp import male_base_risks, female_base_risks, calculateShapValuesMale, calculateShapValuesFemale

app = Flask(__name__)

app.config["JSON_SORT_KEYS"] = False

@app.route('/', methods=["GET", "POST"])
def male():
    outputs = None
    all_data = None
    male_shap_values = None
    if request.method == 'POST':
        outputs = calculateOutputsMale(request.form)
        all_data = calculateAllDataMale(request.form, outputs)
        if 'shap_included' in request.form:
            male_shap_values = calculateShapValuesMale(request.form)
    return render_template('male.html', outputs=outputs, all_data=all_data, labels=male_labels, base_risks=male_base_risks, shap_values=male_shap_values)

@app.route('/female', methods=['GET', 'POST'])
def female():
    outputs = None
    all_data = None
    female_shap_values = None
    if request.method == 'POST':
        outputs = calculateOutputsFemale(request.form)
        all_data = calculateAllDataFemale(request.form, outputs)
        if 'shap_included' in request.form:
            female_shap_values = calculateShapValuesFemale(request.form)
    return render_template('female.html', outputs=outputs, all_data=all_data, labels=female_labels, base_risks=female_base_risks, shap_values=female_shap_values)

if __name__ == "__main__":
    app.run(debug=True)