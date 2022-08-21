from collections import defaultdict
import numpy as np

# Change bases here for male
bases_male = {'blood': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'colorectal': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'gastro': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'lung': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'other': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'pancreatic': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'prostate': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'renal': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'testicular': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'})}

# Change bases here for female
bases_female = {'blood': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'breast': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'cervical': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'colorectal': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'gastro': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'lung': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'other': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'ovarian': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'pancreatic': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}),
        'renal': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}),
        'uterine': defaultdict(lambda: 'no', {'age': 40, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'})}

# Numpy array bases
# Modify these when baselines are changed
# Caution: make sure that dtype=float is set explicitly!!!
male_base_array = np.array([40,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], dtype=float)
female_base_array = np.array([40,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], dtype=float)

# <============================== Background for features ==============================>
male_input = ["age", "alcohol_cat4", "b_chronicpan", "b_copd", "b_type2", 
"bmi", "c_hb", "fh_gicancer", "fh_prostatecancer", "new_abdodist", "new_abdopain", "new_appetiteloss", "new_dysphagia",
"new_gibleed", "new_haematuria", "new_haemoptysis", "new_heartburn", "new_indigestion", "new_necklump", "new_nightsweats", "new_rectalbleed",
"new_testispain", "new_testicularlump", "new_vte", "new_weightloss", "s1_bowelchange", "s1_constipation", "s1_cough", "s1_impotence",
"s1_nocturia", "s1_urinaryfreq", "s1_urinaryretention", "smoke_cat"]

female_input = ["age", "alcohol_cat4", "b_chronicpan", "b_copd", "b_endometrial",
"b_type2", "bmi", "c_hb", "fh_breastcancer", "fh_gicancer", "fh_ovariancancer", "new_abdodist", "new_abdopain",
"new_appetiteloss", "new_breastlump", "new_breastpain", "new_breastskin", "new_dysphagia", "new_gibleed", "new_haematuria", 
"new_haemoptysis", "new_heartburn", "new_imb", "new_indigestion", "new_necklump", "new_nightsweats", "new_pmb", "new_postcoital",
"new_rectalbleed", "new_vte", "new_weightloss", "s1_bowelchange", "s1_bruising", "s1_constipation", "s1_cough",
"smoke_cat"]

def getAlcoholValue(alco):
    alcohol_values = {"no": 0, "< 1 unit per day": 1, "1-2 units per day": 2, "3+ units per day": 3}
    return alcohol_values[alco]

def getSmokeValue(smoke):
    smoke_values = {"non": 0, "ex": 1, "light": 2, "moderate": 3, "heavy": 4}
    return smoke_values[smoke]

def getCheckboxValue(form, name):
    return 1 if name in form else 0

def getCheckboxInputValue(form, name):
    return 'yes' if name in form else 'no'

# This is to be used to put in the data dictionary of all_data (also used in shap_exp.py)
def getInputsMale(form):
    inputs = {
        "age": int(form['age']),
        "alcohol_cat4": form['alcohol_cat4'], 
        "b_chronicpan": getCheckboxInputValue(form, "b_chronicpan"), 
        "b_copd": getCheckboxInputValue(form, "b_copd"), 
        "b_type2": getCheckboxInputValue(form, "b_type2"), 
        "bmi": float(form['bmi']),
        "c_hb": getCheckboxInputValue(form, "c_hb"),
        "fh_gicancer": getCheckboxInputValue(form, "fh_gicancer"),
        "fh_prostatecancer": getCheckboxInputValue(form, "fh_prostatecancer"),
        "new_abdodist": getCheckboxInputValue(form, "new_abdodist"),
        "new_abdopain": getCheckboxInputValue(form, "new_abdopain"),
        "new_appetiteloss": getCheckboxInputValue(form, "new_appetiteloss"),
        "new_dysphagia": getCheckboxInputValue(form, "new_dysphagia"),
        "new_gibleed": getCheckboxInputValue(form, "new_gibleed"),
        "new_haematuria": getCheckboxInputValue(form, "new_haematuria"),
        "new_haemoptysis": getCheckboxInputValue(form, "new_haemoptysis"),
        "new_heartburn": getCheckboxInputValue(form, "new_heartburn"),
        "new_indigestion": getCheckboxInputValue(form, "new_indigestion"),
        "new_necklump": getCheckboxInputValue(form, "new_necklump"),
        "new_nightsweats": getCheckboxInputValue(form, "new_nightsweats"),
        "new_rectalbleed": getCheckboxInputValue(form, "new_rectalbleed"),
        "new_testispain": getCheckboxInputValue(form, "new_testispain"),
        "new_testicularlump": getCheckboxInputValue(form, "new_testicularlump"),
        "new_vte": getCheckboxInputValue(form, "new_vte"),
        "new_weightloss": getCheckboxInputValue(form, "new_weightloss"),
        "s1_bowelchange": getCheckboxInputValue(form, "s1_bowelchange"),
        "s1_constipation": getCheckboxInputValue(form, "s1_constipation"),
        "s1_cough": getCheckboxInputValue(form, "s1_cough"),
        "s1_impotence": getCheckboxInputValue(form, "s1_impotence"),
        "s1_nocturia": getCheckboxInputValue(form, "s1_nocturia"),
        "s1_urinaryfreq": getCheckboxInputValue(form, "s1_urinaryfreq"),
        "s1_urinaryretention": getCheckboxInputValue(form, "s1_urinaryretention"),
        "smoke_cat": form['smoke_cat'],
    }
    return inputs

# This is to be used to put in the data dictionary of all_data (also used in shap_exp.py)
def getInputsFemale(form):
    inputs = {
        "age": int(form['age']),
        "alcohol_cat4": form['alcohol_cat4'], 
        "b_chronicpan": getCheckboxInputValue(form, "b_chronicpan"), 
        "b_copd": getCheckboxInputValue(form, "b_copd"), 
        "b_endometrial": getCheckboxInputValue(form, "b_endometrial"), 
        "b_type2": getCheckboxInputValue(form, "b_type2"), 
        "bmi": float(form['bmi']), 
        "c_hb": getCheckboxInputValue(form, "c_hb"), 
        "fh_breastcancer": getCheckboxInputValue(form, "fh_breastcancer"), 
        "fh_gicancer": getCheckboxInputValue(form, "fh_gicancer"), 
        "fh_ovariancancer": getCheckboxInputValue(form, "fh_ovariancancer"), 
        "new_abdodist": getCheckboxInputValue(form, "new_abdodist"), 
        "new_abdopain": getCheckboxInputValue(form, "new_abdopain"), 
        "new_appetiteloss": getCheckboxInputValue(form, "new_appetiteloss"), 
        "new_breastlump": getCheckboxInputValue(form, "new_breastlump"), 
        "new_breastpain": getCheckboxInputValue(form, "new_breastpain"), 
        "new_breastskin": getCheckboxInputValue(form, "new_breastskin"), 
        "new_dysphagia": getCheckboxInputValue(form, "new_dysphagia"), 
        "new_gibleed": getCheckboxInputValue(form, "new_gibleed"), 
        "new_haematuria": getCheckboxInputValue(form, "new_haematuria"), 
        "new_haemoptysis": getCheckboxInputValue(form, "new_haemoptysis"), 
        "new_heartburn": getCheckboxInputValue(form, "new_heartburn"), 
        "new_imb": getCheckboxInputValue(form, "new_imb"), 
        "new_indigestion": getCheckboxInputValue(form, "new_indigestion"), 
        "new_necklump": getCheckboxInputValue(form, "new_necklump"), 
        "new_nightsweats": getCheckboxInputValue(form, "new_nightsweats"), 
        "new_pmb": getCheckboxInputValue(form, "new_pmb"), 
        "new_postcoital": getCheckboxInputValue(form, "new_postcoital"), 
        "new_rectalbleed": getCheckboxInputValue(form, "new_rectalbleed"), 
        "new_vte": getCheckboxInputValue(form, "new_vte"), 
        "new_weightloss": getCheckboxInputValue(form, "new_weightloss"), 
        "s1_bowelchange": getCheckboxInputValue(form, "s1_bowelchange"), 
        "s1_bruising": getCheckboxInputValue(form, "s1_bruising"), 
        "s1_constipation": getCheckboxInputValue(form, "s1_constipation"), 
        "s1_cough": getCheckboxInputValue(form, "s1_cough"), 
        "smoke_cat": form['smoke_cat'],
    }
    return inputs