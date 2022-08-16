import math
from collections import defaultdict

from qcancer_male.qcancer_male_funcs import *
from qcancer_female.qcancer_female_funcs import *

# <================================ qcancer cmd part ================================>
def is_boolean(b):
    return isinstance(b, bool)

def in_range(x, min, max):
    return x >= min and x <= max

def check_range_bool(b):
    if (not in_range(b, 0, 1)):
        raise Exception("The value must be either 0 or 1")

# <================================ Male part ================================>

# A toy data sample
all_data_male = {
              'blood': 
                [{'factor': 'age', 'data': {'value': 30, 'base': 25, 'effect': 10.9}},
                 {'factor': 'bmi', 'data': {'value': 20, 'base': 25, 'effect': -13.5}},
                 {'factor': 'c_hb', 'data': {'value': 'yes', 'base': 'no', 'effect': 6.3}},
                 {'factor': 'new_abdopain', 'data': {'value': 'no', 'base': 'no', 'effect': 0}},
                 {'factor': 'new_vte', 'data': {'value': 'yes', 'base': 'no', 'effect': 5.47}}],
              'colorectal':
                [{'factor': 'alcohol_cat4', 'data': {'value': '3+ units per day', 'base': 'non-drinker', 'effect': 18.3}},
                 {'factor': 'fh_gicancer', 'data': {'value': 'yes', 'base': 'no', 'effect': 5.1}},
                 {'factor': 'new_abdodist', 'data': {'value': 'yes', 'base': 'no', 'effect': 2.6}},
                 {'factor': 'new_weightloss', 'data': {'value': 'yes', 'base': 'no', 'effect': 4.15}},
                 {'factor': 's1_bowelchange', 'data': {'value': 'yes', 'base': 'no', 'effect': 1.589}}],
              'gastro':
                [{'factor': 'smoke_cat', 'data': {'value': 'heavy', 'base': 'non', 'effect': 17.9}},
                 {'factor': 'age', 'data': {'value': 25, 'base': 40, 'effect': -8.7562}},
                 {'factor': 'new_abdopain', 'data': {'value': 'yes', 'base': 'no', 'effect': 4.589}},
                 {'factor': 'new_gibleed', 'data': {'value': 'yes', 'base': 'no', 'effect': 4.856}},
                 {'factor': 'new_necklump', 'data': {'value': 'yes', 'base': 'no', 'effect': 1.245}}],
              'lung':
                [{'factor': 'age', 'data': {'value': 25, 'base': 32, 'effect': -8.56}},
                 {'factor': 'smoke_cat', 'data': {'value': 'moderate', 'base': 'non', 'effect': 10.9}},
                 {'factor': 'c_hb', 'data': {'value': 'yes', 'base': 'no', 'effect': 5.8}},
                 {'factor': 'new_indigestion', 'data': {'value': 'yes', 'base': 'no', 'effect': 1.45}},
                 {'factor': 'new_vte', 'data': {'value': 'yes', 'base': 'no', 'effect': 2.58}}],
              'other':
                [{'factor': 'age', 'data': {'value': 30, 'base': 30, 'effect': 0}},
                 {'factor': 'b_copd', 'data': {'value': 'yes', 'base': 'no', 'effect': 10.9}},
                 {'factor': 'new_abdopain', 'data': {'value': 'yes', 'base': 'no', 'effect': 5.7}},
                 {'factor': 'new_haematuria', 'data': {'value': 'yes', 'base': 'no', 'effect': 2.3}},
                 {'factor': 'new_necklump', 'data': {'value': 'no', 'base': 'no', 'effect': 0}}],
              'pancreatic':
                [{'factor': 'age', 'data': {'value': 25, 'base': 30, 'effect': -8.75}},
                 {'factor': 'b_chronicpan', 'data': {'value': 'yes', 'base': 'no', 'effect': 8.56}},
                 {'factor': 'b_type2', 'data': {'value': 'yes', 'base': 'no', 'effect': 5.468}},
                 {'factor': 'new_gibleed', 'data': {'value': 'yes', 'base': 'no', 'effect': 6.89}},
                 {'factor': 's1_constipation', 'data': {'value': 'yes', 'base': 'no', 'effect': 18.5}}],
              'prostate':
                [{'factor': 'fh_prostatecancer', 'data': {'value': 'yes', 'base': 'no', 'effect': 4.75}},
                 {'factor': 'age', 'data': {'value': 25, 'base': 30, 'effect': -7.63}},
                 {'factor': 'new_testispain', 'data': {'value': 'yes', 'base': 'no', 'effect': 7.6}},
                 {'factor': 'new_weightloss', 'data': {'value': 'no', 'base': 'no', 'effect': 0}}],
              'renal':
                [{'factor': 'age', 'data': {'value': 36, 'base': 28, 'effect': 1.56}},
                 {'factor': 'bmi', 'data': {'value': 25, 'base': 25, 'effect': 0}},
                 {'factor': 'new_abdopain', 'data': {'value': 'no', 'base': 'no', 'effect': 0}},
                 {'factor': 'new_nightsweats', 'data': {'value': 'yes', 'base': 'no', 'effect': 5.9}},
                 {'factor': 'new_weightloss', 'data': {'value': 'yes', 'base': 'no', 'effect': 4.3}}],
              'testicular':
                [{'factor': 'age', 'data': {'value': 25, 'base': 30, 'effect': -10.9}},
                 {'factor': 'bmi', 'data': {'value': 27, 'base': 25, 'effect': 2.3}},
                 {'factor': 'new_testispain', 'data': {'value': 'yes', 'base': 'no', 'effect': 1.56}},
                 {'factor': 'new_testicularlump', 'data': {'value': 'yes', 'base': 'no', 'effect': 2.5}}],
}

# Change bases here for male
bases_male = {'blood': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'colorectal': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'gastro': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'lung': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'other': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'pancreatic': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'prostate': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'renal': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'testicular': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'})}

def transformAndScaleAgeMale(age):
    # Applying the fractional polynomial transforms (includes scaling)
    dage = age
    dage = dage/10
    age_1 = dage
    age_2 = dage * math.log(dage)

    # Centring the continuous variables
    age_1 = age_1 - 4.800777912139893
    age_2 = age_2 - 7.531354427337647

    return age_1, age_2

def transformAndScaleBMIMale(bmi):
    # Applying the fractional polynomial transforms (includes scaling)
    dbmi = bmi
    dbmi = dbmi/10
    bmi_1 = math.pow(dbmi,-2)
    bmi_2 = dbmi

    # Centring the continuous variables
    bmi_1 = bmi_1 - 0.146067067980766
    bmi_2 = bmi_2 - 2.616518735885620

    return bmi_1, bmi_2

def getAlcoholValue(alco):
    alcohol_values = {"no": 0, "< 1 unit per day": 1, "1-2 units per day": 2, "3+ units per day": 3}
    return alcohol_values[alco]

def getSmokeValue(smoke):
    smoke_values = {"non": 0, "ex": 1, "light": 2, "moderate": 3, "heavy": 4}
    return smoke_values[smoke]

def getCheckboxValue(form, name):
    return 1 if name in form else 0

def getArgsMale(form):
    age_1, age_2 = transformAndScaleAgeMale(int(form['age']))
    bmi_1, bmi_2 = transformAndScaleBMIMale(float(form['bmi']))
    alcohol_cat4 = getAlcoholValue(form['alcohol_cat4'])
    smoke_cat = getSmokeValue(form['smoke_cat'])
    args = {
        "age_1": age_1,
        "age_2": age_2,
        "alcohol_cat4": alcohol_cat4, 
        "b_chronicpan": getCheckboxValue(form, "b_chronicpan"), 
        "b_copd": getCheckboxValue(form, "b_copd"), 
        "b_type2": getCheckboxValue(form, "b_type2"), 
        "bmi_1": bmi_1,
        "bmi_2": bmi_2,
        "c_hb": getCheckboxValue(form, "c_hb"),
        "fh_gicancer": getCheckboxValue(form, "fh_gicancer"),
        "fh_prostatecancer": getCheckboxValue(form, "fh_prostatecancer"),
        "new_abdodist": getCheckboxValue(form, "new_abdodist"),
        "new_abdopain": getCheckboxValue(form, "new_abdopain"),
        "new_appetiteloss": getCheckboxValue(form, "new_appetiteloss"),
        "new_dysphagia": getCheckboxValue(form, "new_dysphagia"),
        "new_gibleed": getCheckboxValue(form, "new_gibleed"),
        "new_haematuria": getCheckboxValue(form, "new_haematuria"),
        "new_haemoptysis": getCheckboxValue(form, "new_haemoptysis"),
        "new_heartburn": getCheckboxValue(form, "new_heartburn"),
        "new_indigestion": getCheckboxValue(form, "new_indigestion"),
        "new_necklump": getCheckboxValue(form, "new_necklump"),
        "new_nightsweats": getCheckboxValue(form, "new_nightsweats"),
        "new_rectalbleed": getCheckboxValue(form, "new_rectalbleed"),
        "new_testispain": getCheckboxValue(form, "new_testispain"),
        "new_testicularlump": getCheckboxValue(form, "new_testicularlump"),
        "new_vte": getCheckboxValue(form, "new_vte"),
        "new_weightloss": getCheckboxValue(form, "new_weightloss"),
        "s1_bowelchange": getCheckboxValue(form, "s1_bowelchange"),
        "s1_constipation": getCheckboxValue(form, "s1_constipation"),
        "s1_cough": getCheckboxValue(form, "s1_cough"),
        "s1_impotence": getCheckboxValue(form, "s1_impotence"),
        "s1_nocturia": getCheckboxValue(form, "s1_nocturia"),
        "s1_urinaryfreq": getCheckboxValue(form, "s1_urinaryfreq"),
        "s1_urinaryretention": getCheckboxValue(form, "s1_urinaryretention"),
        "smoke_cat": smoke_cat,
    }
    return args

def calculateAllScoresMale(args):
    results = [0] * 9
    sum = 1
    
    # list of functions
    all_funcs = [blood_cancer_male, colorectal_cancer_male, gastro_oesophageal_cancer_male, lung_cancer_male,
               other_cancer_male, pancreatic_cancer_male, prostate_cancer_male, renal_tract_cancer_male, testicular_cancer_male]
    
    # calculate each raw score
    for i in range(0, 9):
        results[i] = math.exp(all_funcs[i](args))
        sum += results[i]
    
    # calculate each score as percentage
    for i in range(0, 9):
        results[i] *= 100/sum
    
    return results

# <------------------------- Crucial function 1 ------------------------->
# This function calculates the outputs variable from a given args
def calculateOutputsFromArgsMale(args):
    results = calculateAllScoresMale(args)
    labels = ['Blood', 'Colorectal', 'Gastro', 'Lung',
               'Other', 'Pancreatic', 'Prostate', 'Renal', 'Testicular']
    outputs = {key: value for key, value in zip(labels, results)}
    return outputs
# <------------------------- End of crucial function 1 ------------------------->

# <------------------------- Crucial function 2 ------------------------->
# This function calculates the outputs variable from a given form
def calculateOutputsMale(form):
    args = getArgsMale(form)
    return calculateOutputsFromArgsMale(args)
# <------------------------- End of crucial function 2 ------------------------->

def changeToBase(input, args, factor, base):
    # case 0: the input is the same as the base
    if input == base:
        return (False, {})
    
    args = args.copy()

    # case 1: factor is age
    if factor == 'age':
        age_1, age_2 = transformAndScaleAgeMale(base)
        args['age_1'] = age_1
        args['age_2'] = age_2
        return (True, args)

    # case 2: factor is bmi
    if factor == 'bmi':
        bmi_1, bmi_2 = transformAndScaleBMIMale(base)
        args['bmi_1'] = bmi_1
        args['bmi_2'] = bmi_2
        return (True, args)

    # case 3: factor is alcohol
    if factor == 'alcohol_cat4':
        alcohol_cat4 = getAlcoholValue(base)
        args['alcohol_cat4'] = alcohol_cat4
        return (True, args)

    # case 4: factor is smoke
    if factor == 'smoke_cat':
        smoke_cat = getSmokeValue(base)
        args['smoke_cat'] = smoke_cat
        return (True, args)

    # case 5: factor is boolean
    args[factor] = 0 if base == 'no' else 1
    return (True, args)

def getCheckboxInputValue(form, name):
    return 'yes' if name in form else 'no'

# This is to be used to put in the data dictionary of all_data
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

# <------------------------- Crucial function 3 ------------------------->
# This function calculates the all_data variable
def calculateAllDataMale(form, outputs):
    inputs = getInputsMale(form)
    args = getArgsMale(form)
    all_data = {'blood': [], 'colorectal':[], 'gastro': [], 'lung': [], 'other': [], 'pancreatic': [], 
                    'prostate': [], 'renal': [], 'testicular': []}
    for cancer_type in all_data:
        for factor in inputs:
            change, base_args = changeToBase(inputs[factor], args, factor, bases_male[cancer_type][factor])
            if change:
                base_outputs = calculateOutputsFromArgsMale(base_args)
                all_data[cancer_type].append({'factor': factor, 'data': {'value': inputs[factor], 
                'base': bases_male[cancer_type][factor], 'effect': outputs[cancer_type.capitalize()] - base_outputs[cancer_type.capitalize()]}})
        # Only keep the six most effective factors
        all_data[cancer_type] = sorted(all_data[cancer_type], key=lambda d: abs(d['data']['effect']), reverse=True)[:6]

    return all_data
# <------------------------- End of crucial function 3 ------------------------->

# <================================ End of Male Part ================================>


# <================================ Female part ================================>

# Change bases here for female
bases_female = {'blood': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'breast': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'cervical': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'colorectal': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'gastro': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'lung': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'other': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'ovarian': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}), 
        'pancreatic': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}),
        'renal': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'}),
        'uterine': defaultdict(lambda: 'no', {'age': 25, 'bmi': 25, 'alcohol_cat4': 'no', 'smoke_cat': 'non'})}

def transformAndScaleAgeFemale(age):
    # Applying the fractional polynomial transforms (includes scaling)
    dage = age
    dage /= 10
    age_1 = dage ** -2
    age_2 = age_1 * math.log(dage)

	# Centring the continuous variables
    age_1 = age_1 - 0.039541322737932
    age_2 = age_2 - 0.063867323100567

    return age_1, age_2

def transformAndScaleBMIFemale(bmi):
    # Applying the fractional polynomial transforms (includes scaling)
    dbmi = bmi
    dbmi /= 10
    bmi_1 = dbmi ** -2
    bmi_2 = bmi_1 * math.log(dbmi)

	# Centring the continuous variables
    bmi_1 = bmi_1 - 0.151021569967270
    bmi_2 = bmi_2 - 0.142740502953529

    return bmi_1, bmi_2

def getArgsFemale(form):
    age_1, age_2 = transformAndScaleAgeFemale(int(form['age']))
    bmi_1, bmi_2 = transformAndScaleBMIFemale(float(form['bmi']))
    alcohol_cat4 = getAlcoholValue(form['alcohol_cat4'])
    smoke_cat = getSmokeValue(form['smoke_cat'])

    args = {
        "age_1": age_1,
        "age_2": age_2, 
        "alcohol_cat4": alcohol_cat4, 
        "b_chronicpan": getCheckboxValue(form, "b_chronicpan"), 
        "b_copd": getCheckboxValue(form, "b_copd"), 
        "b_endometrial": getCheckboxValue(form, "b_endometrial"), 
        "b_type2": getCheckboxValue(form, "b_type2"), 
        "bmi_1": bmi_1,
        "bmi_2": bmi_2, 
        "c_hb": getCheckboxValue(form, "c_hb"), 
        "fh_breastcancer": getCheckboxValue(form, "fh_breastcancer"), 
        "fh_gicancer": getCheckboxValue(form, "fh_gicancer"), 
        "fh_ovariancancer": getCheckboxValue(form, "fh_ovariancancer"), 
        "new_abdodist": getCheckboxValue(form, "new_abdodist"), 
        "new_abdopain": getCheckboxValue(form, "new_abdopain"), 
        "new_appetiteloss": getCheckboxValue(form, "new_appetiteloss"), 
        "new_breastlump": getCheckboxValue(form, "new_breastlump"), 
        "new_breastpain": getCheckboxValue(form, "new_breastpain"), 
        "new_breastskin": getCheckboxValue(form, "new_breastskin"), 
        "new_dysphagia": getCheckboxValue(form, "new_dysphagia"), 
        "new_gibleed": getCheckboxValue(form, "new_gibleed"), 
        "new_haematuria": getCheckboxValue(form, "new_haematuria"), 
        "new_haemoptysis": getCheckboxValue(form, "new_haemoptysis"), 
        "new_heartburn": getCheckboxValue(form, "new_heartburn"), 
        "new_imb": getCheckboxValue(form, "new_imb"), 
        "new_indigestion": getCheckboxValue(form, "new_indigestion"), 
        "new_necklump": getCheckboxValue(form, "new_necklump"), 
        "new_nightsweats": getCheckboxValue(form, "new_nightsweats"), 
        "new_pmb": getCheckboxValue(form, "new_pmb"), 
        "new_postcoital": getCheckboxValue(form, "new_postcoital"), 
        "new_rectalbleed": getCheckboxValue(form, "new_rectalbleed"), 
        "new_vte": getCheckboxValue(form, "new_vte"), 
        "new_weightloss": getCheckboxValue(form, "new_weightloss"), 
        "s1_bowelchange": getCheckboxValue(form, "s1_bowelchange"), 
        "s1_bruising": getCheckboxValue(form, "s1_bruising"), 
        "s1_constipation": getCheckboxValue(form, "s1_constipation"), 
        "s1_cough": getCheckboxValue(form, "s1_cough"), 
        "smoke_cat": smoke_cat,
    }
    return args

def calculateAllScoresFemale(args):
    results = [0] * 11
    sum = 1
    
    # list of functions
    all_funcs = [blood_cancer_female, breast_cancer_female, cervical_cancer_female, colorectal_cancer_female, gastro_oesophageal_cancer_female,
                 lung_cancer_female, other_cancer_female, ovarian_cancer_female, pancreatic_cancer_female, renal_tract_cancer_female, uterine_cancer_female]
    
    # calculate each raw score
    for i in range(0, 11):
        results[i] = math.exp(all_funcs[i](args))
        sum += results[i]
    
    # calculate each score as percentage
    for i in range(0, 11):
        results[i] *= 100/sum
    
    return results

# <------------------------- Crucial function 1 ------------------------->
# This function calculates the outputs variable from a given args
def calculateOutputsFromArgsFemale(args):
    results = calculateAllScoresFemale(args)
    labels = ["Blood", "Breast", "Cervical", "Colorectal", "Gastro","Lung","Other", "Ovarian", "Pancreatic", "Renal", "Uterine"]
    outputs = {key: value for key, value in zip(labels, results)}
    return outputs
# <------------------------- End of crucial function 1 ------------------------->

# <------------------------- Crucial function 2 ------------------------->
# This function calculates the outputs variable from a given form
def calculateOutputsFemale(form):
    args = getArgsFemale(form)
    return calculateOutputsFromArgsFemale(args)
# <------------------------- End of crucial function 2 ------------------------->

# This is to be used to put in the data dictionary of all_data
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

# <------------------------- Crucial function 3 ------------------------->
# This function calculates the all_data variable
def calculateAllDataFemale(form, outputs):
    inputs = getInputsFemale(form)
    args = getArgsFemale(form)
    all_data = {"blood": [], "breast": [], "cervical": [], "colorectal": [], "gastro": [], "lung": [], 
                "other": [], "ovarian": [], "pancreatic": [], "renal": [], "uterine": []}
    for cancer_type in all_data:
        for factor in inputs:
            change, base_args = changeToBase(inputs[factor], args, factor, bases_female[cancer_type][factor])
            if change:
                base_outputs = calculateOutputsFromArgsFemale(base_args)
                all_data[cancer_type].append({'factor': factor, 'data': {'value': inputs[factor], 
                'base': bases_female[cancer_type][factor], 'effect': outputs[cancer_type.capitalize()] - base_outputs[cancer_type.capitalize()]}})
        # Only keep the six most effective factors
        all_data[cancer_type] = sorted(all_data[cancer_type], key=lambda d: abs(d['data']['effect']), reverse=True)[:6]

    return all_data
# <------------------------- End of crucial function 3 ------------------------->

# <================================ End of Female Part ================================>