const male_labels = {
  'age': 'age',
  'alcohol_cat4': 'drinking',
  'bmi': 'bmi',
  'b_chronicpan': 'chronic pancreatitis',
  'b_copd': 'chronic obstructive airways disease (COPD)',
  'b_type2': 'type 2 diabetes',
  'c_hb': 'anaemia',
  'fh_gicancer': 'GI cancer in family',
  'fh_prostatecancer': 'prostate cancer in family',
  'new_abdodist': 'abdominal swelling',
  'new_abdopain': 'abdominal pain',
  'new_appetiteloss': 'loss of appetite',
  'new_dysphagia': 'difficulty swallowing',
  'new_gibleed': 'blood when vomit',
  'new_haematuria': 'blood in urine',
  'new_haemoptysis': 'blood when cough',
  'new_heartburn': 'heartburn',
  'new_indigestion': 'indigestion',
  'new_necklump': 'necklump',
  'new_nightsweats': 'night sweats',
  'new_rectalbleed': 'rectal bleeding',
  'new_testicularlump': 'testicular lump',
  'new_testispain': 'testicular pain',
  'new_vte': 'venous thromboembolism',
  'new_weightloss': 'weight loss',
  's1_bowelchange': 'change in bowel habit',
  's1_constipation': 'constipation',
  's1_cough': 'cough',
  's1_impotence': 'impotence',
  's1_nocturia': 'nocturia',
  's1_urinaryfreq': 'urinary frequency',
  's1_urinaryretention': 'urinary retention',
  'smoke_cat': 'smoking',
  'blood': 'Blood',
  'colorectal': 'Colorectal', 
  'gastro': 'Gastro-oesophageal', 
  'lung': 'Lung',
  'other': 'Other', 
  'pancreatic': 'Pancreatic', 
  'prostate': 'Prostate', 
  'renal': 'Renal tract', 
  'testicular': 'Testicular'
}

function getFullLabelMale(label) {
  return male_labels[label];
}

const female_labels = {
  'age': 'age',
  'alcohol_cat4': 'drinking',
  'bmi': 'bmi',
  'b_type2': 'type 2 diabetes',
  'b_chronicpan': 'chronic pancreatitis',
  'b_copd': 'chronic obstructive airways disease (COPD)',
  'b_endometrial': 'Endometrial polyp',
  'c_hb': 'anaemia',
  'fh_breastcancer': 'breast cancer in family',
  'fh_gicancer': 'GI cancer in family',
  'fh_ovariancancer': 'overian cancer in family',
  'new_abdodist': 'abdominal swelling',
  'new_abdopain': 'abdominal pain',
  'new_appetiteloss': 'loss of appetite',
  'new_breastlump': 'breastlump',
  'new_breastpain': 'breast pain',
  'new_breastskin': 'breast skin tethering',
  'new_dysphagia': 'difficulty swallowing',
  'new_gibleed': 'blood when vomit',
  'new_haematuria': 'blood in urine',
  'new_haemoptysis': 'blood when cough',
  'new_heartburn': 'heartburn',
  'new_imb': 'irregular menstrual bleeding',
  'new_indigestion': 'indigestion',
  'new_necklump': 'necklump',
  'new_nightsweats': 'night sweats',
  'new_pmb': 'postmenopausal bleeding',
  'new_postcoital': 'vaginal bleeding after sex',
  'new_rectalbleed': 'rectal bleeding',
  'new_vte': 'venous thromboembolism',
  'new_weightloss': 'weight loss',
  's1_bowelchange': 'change in bowel habit',
  's1_bruising': 'bruising',
  's1_constipation': 'constipation',
  's1_cough': 'cough',
  'smoke_cat': 'smoking',
  "blood": 'Blood', 
  "breast": 'Breast', 
  "cervical": 'Cervical', 
  "colorectal": 'Colorectal', 
  "gastro": 'Gastro-oesophageal', 
  "lung": 'Lung',
  "other": 'Other', 
  "ovarian": 'Ovarian', 
  "pancreatic": 'Pancreatic', 
  "renal": 'Renal tract', 
  "uterine": 'Uterine'
}

function getFullLabelFemale(label) {
  return female_labels[label];
}

function getExpTextLabelMale(data) {
  const fullLabel = getFullLabelMale(data.factor)
  if (data.factor == 'age' || data.factor == 'bmi') {
    const value = Number.isInteger(data.data.value) ? data.data.value : data.data.value.toFixed(3);
    return `${fullLabel} of ${value}`
  } else if (data.factor == 'smoke_cat' || data.factor == 'alcohol_cat4') {
    return `${data.data.value} ${fullLabel}`
  } else {
    return (data.data.value == 'no' ? 'no' : '') + ` ${fullLabel}`
  }
}

function generateExplanationMale(header, data) {
  let html = `<h2>${header} cancer risk relative to baseline</h2><ul>`
  for (const elem of data) {
    const baseLabel = createBaseTextForExplanation(elem.data.base, getFullLabelMale(elem.factor))
    if (elem.data.effect > 0) {
      html += `<li><i>${getExpTextLabelMale(elem)}</i> increased this risk by <span style="color:red">${elem.data.effect.toFixed(3)}%</span> <i>(relative to ${baseLabel})</i></li>`
    } else if (elem.data.effect < 0) {
      html += `<li><i>${getExpTextLabelMale(elem)}</i> decreased this risk by <span style="color:green">${-elem.data.effect.toFixed(3)}%</span> <i>(relative to ${baseLabel})</i></li>`
    } else {
      html += `<li><i>${getExpTextLabelMale(elem)}</i> didn't increase nor decrease this risk <i>(relative to ${baseLabel})</i></li>`
    }
  }
  html += `</ul>`;
  return html;
}

function getExpTextLabelFemale(data) {
  const fullLabel = getFullLabelFemale(data.factor)
  if (data.factor == 'age' || data.factor == 'bmi') {
    const value = Number.isInteger(data.data.value) ? data.data.value : data.data.value.toFixed(3);
    return `${fullLabel} of ${value}`
  } else if (data.factor == 'smoke_cat' || data.factor == 'alcohol_cat4') {
    return `${data.data.value} ${fullLabel}`
  } else {
    return (data.data.value == 'no' ? 'no' : '') + ` ${fullLabel}`
  }
}

function generateExplanationFemale(header, data) {
  let html = `<h2>${header} cancer risk relative to baseline</h2><ul>`
  for (const elem of data) {
    const baseLabel = createBaseTextForExplanation(elem.data.base, getFullLabelFemale(elem.factor))
    if (elem.data.effect > 0) {
      html += `<li><i>${getExpTextLabelFemale(elem)}</i> increased this risk by <span style="color:red">${elem.data.effect.toFixed(3)}%</span> <i>(relative to ${baseLabel})</i></li>`
    } else if (elem.data.effect < 0) {
      html += `<li><i>${getExpTextLabelFemale(elem)}</i> decreased this risk by <span style="color:green">${-elem.data.effect.toFixed(3)}%</span> <i>(relative to ${baseLabel})</i></li>`
    } else {
      html += `<li><i>${getExpTextLabelFemale(elem)}</i> didn't increase nor decrease this risk <i>(relative to ${baseLabel})</i></li>`
    }
  }
  html += `</ul>`;
  return html;
}

function generateShapExplanation(header, output, base) {
  let html = `<h2>${header} cancer</h2>`;
  html += `<p style="margin:0">The base risk for this cancer type is ${base.toFixed(4)}%</p>`;
  html += `<p style="margin:0">Your risk is ${output.toFixed(4)}%</p>`;
  const diff = (output - base).toFixed(4);
  if (diff > 0) {
    html += `<p style="margin:0"}>The increase of ${diff}% is partly contributed by these factors:</p>`;
  } else if (diff < 0) {
    html += `<p style="margin:0">The decrease of ${-diff}% is partly contributed by these factors:</p>`;
  } else {
    html += `<p style="margin:0">There is no difference between your risk and the base risk.</p>`;
  }
  return html;
}

function createBaseTextForExplanation(base_value, factor_label) {
  if (factor_label == 'age' || factor_label == 'bmi') {
    return factor_label + ' of ' + base_value;
  } else if (factor_label == 'chronic obstructive airways disease (COPD)') {
    return base_value + ' COPD';
  } else if (factor_label == 'drinking') {
    return base_value == 'no' ? 'non-drinker' : base_value + ' drinker';
  } else if (factor_label == 'smoking') {
    return (base_value == 'non' || base_value == 'ex') ? base_value + '-smoker' : base_value + ' smoker';
  } else {
    return base_value + ' ' + factor_label;
  }
}

function download(chartName) {
  const imageLink = document.createElement('a');
  const canvas = document.getElementById(chartName);
  imageLink.download = 'chart.png';
  imageLink.href = canvas.toDataURL('image/png', 1);
  imageLink.click();
}