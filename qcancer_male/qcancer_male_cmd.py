import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils import in_range, check_range_bool
from qcancer_male_funcs import *
import math

def calculateAllScores(args):
  results = [0] * 10
  sum = 1

  # list of functions
  all_funcs = [blood_cancer_male, colorectal_cancer_male, gastro_oesophageal_cancer_male, lung_cancer_male,
               other_cancer_male, pancreatic_cancer_male, prostate_cancer_male, renal_tract_cancer_male, testicular_cancer_male]

  # calculate each raw score
  for i in range(1, 10):
    results[i] = math.exp(all_funcs[i-1](args))
    sum += results[i]
  
  sum2 = 0

  # calculate each score as percentage
  for i in range(1, 10):
    results[i] *= 100/sum
    sum2 += results[i]
  
  results[0] = 100 - sum2

  return results


def main():
  # input and validate data
  age = int(input("Please input your age: "))
  if (not in_range(age, 25, 89)):
    raise Exception("age must be in range [25,89]")
  
  alcohol_cat4 = int(input("""How often do you drink alcohols?
    0: non-drinker
    1: < 1 unit per day
    2: 1-2 units per day
    3: 3+ units per day
    : """))
  if (not in_range(alcohol_cat4, 0, 3)):
    raise Exception("The value must be in range [0,3]")

  b_chronicpan = int(input("Do you have chronic pancreatitis? (0: No, 1: Yes): "))
  check_range_bool(b_chronicpan)

  b_copd = int(input("Do you have chronic obstructive airways disease (COPD)? (0: No, 1: Yes): "))
  check_range_bool(b_copd)

  b_type2 = int(input("Do you have type 2 diabetes?	(0: No, 1: Yes): "))
  check_range_bool(b_type2)

  bmi = float(input("What is your bmi?: "))
  if (not in_range(bmi, 20, 40)):
    raise Exception("BMI must be in range [20,40]")

  c_hb = int(input("In the last year have you seen your GP with anaemia (Haemoglobin < 11g/dL)? (0: No, 1: Yes): "))
  check_range_bool(c_hb)

  fh_gicancer = int(input("Has anyone in your family ever had a gastrointestinal cancer? (0: No, 1: Yes): "))
  check_range_bool(fh_gicancer)

  fh_prostatecancer = int(input("Do you have a family history of prostate cancer? (0: No, 1: Yes): "))
  check_range_bool(fh_prostatecancer)

  new_abdodist = int(input("Do you currently have an abdominal swelling? (0: No, 1: Yes): "))
  check_range_bool(new_abdodist)

  new_abdopain = int(input("Do you currently have an abdominal pain? (0: No, 1: Yes): "))
  check_range_bool(new_abdopain)

  new_appetiteloss = int(input("Do you currently have a loss of appetite? (0: No, 1: Yes): "))
  check_range_bool(new_appetiteloss)

  new_dysphagia = int(input("Do you currently have difficulty swallowing? (0: No, 1: Yes): "))
  check_range_bool(new_dysphagia)

  new_gibleed = int(input("Do you currently have blood when you vomit? (0: No, 1: Yes): "))
  check_range_bool(new_gibleed)

  new_haematuria = int(input("Do you currently have blood in your urine? (0: No, 1: Yes): "))
  check_range_bool(new_haematuria)

  new_haemoptysis = int(input("Do you currently have blood when you cough? (0: No, 1: Yes): "))
  check_range_bool(new_haemoptysis)

  new_heartburn = int(input("Do you currently have heartburn? (0: No, 1: Yes): "))
  check_range_bool(new_heartburn)

  new_indigestion = int(input("Do you currently have indigestion? (0: No, 1: Yes): "))
  check_range_bool(new_indigestion)

  new_necklump = int(input("Do you currently have a lump in your neck? (0: No, 1: Yes): "))
  check_range_bool(new_necklump)

  new_nightsweats = int(input("Do you currently have night sweats? (0: No, 1: Yes): "))
  check_range_bool(new_nightsweats)

  new_rectalbleed = int(input("Do you currently have rectal bleeding? (0: No, 1: Yes): "))
  check_range_bool(new_rectalbleed)

  new_testispain = int(input("Do you currently have testicular pain? (0: No, 1: Yes): "))
  check_range_bool(new_testispain)

  new_testicularlump = int(input("Do you currently have a testicular lump? (0: No, 1: Yes): "))
  check_range_bool(new_testicularlump)

  new_vte = int(input("Do you currently have a venous thromboembolism? (0: No, 1: Yes): "))
  check_range_bool(new_vte)

  new_weightloss = int(input("Do you currently have unintentional weight loss? (0: No, 1: Yes): "))
  check_range_bool(new_weightloss)

  s1_bowelchange = int(input("In the last year have you seen your GP with change in bowel habit? (0: No, 1: Yes): "))
  check_range_bool(s1_bowelchange)

  s1_constipation = int(input("In the last year have you seen your GP with constipation? (0: No, 1: Yes): "))
  check_range_bool(s1_constipation)

  s1_cough = int(input("In the last year have you seen your GP with cough? (0: No, 1: Yes): "))
  check_range_bool(s1_cough)

  s1_impotence = int(input("In the last year have you seen your GP with impotence? (0: No, 1: Yes): "))
  check_range_bool(s1_impotence)

  s1_nocturia = int(input("In the last year have you seen your GP with nocturia (passing urine at night)? (0: No, 1: Yes): "))
  check_range_bool(s1_nocturia)
  
  s1_urinaryfreq = int(input("In the last year have you seen your GP with urinary frequency? (0: No, 1: Yes): "))
  check_range_bool(s1_urinaryfreq)

  s1_urinaryretention = int(input("In the last year have you seen your GP with urinary retention? (0: No, 1: Yes): "))
  check_range_bool(s1_urinaryretention)

  smoke_cat = int(input("""What is your smoking status?
    0: non-smoker
    1: ex-smoker
    2: light smoker (less than 10)
    3: moderate smoker (10 to 19)
    4: heavy smoker (20 or over)
    : """))
  if (not in_range(smoke_cat, 0, 4)):
    raise Exception("The value must be in range [0, 4]")
  
  # Applying the fractional polynomial transforms (includes scaling)
  dage = age
  dage = dage/10
  age_1 = dage
  age_2 = dage * math.log(dage)
  dbmi = bmi
  dbmi = dbmi/10
  bmi_1 = math.pow(dbmi,-2)
  bmi_2 = dbmi

  # Centring the continuous variables
  age_1 = age_1 - 4.800777912139893
  age_2 = age_2 - 7.531354427337647
  bmi_1 = bmi_1 - 0.146067067980766
  bmi_2 = bmi_2 - 2.616518735885620

  # end of polynomial transform

  # create a dictionary to hold all the inputs
  args = {
    "age_1": age_1,
    "age_2": age_2,
    "alcohol_cat4": alcohol_cat4, 
    "b_chronicpan": b_chronicpan, 
    "b_copd": b_copd, 
    "b_type2": b_type2, 
    "bmi_1": bmi_1,
    "bmi_2": bmi_2,
    "c_hb": c_hb,
    "fh_gicancer": fh_gicancer,
    "fh_prostatecancer": fh_prostatecancer,
    "new_abdodist": new_abdodist,
    "new_abdopain": new_abdopain,
    "new_appetiteloss": new_appetiteloss,
    "new_dysphagia": new_dysphagia,
    "new_gibleed": new_gibleed,
    "new_haematuria": new_haematuria,
    "new_haemoptysis": new_haemoptysis,
    "new_heartburn": new_heartburn,
    "new_indigestion": new_indigestion,
    "new_necklump": new_necklump,
    "new_nightsweats": new_nightsweats,
    "new_rectalbleed": new_rectalbleed,
    "new_testispain": new_testispain,
    "new_testicularlump": new_testicularlump,
    "new_vte": new_vte,
    "new_weightloss": new_weightloss,
    "s1_bowelchange": s1_bowelchange,
    "s1_constipation": s1_constipation,
    "s1_cough": s1_cough,
    "s1_impotence": s1_impotence,
    "s1_nocturia": s1_nocturia,
    "s1_urinaryfreq": s1_urinaryfreq,
    "s1_urinaryretention": s1_urinaryretention,
    "smoke_cat": smoke_cat,
  }

  # calculate all the scores
  results = calculateAllScores(args)

  # print the scores
  all_cancer_types = ["none","blood_cancer","colorectal_cancer","gastro_oesophageal_cancer",
  "lung_cancer","other_cancer","pancreatic_cancer","prostate_cancer","renal_tract_cancer","testicular_cancer"]

  print("-----------------------------------------------------------")
  print("Results")
  print("-----------------------------------------------------------")

  for (i, cancer_name) in enumerate(all_cancer_types):
    print(f"{cancer_name:<30}", f"{results[i]:<25}%")

if __name__ == "__main__":
  main()