import numpy as np
import shap
from bases import *

# <============================== Background for features ==============================>
# male_input = ["age", "alcohol_cat4", "b_chronicpan", "b_copd", "b_type2", 
# "bmi", "c_hb", "fh_gicancer", "fh_prostatecancer", "new_abdodist", "new_abdopain", "new_appetiteloss", "new_dysphagia",
# "new_gibleed", "new_haematuria", "new_haemoptysis", "new_heartburn", "new_indigestion", "new_necklump", "new_nightsweats", "new_rectalbleed",
# "new_testispain", "new_testicularlump", "new_vte", "new_weightloss", "s1_bowelchange", "s1_constipation", "s1_cough", "s1_impotence",
# "s1_nocturia", "s1_urinaryfreq", "s1_urinaryretention", "smoke_cat"]

# Male Features (used in cancer risk calculation):
# "age_1", "age_2", "alcohol_cat4_0", "alcohol_cat4_1", "alcohol_cat4_2", "alcohol_cat4_3", "b_chronicpan", "b_copd", "b_type2", 
# "bmi_1", "bmi_2", "c_hb", "fh_gicancer", "fh_prostatecancer", "new_abdodist", "new_abdopain", "new_appetiteloss", "new_dysphagia",
# "new_gibleed", "new_haematuria", "new_haemoptysis", "new_heartburn", "new_indigestion", "new_necklump", "new_nightsweats", "new_rectalbleed",
# "new_testispain", "new_testicularlump", "new_vte", "new_weightloss", "s1_bowelchange", "s1_constipation", "s1_cough", "s1_impotence",
# "s1_nocturia", "s1_urinaryfreq", "s1_urinaryretention", "smoke_cat_0", "smoke_cat_1", "smoke_cat_2", "smoke_cat_3", "smoke_cat_4"

# female_input = ["age", "alcohol_cat4", "b_chronicpan", "b_copd", "b_endometrial",
# "b_type2", "bmi", "c_hb", "fh_breastcancer", "fh_gicancer", "fh_ovariancancer", "new_abdodist", "new_abdopain",
# "new_appetiteloss", "new_breastlump", "new_breastpain", "new_breastskin", "new_dysphagia", "new_gibleed", "new_haematuria", 
# "new_haemoptysis", "new_heartburn", "new_imb", "new_indigestion", "new_necklump", "new_nightsweats", "new_pmb", "new_postcoital",
# "new_rectalbleed", "new_vte", "new_weightloss", "s1_bowelchange", "s1_bruising", "s1_constipation", "s1_cough",
# "smoke_cat"]

# Female Features (used in cancer risk calculation):
# "age_1", "age_2", "alcohol_cat4_0", "alcohol_cat4_1", "alcohol_cat4_2", "alcohol_cat4_3", "b_chronicpan", "b_copd", "b_endometrial",
# "b_type2", "bmi_1", "bmi_2", "c_hb", "fh_breastcancer", "fh_gicancer", "fh_ovariancancer", "new_abdodist", "new_abdopain",
# "new_appetiteloss", "new_breastlump", "new_breastpain", "new_breastskin", "new_dysphagia", "new_gibleed", "new_haematuria", 
# "new_haemoptysis", "new_heartburn", "new_imb", "new_indigestion", "new_necklump", "new_nightsweats", "new_pmb", "new_postcoital",
# "new_rectalbleed", "new_vte", "new_weightloss", "s1_bowelchange", "s1_bruising", "s1_constipation", "s1_cough",
# "smoke_cat_0", "smoke_cat_1", "smoke_cat_2", "smoke_cat_3", "smoke_cat_4"

male_cancers = ['blood', 'colorectal', 'gastro', 'lung', 'other', 'pancreatic', 'prostate', 'renal', 'testicular']

female_cancers = ["blood", "breast", "cervical", "colorectal", "gastro", "lung", "other", "ovarian", "pancreatic", "renal", "uterine"]

# <================================= Part 1: Matrices to be used for cancer risk calculation =================================>
# matrix to be used to calculate cancer risks for males
male_matrix = np.array([
    [3.497017935455661, -1.0806801421562633, 0, 0, 0, 0, 0, 0, 0, 
    0.95192594795117924, 0.17146693584100858, 1.8905802113004144, 0, 0, 0.84304321972113938, 0.62264732882949925, 1.067215038075376, 0.5419443056595199,
    0, 0.46075380853635217, 0.95014468992418366, 0, 0.56356865693313374, 3.1567783466839603, 1.5201300180753576, 0,
    0, 0.99575249282451073, 0.61425897261328666, 1.2233663263194712, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0], 
    [7.2652842514036369, -2.3119103657424414, 0, 0.067443170026859178, 0.2894952197787854, 0.44195399849740974, 0, 0, 0,
    0.4591530847132721, 0.14026516690905994, 1.4066322376473517, 0.40572853210100446, 0, 1.3572627165452165, 1.5179997924486877, 0.54213354577521133, 0,
    0, 0, 0, 0, 0, 0, 0, 2.8846500840638964,
    0, 0, 0, 1.1082218896963933, 1.2962496832506105, 0.22842561154989671, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0], 
    [8.5841509312915623, -2.765040945011636, 0, 0, 0, 0, 0, 0, 0,
    4.1816752831070323, 0.624710628895496, 1.1065543049459461, 0, 0, 0, 1.0280133043080188, 1.1868017500634926, 3.8253199428642568,
    1.8454733322333583, 0, 0, 1.1727679169313121, 1.8843639195644077, 0.84146963853933576, 0, 0,
    0, 0, 0, 1.4698638306735652, 0, 0, 0, 0,
    0, 0, 0, 0, 0.35326859222399482, 0.63432015577122913, 0.65008197369041587, 0.62734130105599528], 
    [11.917808960225496, -3.8503786390624457, 0, 0, 0, 0, 0, 0.55261276296940742, 0,
    1.860558422294992, -0.11327500388008699, 0.82437891170693112, 0, 0, 0, 0.39964248791030577, 0.7487413720163385, 1.0410482089004374,
    0, 0, 2.8241680746676243, 0, 0.2689673675929089, 1.1065323833644807, 0.78906965838459642, 0,
    0, 0, 0.79911502960387548, 1.3738119234931856, 0, 0, 0.51541790034374857, 0,
    0, 0, 0, 0, 0.84085747375244646, 1.4966499028172435, 1.7072509513243501, 1.8882615411851338], 
    [4.1156415170875666, -1.2786588534988286, 0, 0, 0, 0, 0, 0.2364397443316423, 0.23902124891032553,
    2.4067691257533248, 0.25667996163352191, 0.97655258651771926, 0, 0, 0.72038222276484332, 0.8372159579979499, 1.1647610659454599, 1.0747326525064285,
    0.4468867932306167, 0.52768845201398362, 0.64659761312085173, 0, 0.3156125379576864, 2.947244878727457, 0, 0,
    0, 0, 1.0954486585194212, 1.0550815022699203, 0.50594859446821627, 0.60351704120917271, 0, 0,
    0, 0, 0, 0, 0.13062823306486579, 0.41568246125931085, 0.40341603935413767, 0.52903833230651798], 
    [8.0275778709105907, -2.6082429130982798, 0, 0, 0, 0, 0.99132463479918231, 0, 0.73969050982025408,
    1.781957499473682, -0.024960006489569975, 0, 0, 0, 0, 2.1506984011721579, 1.4272326009960661, 0.91686892075260662,
    0.98810610330811499, 0, 0, 0, 1.2837402377092237, 0, 0, 0,
    0, 0, 1.1741805346104719, 2.0466064239967046, 0, 0.62405480330482144, 0, 0,
    0, 0, 0, 0, 0.27832981720899735, 0.30794189289176033, 0.56473593949911283, 0.77651254271268666], 
    [14.839101042656692, -4.8051341054408843, 0, 0, 0, 0, 0, 0, 0,
    -2.8369035324107057, -0.36349842659000514, 0, 0, 1.2892957682128878, 0, 0.44455883728607742, 0.34255819715349151, 0,
    0, 1.4890866073593347, 0, 0, 0, 0, 0, 0.34786129520339637,
    0.63876093500764075, 0.6338177436853567, 0.57581908041962615, 0.75287362266658731, 0, 0, 0, 0.36921800415342415,
    1.0381560026453696, 0.70364102530803652, 0.85257033994355869, 0, 0, 0, 0, 0], 
    [6.2113803461111061, -1.983566150695387, 0, 0, 0, 0, 0, 0, 0,
    -1.5995682550089132, -0.077769683693075312, 0, 0, 0, 0, 0.60894656789095847, 0, 0,
    0, 4.1596453389556789, 0, 0, 0, 0, 1.0520790556587876, 0,
    0, 0, 0, 0.6824635274408537, 0, 0, 0, 0,
    0, 0, 0, 0, 0.4183007995792849, 0.63351623682787428, 0.78472308793222056, 0.96310914112952117], 
    [3.9854184482476338, -1.7426970576325218, 0, 0, 0, 0, 0, 0, 0,
    2.0160796798276812, -0.042734043745477374, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    2.7411880902787775, 5.2200886149323269, 2.2416746922896493, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0]])

# bias matrix for males
male_bias = np.array([[-7.2591289466850277, -7.6876342765226262, -8.4208700270300625, -8.7166918098019277, -6.7132875682858542, -9.2275729512009956,
-7.8871012697298699, -8.300655539894251, -8.7592209887895898]])

# matrix to be used to calculate cancer risks for females
female_matrix = np.array([
    [35.940566689628312, -68.849637597790448, 0, 0, 0, 0, 0, 0, 0,
    0, 0.078517122305750198, -5.3730627788681424, 1.703586650229763, 0, 0, 0, 0, 0.37792062393857978,
    0, 0, 0, 0, 0, 0, 0.40866629745988947,
    0, 0, 0, 0, 2.9539029476671903, 1.3792892192392403, 0.46892163134409925, 0,
    0, 0.60366306629906741, 0.89633989323063157, 0.72913796124686203, 1.0255003552753392, 0, 0,
    0, 0, 0, 0, 0], 
    [-14.30294840678985, -25.930181137736426, 0, 0.054381307594513456, 0.12457099729838178, 0.18551986792615147, 0, 0, 0,
    0, -1.75409838256809, 2.0601979121740364, 0, 0.3863899675953914, 0, 0, 0, 0,
    0, 3.9278533274888368, 0.87796160783291022, 2.232029623398788, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0.44650530022482998, 0,
    0, 0.27286102972131654, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0], 
    [10.16633931075058, -16.911890249110002, 0, 0, 0, 0, 0, 0, 0,
    0, -0.56751433080526148, -2.6377586334504044, 1.2205973555195053, 0, 0, 0, 0, 0.72298701917735742,
    0, 0, 0, 0, 0, 0, 1.6126499968790107,
    0, 0, 1.9527008812518938, 0, 0, 0, 3.3618997560756485, 3.1391568551730864,
    0, 1.1276327958138455, 0, 0, 0, 0, 0,
    0, 0.32478752770957153, 0.75412112590767388, 0.74483430351396596, 0.63283485339138068], 
    [-11.617560661639077, -42.909805768687022, 0, 0.24290142628846959, 0.23592245201976081, 0.46066059345394461, 0, 0, 0,
    0, -0.53442378227530529, 2.6900552265408226, 1.4759238359186861, 0, 0.40445010488479982, 0, 0.66300742878565599, 1.4990872468711913,
    0.50680201072619224, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    2.7491673095810105, 0.70728168840029326, 1.0288860866585736, 0.76644141231996432, 0, 0.33751581231211736, 0,
    0, 0, 0, 0, 0], 
    [5.512793295816083, -70.273406291616183, 0, 0, 0, 0, 0, 0, 0,
    0, 2.6063377632938987, -1.2389834515079798, 1.2479756970482034, 0, 0, 0, 0, 0.78253040051247291,
    0.65145922368892439, 0, 0, 0, 3.7751714910656862, 1.4264472204617833, 0,
    0, 0.81787460691933733, 0, 1.4998439683677578, 0, 0, 0, 0,
    0, 0.71998946581725987, 1.2287925630053846, 0, 0, 0, 0,
    0, 0.21088353859940934, 0.4020914846651602, 0.84971197669592125, 1.102058546972454], 
    [-117.24057375029625, 25.170225474126809, 0, 0, 0, 0, 0, 0.79429019626713648, 0,
    0, 2.584548813392435, -0.60835239667627994, 0.86279803244016284, 0, 0, 0, 0, 0,
    0.71702321213794462, 0, 0, 0, 0.67184268060773233, 0, 0,
    2.9286439157734474, 0, 0, 0.36348937301142736, 1.209724038009159, 0, 0, 0,
    0, 0.8907072670032341, 1.1384524885073082, 0, 0, 0, 0.64399170532756023,
    0, 1.3397416191950409, 1.9500839456663224, 2.1881694694325233, 2.4828660433307768], 
    [35.820898730220478, -68.329474103771915, 0, 0.11292925170889954, 0.13891832056179676, 0.34281147667895862, 0, 0.28230214291079436, 0,
    0, 1.8969796480108396, -3.7755945945329574, 1.0476364795173587, 0, 0, 0, 0.9628688090459262, 0.83357100667156103,
    0.84509724384765461, 1.0400807427059522, 0, 0, 0.89053428956845959, 0.38396322651340786, 0.61431846475494478,
    0, 0, 0, 0.24570160029924543, 2.1666504706191545, 0, 0.42193832526235409, 0,
    0, 1.063078486173392, 1.1058752771736007, 0, 0, 0.37801436412994915, 0,
    0, 0.064383979255164758, 0.18750681016606915, 0.3754052152821668, 0.50073379522108441], 
    [-61.083181446256894, 20.302861270110689, 0, 0, 0, 0, 0, 0, 0,
    0, -2.1261135335028407, 3.2168200408772472, 1.3625636791018674, 0, 0, 1.995177480995183, 2.9381020883363806, 1.7307824546132513,
    1.0606947909647773, 0, 0, 0, 0, 0, 0.49588359974681079,
    0, 0, 0, 0.38437310274939984, 0, 0, 1.5869592940878865, 0,
    0, 1.6839747529852673, 0.47743323938217208, 0.68498500071823143, 0, 0, 0,
    0, 0, 0, 0, 0], 
    [-6.8219654517231225, -65.640489730518865, 0, 0, 0, 0, 1.1948138830441282, 0, 0,
    0.7951745325664703, 3.9715559458995728, -3.11611079991305, 0, 0, 0, 0, 0, 1.9230379689782926,
    1.5209568259888571, 0, 0, 0, 1.0107551560302726, 0.93240591532542594, 0,
    0, 0, 0, 1.1134012616631439, 0, 0, 0, 0,
    0, 1.4485586969016084, 1.5791912580663912, 0.93617386119414447, 0, 0, 0,
    0, -0.063130184815204424, 0.35236959505289345, 0.71460036703271568, 0.80732074103354412], 
    [-0.032322656962661747, -56.355141078663578, 0, 0, 0, 0, 0, 0, 0,
    0, 1.210391053577933, -4.7221299079939785, 1.2666531852544143, 0, 0, 0, 0, 0.61559549847075945,
    0.68421845946760196, 0, 0, 0, 0, 0, 4.1791444537241542,
    0, 0, 0, 0.56943292248218746, 0, 0, 1.2541097882792864, 0,
    0, 0, 0.77116105602905183, 0, 0, 0, 0,
    0, 0.27521757277393727, 0.54986566314758611, 0.65362421821366801, 0.90537636617858797], 
    [2.7778124257317254, -59.533351456663333, 0, 0, 0, 0, 0, 0, 0.8742311851235286,
    0.26551810240635559, 3.7623897936404322, -26.804545007465432, 0, 0, 0, 0, 0, 0.68919538367355804,
    0, 0, 0, 0, 0, 0, 1.6798617740998527,
    0, 0, 1.7853122923827887, 0, 0, 0, 4.4770199876067398, 0,
    0, 1.0362058616761669, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0]])

# bias matrix for females
female_bias = np.array([[-7.4207849482565749, -6.1261694200869234, -8.8309098444401926, -7.5466948789670942, -8.8746031610250764,
-8.6449002971789692, -6.7864501668594306, -7.5609929644491318, -9.2782129678657608, -8.9440775553776248,
-8.9931390822564037]])

# <================================= End of Part 1 =================================>

# <================================= Part 2: Helper functions + Function to transform the given input numpy array =================================>
def transform_age(x, isMale):
    def get_age_columns(age_col, isMale):
        new_array = np.zeros((len(age_col), 2))
        if isMale:
            new_array[:, 0] = (age_col / 10) - 4.800777912139893
            new_array[:, 1] = ((age_col / 10) * np.log(age_col / 10)) - 7.531354427337647
        else:
            new_array[:, 0] = (np.power(age_col / 10, float(-2))) - 0.039541322737932
            new_array[:, 1] = (np.power(age_col / 10, float(-2))) * np.log(age_col / 10) - 0.063867323100567
        return new_array

    # remove age (col 0) + add age_1, age_2 (cols 0, 1)
    age_col = x[:, 0].copy()
    x = np.delete(x, 0, axis=1)
    x = np.insert(x, [0], get_age_columns(age_col, isMale), axis=1)
    return x

def transform_alcohol_cat4(x, isMale):
    def get_alcohol_columns(alcohol_cat_col):
        alcohol_cat_col = alcohol_cat_col.astype(int)
        new_array = np.zeros((len(alcohol_cat_col), 4))
        new_array[range(len(alcohol_cat_col)), alcohol_cat_col] = 1
        return new_array
    
    # remove alcohol_cat4 (col 2) + add alcohol one-hot category (cols 2, 3, 4, 5)
    alcohol_cat_col = x[:, 2].copy()
    x = np.delete(x, 2, axis=1)
    x = np.insert(x, [2], get_alcohol_columns(alcohol_cat_col), axis=1)
    return x

def transfrom_bmi(x, isMale):
    def get_bmi_columns(bmi_col, isMale):
        new_array = np.zeros((len(bmi_col), 2))
        if isMale:
            new_array[:, 0] = np.power((bmi_col / 10), float(-2)) - 0.146067067980766
            new_array[:, 1] = (bmi_col / 10) - 2.616518735885620
        else:
            new_array[:, 0] = np.power((bmi_col / 10), float(-2)) - 0.151021569967270
            new_array[:, 1] = np.power((bmi_col / 10), float(-2)) * np.log(bmi_col / 10) - 0.142740502953529
        return new_array
    
    deleted_col_index = 9 if isMale else 10
    bmi_col = x[:, deleted_col_index].copy()
    x = np.delete(x, deleted_col_index, axis=1)
    x = np.insert(x, [deleted_col_index], get_bmi_columns(bmi_col, isMale), axis=1)
    return x

def transform_smoke_cat(x, isMale):
    # male case: remove smoke_cat (col 37) + add smoke one-hot category (cols 37, 38, 39, 40, 41)
    # female case: remove smoke_cat (col 40) + add smoke one-hot category (cols 40, 41, 42, 43, 44)
    def get_smoke_columns(smoke_cat_col, isMale):
        smoke_cat_col = smoke_cat_col.astype(int)
        new_array = np.zeros((len(smoke_cat_col), 5))
        new_array[range(len(smoke_cat_col)), smoke_cat_col] = 1
        return new_array

    deleted_col_index = 37 if isMale else 40
    smoke_cat_col = x[:, deleted_col_index].copy()
    x = np.delete(x, deleted_col_index, axis=1)
    x = np.insert(x, [deleted_col_index], get_smoke_columns(smoke_cat_col, isMale), axis=1)
    return x

# transform the input x into a format that can be used to calculate cancer risks
def transform_input(x, isMale):
    x = transform_age(x, isMale)
    x = transform_alcohol_cat4(x, isMale)
    x = transfrom_bmi(x, isMale)
    x = transform_smoke_cat(x, isMale)
    return x

# <================================= End of Part 2 =================================>

# <================================= Part 3: Functions for cancer risk calculation (Male + Female) =================================>
def male_function(x):
    x = transform_input(x, isMale=True)
    male_mat = male_matrix.transpose()
    exp_mult_mat = np.exp((x @ male_mat) + male_bias)
    result = (exp_mult_mat / (1 + np.sum(exp_mult_mat, axis=1))[:, np.newaxis]) * 100
    return result

def female_function(x):
    x = transform_input(x, isMale=False)
    female_mat = female_matrix.transpose()
    exp_mult_mat = np.exp((x @ female_mat) + female_bias)
    result = (exp_mult_mat / (1 + np.sum(exp_mult_mat, axis=1))[:, np.newaxis]) * 100
    return result

# <================================= End of Part 3 =================================>

female_input = ["age", "alcohol_cat4", "b_chronicpan", "b_copd", "b_endometrial",
"b_type2", "bmi", "c_hb", "fh_breastcancer", "fh_gicancer", "fh_ovariancancer", "new_abdodist", "new_abdopain",
"new_appetiteloss", "new_breastlump", "new_breastpain", "new_breastskin", "new_dysphagia", "new_gibleed", "new_haematuria", 
"new_haemoptysis", "new_heartburn", "new_imb", "new_indigestion", "new_necklump", "new_nightsweats", "new_pmb", "new_postcoital",
"new_rectalbleed", "new_vte", "new_weightloss", "s1_bowelchange", "s1_bruising", "s1_constipation", "s1_cough",
"smoke_cat"]

# Functions to get input numpy array from HTTP response
def getInputArray(form, isMale):
    input_arr = np.zeros(33 if isMale else 36, dtype=float)
    if isMale:
        for i in range(33):
            if i == 0 or i == 5:
                input_arr[i] = float(form[male_input[i]])
            elif i == 1:
                input_arr[i] = getAlcoholValue(form['alcohol_cat4'])
            elif i == 32:
                input_arr[i] = getSmokeValue(form['smoke_cat'])
            else:
                input_arr[i] = getCheckboxValue(form, male_input[i])
    else:
        for i in range(36):
            if i == 0 or i == 6:
                input_arr[i] = float(form[female_input[i]])
            elif i == 1:
                input_arr[i] = getAlcoholValue(form['alcohol_cat4'])
            elif i == 35:
                input_arr[i] = getSmokeValue(form['smoke_cat'])
            else:
                input_arr[i] = getCheckboxValue(form, female_input[i])
    return input_arr

# Explainers
male_explainer = shap.KernelExplainer(male_function, np.reshape(male_base_array, (1, len(male_base_array))))
female_explainer = shap.KernelExplainer(female_function, np.reshape(female_base_array, (1, len(female_base_array))))

# Base cancer risks 
male_base_risks = {key: val for key, val in zip(male_cancers, male_explainer.expected_value)}
female_base_risks = {key: val for key, val in zip(female_cancers, female_explainer.expected_value)}

# returns a list of numpy arrays of SHAP
def compute_shap_values(form, isMale):
    explainer = male_explainer if isMale else female_explainer
    input_arr = getInputArray(form, isMale)
    return explainer.shap_values(input_arr)

# <================================= Two functions that are called in main.py =================================>
def calculateShapValuesMale(form):
    inputs = getInputsMale(form)
    raw_shap_values = compute_shap_values(form, isMale=True)
    male_shap_values = {'blood': [], 'colorectal':[], 'gastro': [], 'lung': [], 'other': [], 'pancreatic': [], 
                'prostate': [], 'renal': [], 'testicular': []}
    for i, cancer_type in enumerate(male_shap_values):
        six_features = sorted(list(zip(male_input, raw_shap_values[i])), key=lambda t: abs(t[-1]), reverse=True)[:6]
        for feature, shap_value in six_features:
            if shap_value == 0:
                continue
            male_shap_values[cancer_type].append({'factor': feature, 'data': {'value': inputs[feature], 'base': bases_male[cancer_type][feature], 'effect': shap_value}})
    return male_shap_values

def calculateShapValuesFemale(form):
    inputs = getInputsFemale(form)
    raw_shap_values = compute_shap_values(form, isMale=False)
    female_shap_values = {"blood": [], "breast": [], "cervical": [], "colorectal": [], "gastro": [], "lung": [], 
                "other": [], "ovarian": [], "pancreatic": [], "renal": [], "uterine": []}
    for i, cancer_type in enumerate(female_shap_values):
        six_features = sorted(list(zip(female_input, raw_shap_values[i])), key=lambda t: abs(t[-1]), reverse=True)[:6]
        for feature, shap_value in six_features:
            if shap_value == 0:
                continue
            female_shap_values[cancer_type].append({'factor': feature, 'data': {'value': inputs[feature], 'base': bases_female[cancer_type][feature], 'effect': shap_value}})
    return female_shap_values

# <================================= End of two functions =================================>

if __name__ == "__main__":
    # male_x = np.array([45,1,1,1,1,25,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], dtype=float)
    # female_x = np.array([45,1,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], dtype=float)

    # # male_shap_values = male_explainer.shap_values(male_x)
    # # print("male_shap_values =", male_shap_values)
    # # print("base value =", male_explainer.expected_value)
    
    # female_shap_values = female_explainer.shap_values(female_x)
    # print("female_shap_values =", female_shap_values)
    # print("base value =", female_explainer.expected_value)
    print(male_base_risks)