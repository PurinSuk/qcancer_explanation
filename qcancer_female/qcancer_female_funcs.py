def blood_cancer_female(args):
  score = 0

  score += args["age_1"] * 35.9405666896283120000000000
  score += args["age_2"] * -68.8496375977904480000000000
  score += args["bmi_1"] * 0.0785171223057501980000000
  score += args["bmi_2"] * -5.3730627788681424000000000

  score += args["c_hb"] * 1.7035866502297630000000000
  score += args["new_abdopain"] * 0.3779206239385797800000000
  score += args["new_haematuria"] * 0.4086662974598894700000000
  score += args["new_necklump"] * 2.9539029476671903000000000
  score += args["new_nightsweats"] * 1.3792892192392403000000000
  score += args["new_pmb"] * 0.4689216313440992500000000
  score += args["new_vte"] * 0.6036630662990674100000000
  score += args["new_weightloss"] * 0.8963398932306315700000000
  score += args["s1_bowelchange"] * 0.7291379612468620300000000
  score += args["s1_bruising"] * 1.0255003552753392000000000

  return score - 7.4207849482565749000000000

def breast_cancer_female(args):
  score = 0

  Ialcohol = [0, 0.0543813075945134560000000, 0.1245709972983817800000000, 0.1855198679261514700000000]

  score += Ialcohol[args["alcohol_cat4"]]

  score += args["age_1"] * -14.3029484067898500000000000
  score += args["age_2"] * -25.9301811377364260000000000
  score += args["bmi_1"] * -1.7540983825680900000000000
  score += args["bmi_2"] * 2.0601979121740364000000000

  score += args["fh_breastcancer"] * 0.3863899675953914000000000
  score += args["new_breastlump"] * 3.9278533274888368000000000
  score += args["new_breastpain"] * 0.8779616078329102200000000
  score += args["new_breastskin"] * 2.2320296233987880000000000
  score += args["new_pmb"] * 0.4465053002248299800000000
  score += args["new_vte"] * 0.2728610297213165400000000

  return score - 6.1261694200869234000000000

def cervical_cancer_female(args):
  score = 0

  Ismoke =[0, 0.3247875277095715300000000, 0.7541211259076738800000000, 0.7448343035139659600000000, 0.6328348533913806800000000]

  score += Ismoke[args["smoke_cat"]]

  score += args["age_1"] * 10.1663393107505800000000000
  score += args["age_2"] * -16.9118902491100020000000000
  score += args["bmi_1"] * -0.5675143308052614800000000
  score += args["bmi_2"] * -2.6377586334504044000000000

  score += args["c_hb"] * 1.2205973555195053000000000
  score += args["new_abdopain"] * 0.7229870191773574200000000
  score += args["new_haematuria"] * 1.6126499968790107000000000
  score += args["new_imb"] * 1.9527008812518938000000000
  score += args["new_pmb"] * 3.3618997560756485000000000
  score += args["new_postcoital"] * 3.1391568551730864000000000
  score += args["new_vte"] * 1.1276327958138455000000000

  return score - 8.8309098444401926000000000

def colorectal_cancer_female(args):
  score = 0

  Ialcohol = [0, 0.2429014262884695900000000, 0.2359224520197608100000000, 0.4606605934539446100000000]

  score += Ialcohol[args["alcohol_cat4"]]

  score += args["age_1"] * -11.6175606616390770000000000
  score += args["age_2"] * -42.9098057686870220000000000
  score += args["bmi_1"] * -0.5344237822753052900000000
  score += args["bmi_2"] * 2.6900552265408226000000000

  score += args["c_hb"] * 1.4759238359186861000000000
  score += args["fh_gicancer"] * 0.4044501048847998200000000
  score += args["new_abdodist"] * 0.6630074287856559900000000
  score += args["new_abdopain"] * 1.4990872468711913000000000
  score += args["new_appetiteloss"] * 0.5068020107261922400000000
  score += args["new_rectalbleed"] * 2.7491673095810105000000000
  score += args["new_vte"] * 0.7072816884002932600000000
  score += args["new_weightloss"] * 1.0288860866585736000000000
  score += args["s1_bowelchange"] * 0.7664414123199643200000000
  score += args["s1_constipation"] * 0.3375158123121173600000000

  return score - 7.5466948789670942000000000

def gastro_oesophageal_cancer_female(args):
  score = 0

  Ismoke = [0, 0.2108835385994093400000000, 0.4020914846651602000000000, 0.8497119766959212500000000, 1.1020585469724540000000000]

  score += Ismoke[args["smoke_cat"]]

  score += args["age_1"] * 5.5127932958160830000000000
  score += args["age_2"] * -70.2734062916161830000000000
  score += args["bmi_1"] * 2.6063377632938987000000000
  score += args["bmi_2"] * -1.2389834515079798000000000

  score += args["c_hb"] * 1.2479756970482034000000000
  score += args["new_abdopain"] * 0.7825304005124729100000000
  score += args["new_appetiteloss"] * 0.6514592236889243900000000
  score += args["new_dysphagia"] * 3.7751714910656862000000000
  score += args["new_gibleed"] * 1.4264472204617833000000000
  score += args["new_heartburn"] * 0.8178746069193373300000000
  score += args["new_indigestion"] * 1.4998439683677578000000000
  score += args["new_vte"] * 0.7199894658172598700000000
  score += args["new_weightloss"] * 1.2287925630053846000000000

  return score - 8.8746031610250764000000000

def lung_cancer_female(args):
  score = 0

  Ismoke = [0, 1.3397416191950409000000000, 1.9500839456663224000000000, 2.1881694694325233000000000, 2.4828660433307768000000000]

  score += Ismoke[args["smoke_cat"]]

  score += args["age_1"] * -117.2405737502962500000000000
  score += args["age_2"] * 25.1702254741268090000000000
  score += args["bmi_1"] * 2.5845488133924350000000000
  score += args["bmi_2"] * -0.6083523966762799400000000

  score += args["b_copd"] * 0.7942901962671364800000000
  score += args["c_hb"] * 0.8627980324401628400000000
  score += args["new_appetiteloss"] * 0.7170232121379446200000000
  score += args["new_dysphagia"] * 0.6718426806077323300000000
  score += args["new_haemoptysis"] * 2.9286439157734474000000000
  score += args["new_indigestion"] * 0.3634893730114273600000000
  score += args["new_necklump"] * 1.2097240380091590000000000
  score += args["new_vte"] * 0.8907072670032341000000000
  score += args["new_weightloss"] * 1.1384524885073082000000000
  score += args["s1_cough"] * 0.6439917053275602300000000

  return score - 8.6449002971789692000000000

def other_cancer_female(args):
  score = 0

  Ialcohol = [0, 0.1129292517088995400000000, 0.1389183205617967600000000, 0.3428114766789586200000000]
  Ismoke = [0, 0.0643839792551647580000000, 0.1875068101660691500000000, 0.3754052152821668000000000, 0.5007337952210844100000000]

  score += Ialcohol[args["alcohol_cat4"]]
  score += Ismoke[args["smoke_cat"]]

  score += args["age_1"] * 35.8208987302204780000000000
  score += args["age_2"] * -68.3294741037719150000000000
  score += args["bmi_1"] * 1.8969796480108396000000000
  score += args["bmi_2"] * -3.7755945945329574000000000

  score += args["b_copd"] * 0.2823021429107943600000000
  score += args["c_hb"] * 1.0476364795173587000000000
  score += args["new_abdodist"] * 0.9628688090459262000000000
  score += args["new_abdopain"] * 0.8335710066715610300000000
  score += args["new_appetiteloss"] * 0.8450972438476546100000000
  score += args["new_breastlump"] * 1.0400807427059522000000000
  score += args["new_dysphagia"] * 0.8905342895684595900000000
  score += args["new_gibleed"] * 0.3839632265134078600000000
  score += args["new_haematuria"] * 0.6143184647549447800000000
  score += args["new_indigestion"] * 0.2457016002992454300000000
  score += args["new_necklump"] * 2.1666504706191545000000000
  score += args["new_pmb"] * 0.4219383252623540900000000
  score += args["new_vte"] * 1.0630784861733920000000000
  score += args["new_weightloss"] * 1.1058752771736007000000000
  score += args["s1_constipation"] * 0.3780143641299491500000000

  return score - 6.7864501668594306000000000

def ovarian_cancer_female(args):
  score = 0

  score += args["age_1"] * -61.0831814462568940000000000
  score += args["age_2"] * 20.3028612701106890000000000
  score += args["bmi_1"] * -2.1261135335028407000000000
  score += args["bmi_2"] * 3.2168200408772472000000000

  score += args["c_hb"] * 1.3625636791018674000000000
  score += args["fh_ovariancancer"] * 1.9951774809951830000000000
  score += args["new_abdodist"] * 2.9381020883363806000000000
  score += args["new_abdopain"] * 1.7307824546132513000000000
  score += args["new_appetiteloss"] * 1.0606947909647773000000000
  score += args["new_haematuria"] * 0.4958835997468107900000000
  score += args["new_indigestion"] * 0.3843731027493998400000000
  score += args["new_pmb"] * 1.5869592940878865000000000
  score += args["new_vte"] * 1.6839747529852673000000000
  score += args["new_weightloss"] * 0.4774332393821720800000000
  score += args["s1_bowelchange"] * 0.6849850007182314300000000

  return score - 7.5609929644491318000000000

def pancreatic_cancer_female(args):
  score = 0

  Ismoke = [0, -0.0631301848152044240000000, 0.3523695950528934500000000, 0.7146003670327156800000000, 0.8073207410335441200000000]

  score += Ismoke[args["smoke_cat"]]

  score += args["age_1"] * -6.8219654517231225000000000
  score += args["age_2"] * -65.6404897305188650000000000
  score += args["bmi_1"] * 3.9715559458995728000000000
  score += args["bmi_2"] * -3.1161107999130500000000000

  score += args["b_chronicpan"] * 1.1948138830441282000000000
  score += args["b_type2"] * 0.7951745325664703000000000
  score += args["new_abdopain"] * 1.9230379689782926000000000
  score += args["new_appetiteloss"] * 1.5209568259888571000000000
  score += args["new_dysphagia"] * 1.0107551560302726000000000
  score += args["new_gibleed"] * 0.9324059153254259400000000
  score += args["new_indigestion"] * 1.1134012616631439000000000
  score += args["new_vte"] * 1.4485586969016084000000000
  score += args["new_weightloss"] * 1.5791912580663912000000000
  score += args["s1_bowelchange"] * 0.9361738611941444700000000

  return score - 9.2782129678657608000000000

def renal_tract_cancer_female(args):
  score = 0

  Ismoke = [0, 0.2752175727739372700000000, 0.5498656631475861100000000, 0.6536242182136680100000000, 0.9053763661785879700000000]

  score += Ismoke[args["smoke_cat"]]

  score += args["age_1"] * -0.0323226569626617470000000
  score += args["age_2"] * -56.3551410786635780000000000
  score += args["bmi_1"] * 1.2103910535779330000000000
  score += args["bmi_2"] * -4.7221299079939785000000000

  score += args["c_hb"] * 1.2666531852544143000000000
  score += args["new_abdopain"] * 0.6155954984707594500000000
  score += args["new_appetiteloss"] * 0.6842184594676019600000000
  score += args["new_haematuria"] * 4.1791444537241542000000000
  score += args["new_indigestion"] * 0.5694329224821874600000000
  score += args["new_pmb"] * 1.2541097882792864000000000
  score += args["new_weightloss"] * 0.7711610560290518300000000

  return score - 8.9440775553776248000000000

def uterine_cancer_female(args):
  score = 0

  score += args["age_1"] * 2.7778124257317254000000000
  score += args["age_2"] * -59.5333514566633330000000000
  score += args["bmi_1"] * 3.7623897936404322000000000
  score += args["bmi_2"] * -26.8045450074654320000000000

  score += args["b_endometrial"] * 0.8742311851235286000000000
  score += args["b_type2"] * 0.2655181024063555900000000
  score += args["new_abdopain"] * 0.6891953836735580400000000
  score += args["new_haematuria"] * 1.6798617740998527000000000
  score += args["new_imb"] * 1.7853122923827887000000000
  score += args["new_pmb"] * 4.4770199876067398000000000
  score += args["new_vte"] * 1.0362058616761669000000000

  return score - 8.9931390822564037000000000