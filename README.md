# QCancer<sup>&reg;</sup> Explanation

This web application aims to explain the QCancer<sup>&reg;</sup> algorithm which predicts cancer risks for males and females of the age between 25 and 89 in the UK (more information on https://qcancer.org/).

This app provides a **counterfactual explanation** (in graphical and textual forms) as well as the standard **SHAP explanation**, both of which are local explanations (i.e. with respect to the given input).

The app is now available online at https://qcancer-explanation.herokuapp.com/.

## Run the program on a local machine
Step 1: Install relevant packages (only for the first time):\
`pip install -r requirements.txt`

Step 2: Run the app:\
`python main.py` 