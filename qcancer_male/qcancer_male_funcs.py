def blood_cancer_male(args):
  score = 0
  
  score += args['age_1'] * 3.4970179354556610000000000
  score += args['age_2'] * -1.0806801421562633000000000
  score += args['bmi_1'] * 0.9519259479511792400000000
  score += args['bmi_2'] * 0.1714669358410085800000000

  score += args['c_hb'] * 1.8905802113004144000000000
  score += args['new_abdodist'] * 0.8430432197211393800000000
  score += args['new_abdopain'] * 0.6226473288294992500000000
  score += args['new_appetiteloss'] * 1.0672150380753760000000000
  score += args['new_dysphagia'] * 0.5419443056595199000000000
  score += args['new_haematuria'] * 0.4607538085363521700000000
  score += args['new_haemoptysis'] * 0.9501446899241836600000000
  score += args['new_indigestion'] * 0.5635686569331337400000000
  score += args['new_necklump'] * 3.1567783466839603000000000
  score += args['new_nightsweats'] * 1.5201300180753576000000000
  score += args['new_testicularlump'] * 0.9957524928245107300000000
  score += args['new_vte'] * 0.6142589726132866600000000
  score += args['new_weightloss'] * 1.2233663263194712000000000

  return score - 7.2591289466850277000000000

def colorectal_cancer_male(args):
  score = 0

  Ialcohol = [0, 0.0674431700268591780000000, 0.2894952197787854000000000, 0.4419539984974097400000000]

  score += Ialcohol[args['alcohol_cat4']]

  score += args['age_1'] * 7.2652842514036369000000000
  score += args['age_2'] * -2.3119103657424414000000000
  score += args['bmi_1'] * 0.4591530847132721000000000
  score += args['bmi_2'] * 0.1402651669090599400000000

  score += args['c_hb'] * 1.4066322376473517000000000
  score += args['fh_gicancer'] * 0.4057285321010044600000000
  score += args['new_abdodist'] * 1.3572627165452165000000000
  score += args['new_abdopain'] * 1.5179997924486877000000000
  score += args['new_appetiteloss'] * 0.5421335457752113300000000
  score += args['new_rectalbleed'] * 2.8846500840638964000000000
  score += args['new_weightloss'] * 1.1082218896963933000000000
  score += args['s1_bowelchange'] * 1.2962496832506105000000000
  score += args['s1_constipation'] * 0.2284256115498967100000000

  return score - 7.6876342765226262000000000

def gastro_oesophageal_cancer_male(args):
  score = 0

  Ismoke = [0, 0.3532685922239948200000000, 0.6343201557712291300000000, 0.6500819736904158700000000, 0.6273413010559952800000000]

  score += Ismoke[args['smoke_cat']]

  score += args['age_1'] * 8.5841509312915623000000000
  score += args['age_2'] * -2.7650409450116360000000000
  score += args['bmi_1'] * 4.1816752831070323000000000
  score += args['bmi_2'] * 0.6247106288954960000000000

  score += args['c_hb'] * 1.1065543049459461000000000
  score += args['new_abdopain'] * 1.0280133043080188000000000
  score += args['new_appetiteloss'] * 1.1868017500634926000000000
  score += args['new_dysphagia'] * 3.8253199428642568000000000
  score += args['new_gibleed'] * 1.8454733322333583000000000
  score += args['new_heartburn'] * 1.1727679169313121000000000
  score += args['new_indigestion'] * 1.8843639195644077000000000
  score += args['new_necklump'] * 0.8414696385393357600000000
  score += args['new_weightloss'] * 1.4698638306735652000000000

  return score - 8.4208700270300625000000000

def lung_cancer_male(args):
  score = 0

  Ismoke = [0, 0.8408574737524464600000000, 1.4966499028172435000000000, 1.7072509513243501000000000, 1.8882615411851338000000000]

  score += Ismoke[args['smoke_cat']]

  score += args['age_1'] * 11.9178089602254960000000000
  score += args['age_2'] * -3.8503786390624457000000000
  score += args['bmi_1'] * 1.8605584222949920000000000
  score += args['bmi_2'] * -0.1132750038800869900000000

  score += args['b_copd'] * 0.5526127629694074200000000
  score += args['c_hb'] * 0.8243789117069311200000000
  score += args['new_abdopain'] * 0.3996424879103057700000000
  score += args['new_appetiteloss'] * 0.7487413720163385000000000
  score += args['new_dysphagia'] * 1.0410482089004374000000000
  score += args['new_haemoptysis'] * 2.8241680746676243000000000
  score += args['new_indigestion'] * 0.2689673675929089000000000
  score += args['new_necklump'] * 1.1065323833644807000000000
  score += args['new_nightsweats'] * 0.7890696583845964200000000
  score += args['new_vte'] * 0.7991150296038754800000000
  score += args['new_weightloss'] * 1.3738119234931856000000000
  score += args['s1_cough'] * 0.5154179003437485700000000

  return score - 8.7166918098019277000000000

def other_cancer_male(args):
  score = 0

  Ismoke = [0, 0.1306282330648657900000000, 0.4156824612593108500000000, 0.4034160393541376700000000, 0.5290383323065179800000000]

  score += Ismoke[args['smoke_cat']]

  score += args['age_1'] * 4.1156415170875666000000000
  score += args['age_2'] * -1.2786588534988286000000000
  score += args['bmi_1'] * 2.4067691257533248000000000
  score += args['bmi_2'] * 0.2566799616335219100000000

  score += args['b_copd'] * 0.2364397443316423000000000
  score += args['b_type2'] * 0.2390212489103255300000000
  score += args['c_hb'] * 0.9765525865177192600000000
  score += args['new_abdodist'] * 0.7203822227648433200000000
  score += args['new_abdopain'] * 0.8372159579979499000000000
  score += args['new_appetiteloss'] * 1.1647610659454599000000000
  score += args['new_dysphagia'] * 1.0747326525064285000000000
  score += args['new_gibleed'] * 0.4468867932306167000000000
  score += args['new_haematuria'] * 0.5276884520139836200000000
  score += args['new_haemoptysis'] * 0.6465976131208517300000000
  score += args['new_indigestion'] * 0.3156125379576864000000000
  score += args['new_necklump'] * 2.9472448787274570000000000
  score += args['new_vte'] * 1.0954486585194212000000000
  score += args['new_weightloss'] * 1.0550815022699203000000000
  score += args['s1_bowelchange'] * 0.5059485944682162700000000
  score += args['s1_constipation'] * 0.6035170412091727100000000

  return score - 6.7132875682858542000000000

def pancreatic_cancer_male(args):
  score = 0

  Ismoke = [0, 0.2783298172089973500000000, 0.3079418928917603300000000, 0.5647359394991128300000000, 0.7765125427126866600000000]

  score += Ismoke[args['smoke_cat']]

  score += args['age_1'] * 8.0275778709105907000000000
  score += args['age_2'] * -2.6082429130982798000000000
  score += args['bmi_1'] * 1.7819574994736820000000000
  score += args['bmi_2'] * -0.0249600064895699750000000

  score += args['b_chronicpan'] * 0.9913246347991823100000000
  score += args['b_type2'] * 0.7396905098202540800000000
  score += args['new_abdopain'] * 2.1506984011721579000000000
  score += args['new_appetiteloss'] * 1.4272326009960661000000000
  score += args['new_dysphagia'] * 0.9168689207526066200000000
  score += args['new_gibleed'] * 0.9881061033081149900000000
  score += args['new_indigestion'] * 1.2837402377092237000000000
  score += args['new_vte'] * 1.1741805346104719000000000
  score += args['new_weightloss'] * 2.0466064239967046000000000
  score += args['s1_constipation'] * 0.6240548033048214400000000

  return score - 9.2275729512009956000000000

def prostate_cancer_male(args):
  score = 0

  score += args['age_1'] * 14.8391010426566920000000000
  score += args['age_2'] * -4.8051341054408843000000000
  score += args['bmi_1'] * -2.8369035324107057000000000
  score += args['bmi_2'] * -0.3634984265900051400000000

  score += args['fh_prostatecancer'] * 1.2892957682128878000000000
  score += args['new_abdopain'] * 0.4445588372860774200000000
  score += args['new_appetiteloss'] * 0.3425581971534915100000000
  score += args['new_haematuria'] * 1.4890866073593347000000000
  score += args['new_rectalbleed'] * 0.3478612952033963700000000
  score += args['new_testispain'] * 0.6387609350076407500000000
  score += args['new_testicularlump'] * 0.6338177436853567000000000
  score += args['new_vte'] * 0.5758190804196261500000000
  score += args['new_weightloss'] * 0.7528736226665873100000000
  score += args['s1_impotence'] * 0.3692180041534241500000000
  score += args['s1_nocturia'] * 1.0381560026453696000000000
  score += args['s1_urinaryfreq'] * 0.7036410253080365200000000
  score += args['s1_urinaryretention'] * 0.8525703399435586900000000

  return score - 7.8871012697298699000000000

def renal_tract_cancer_male(args):
  score = 0

  Ismoke = [0, 0.4183007995792849000000000, 0.6335162368278742800000000, 0.7847230879322205600000000, 0.9631091411295211700000000]

  score += Ismoke[args['smoke_cat']]

  score += args['age_1'] * 6.2113803461111061000000000
  score += args['age_2'] * -1.9835661506953870000000000
  score += args['bmi_1'] * -1.5995682550089132000000000
  score += args['bmi_2'] * -0.0777696836930753120000000

  score += args['new_abdopain'] * 0.6089465678909584700000000
  score += args['new_haematuria'] * 4.1596453389556789000000000
  score += args['new_nightsweats'] * 1.0520790556587876000000000
  score += args['new_weightloss'] * 0.6824635274408537000000000

  return score - 8.3006555398942510000000000

def testicular_cancer_male(args):
  score = 0

  score += args['age_1'] * 3.9854184482476338000000000
  score += args['age_2'] * -1.7426970576325218000000000
  score += args['bmi_1'] * 2.0160796798276812000000000
  score += args['bmi_2'] * -0.0427340437454773740000000

  score += args['new_testispain'] * 2.7411880902787775000000000
  score += args['new_testicularlump'] * 5.2200886149323269000000000
  score += args['new_vte'] * 2.2416746922896493000000000
  
  return score - 8.7592209887895898000000000