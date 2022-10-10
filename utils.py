import math
import numpy as np
from collections import defaultdict

from bases import bases_male, bases_female, male_input, female_input, getInputsMale, getInputsFemale, male_base_array, female_base_array
from shap_exp import getInputArray, transform_input, male_function, female_function

# Labels to be shown on the output page
male_labels = {'blood': 'Blood', 'colorectal': 'Colorectal', 'gastro': 'Gastro-oesophageal', 'lung': 'Lung',
               'other': 'Other', 'pancreatic': 'Pancreatic', 'prostate': 'Prostate', 'renal': 'Renal tract', 'testicular': 'Testicular'}
female_labels = {"blood": 'Blood', "breast": 'Breast', "cervical": 'Cervical', "colorectal": 'Colorectal',
                 "gastro": 'Gastro-oesophageal', "lung": 'Lung', "other": 'Other', "ovarian": 'Ovarian', 
                 "pancreatic": 'Pancreatic', "renal": 'Renal tract', "uterine": 'Uterine'}

# <================================ qcancer cmd part ================================>
def is_boolean(b):
    return isinstance(b, bool)

def in_range(x, min, max):
    return x >= min and x <= max

def check_range_bool(b):
    if (not in_range(b, 0, 1)):
        raise Exception("The value must be either 0 or 1")

# <================================ input part (for male and female) ================================>


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

# <------------------------- Crucial function 1 ------------------------->
# This function calculates the outputs variable from a given form
def calculateOutputsMale(form):
    input_arr = getInputArray(form, True)
    raw_output = male_function(input_arr.reshape(1, -1))[0]
    labels = ['blood', 'colorectal', 'gastro', 'lung',
               'other', 'pancreatic', 'prostate', 'renal', 'testicular']
    outputs = {key: value for key, value in zip(labels, raw_output)}
    return outputs
# <------------------------- End of crucial function 1 ------------------------->

# <------------------------- Crucial function 2 ------------------------->
# This function calculates the all_data variable
def calculateAllDataMale(form, outputs):
    inputs = getInputsMale(form)
    input_array = getInputArray(form, isMale=True)
    all_data = {'blood': [], 'colorectal':[], 'gastro': [], 'lung': [], 'other': [], 'pancreatic': [], 
                    'prostate': [], 'renal': [], 'testicular': []}
    for cancer_type_index, cancer_type in enumerate(all_data):
        # list of indices whose value is not the baseline
        change_indices = np.nonzero(input_array - male_base_array)[0]
        for change_index in change_indices:
            factor = male_input[change_index]
            change_array = input_array.copy()
            change_array[change_index] = male_base_array[change_index]
            base_output = male_function(change_array.reshape(1, -1))[0][cancer_type_index]
            all_data[cancer_type].append({'factor': factor, 'data': {'value': inputs[factor], 
                'base': bases_male[cancer_type][factor], 'effect': outputs[cancer_type] - base_output}})
        # Only keep the six most effective factors
        all_data[cancer_type] = sorted(all_data[cancer_type], key=lambda d: abs(d['data']['effect']), reverse=True)[:6]

    return all_data
# <------------------------- End of crucial function 2 ------------------------->

# <================================ End of Male Part ================================>


# <================================ Female part ================================>

# <------------------------- Crucial function 1 ------------------------->
# This function calculates the outputs variable from a given form
def calculateOutputsFemale(form):
    input_arr = getInputArray(form, isMale=False)
    raw_output = female_function(input_arr.reshape(1, -1))[0]
    labels = ["blood", "breast", "cervical", "colorectal", "gastro", "lung", "other", "ovarian", "pancreatic", "renal", "uterine"]
    outputs = {key: value for key, value in zip(labels, raw_output)}
    return outputs
# <------------------------- End of crucial function 1 ------------------------->

# <------------------------- Crucial function 2 ------------------------->
# This function calculates the all_data variable
def calculateAllDataFemale(form, outputs):
    inputs = getInputsFemale(form)
    input_array = getInputArray(form, isMale=False)
    all_data = {"blood": [], "breast": [], "cervical": [], "colorectal": [], "gastro": [], "lung": [], 
                "other": [], "ovarian": [], "pancreatic": [], "renal": [], "uterine": []}
    for cancer_type_index, cancer_type in enumerate(all_data):
        # list of indices whose value is not the baseline
        change_indices = np.nonzero(input_array - female_base_array)[0]
        for change_index in change_indices:
            factor = female_input[change_index]
            change_array = input_array.copy()
            change_array[change_index] = female_base_array[change_index]
            base_output = female_function(change_array.reshape(1, -1))[0][cancer_type_index]
            all_data[cancer_type].append({'factor': factor, 'data': {'value': inputs[factor], 
                'base': bases_female[cancer_type][factor], 'effect': outputs[cancer_type] - base_output}})
        # Only keep the six most effective factors
        all_data[cancer_type] = sorted(all_data[cancer_type], key=lambda d: abs(d['data']['effect']), reverse=True)[:6]

    return all_data
# <------------------------- End of crucial function 2 ------------------------->

# <================================ End of Female Part ================================>