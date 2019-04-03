replD = {'ABDOMINAL':'' \
    , 'ABNORMAL LOSS OF WEIGHT':'WEIGHT' \
    , 'INJECTION SITE':'INJECTION_SITE' \
    , 'ADMINISTRATION SITE':'INJECTION_SITE' \
    , 'ALLERGIC':'' \
    , 'ANXIETY':'' \
    , 'APPENDICITIS':'' \
    , 'APPLICATION SITE':'INJECTION_SITE' \
    , 'ARTERIAL':'' \
    , 'BLINDNESS':'' \
    , 'BLOOD CHOLESTEROL':'BLOOD_CHOLESTEROL' \
    , 'BLOOD GLUCOSE':'BLOOD_GLUCOSE' \
    , 'BLOOD POTASSIUM':'BLOOD_POTASSIUM' \
    , 'BLOOD PRESSURE':'BLOOD_PRESSURE' \
    , 'BLOOD TRIGLYCERIDES':'BLOOD_TRIGLYCERIDES' \
    , 'BODY MASS INDEX':'BODY_MASS_INDEX' \
    , 'CARDIAC':'' \
    , 'CHOLECYSTITIS':'' \
    , 'CIRCUMSTANCE OR INFORMATION CAPABLE OF LEADING TO':'CIRCUMSTANCE_OR_INFORMATION_CAPABLE_OF_LEADING_TO' \
    , 'COLITIS':'' \
    , 'COMPLICATION ASSOCIATED WITH DEVICE':'DEVICE' \
    , 'COMPLICATION OF DEVICE':'DEVICE' \
    , 'CORONARY ARTERY':'CORONARY_ARTERY' \
    , 'DEPRESSION':'DEPRESSION' \
    , 'DEPRESSED LEVEL':'DEPRESSION' \
    , 'DEPRESSED MOOD':'DEPRESSION' \
    , 'DEVICE':'' \
    , 'DIABETES MELLITUS':'DIABETES' \
    , 'DIABETIC':'DIABETES' \
    , 'DRUG ADM':'DRUG_ADMINISTRATION' \
    , 'DRUG D':'DRUG_EFFECT' \
    , 'DRUG E':'DRUG_EFFECT' \
    , 'DRUG H':'DRUG_EFFECT' \
    , 'DRUG IN':'DRUG_EFFECT' \
    , 'EMOTIONAL':'' \
    , 'EOSINOPH':'EOSINOPHIL' \
    , 'EYE':'' \
    , 'FEAR':'' \
    , 'FEELING':'EMOTIONAL' \
    , 'FUNGAL':'' \
    , 'GALLBLADDER':'' \
    , 'GASTRIC':'' \
    , 'GASTRITIS':'' \
    , 'GASTROINTESTINAL':'' \
    , 'GASTROENTERITIS':'GASTROINTESTINAL' \
    , 'GENITAL':'' \
    , 'GLAUCOMA':'EYE' \
    , 'GLYCOSYLATED HAEMOGLOBIN':'GLYCOSYLATED_HAEMOGLOBIN' \
    , 'HEART RATE':'HEART_RATE' \
    , 'HEPATIC':'' \
    , 'HERNIA':'' \
    , 'HYPOGLYCAEM':'' \
    , 'INCISION SITE':'INCISION_SITE' \
    , 'INCORRECT D':'INCORRECT_DOSE' \
    , 'INCREASED APPETITE':'HUNGER' \
    , 'INFLUENZA':'' \
    , 'INSULIN':'' \
    , 'INTENTIONAL DEVICE':'DEVICE' \
    , 'INTENTIONAL PRODUCT':'PRODUCT' \
    , 'INTERVERTEBRAL':'' \
    , 'INTRAOCULAR':'EYE' \
    , 'LETHARGY':'EMOTIONAL' \
    , 'LIBIDO DISORDER':'EMOTIONAL' \
    , 'LIGAMENT':'' \
    , 'LIVER DISORDER':'HEPATIC' \
    , 'LYMPH':'' \
    , 'MALNUTRITION':'HUNGER' \
    , 'MEDICATION ERROR':'DEVICE' \
    , 'MOOD SWINGS':'EMOTIONAL' \
    , 'MUSCLE':'' \
    , 'MUSCULOSKELETAL':'' \
    , 'NEUROPATHY':'DIABETES' \
    , 'OBESITY':'WEIGHT' \
    , 'OESOPHAGEAL':'' \
    , 'OVERWEIGHT':'WEIGHT' \
    , 'PANCREA':'PANCREAS' \
    , 'PANIC':'' \
    , 'POST PROCEDURAL':'POST_PROCEDURAL' \
    , 'PRODUCT PREPARATION ERROR':'PRODUCT' \
    , 'PRURITUS':'' \
    , 'PULMONARY':'' \
    , 'RASH':'' \
    , 'RENAL':'' \
    , 'RETINAL VASCULAR OCCLUSION':'EYE' \
    , 'RETINOPATHY':'EYE' \
    , 'SHOCK HYPOGLYCAEMIC':'HYPOGLYCAEM' \
    , 'SKIN':'' \
    , 'SLEEP':'' \
    , 'THYROID':'' \
    , 'TOOTH':'' \
    , 'TYPE 1 DIABETES M':'DIABETES' \
    , 'TYPE 2 DIABETES M':'DIABETES' \
    , 'URINARY TRACT':'' \
    , 'UTERINE':'' \
    , 'VISUAL ACUITY REDUCED':'EYE' \
    , 'VISUAL IMPAIRMENT':'EYE' \
    , 'VOMITING':'' \
    , 'WEIGHT':'' \
    , 'WRONG TECHNIQUE IN DEVICE USAGE':'DEVICE' \
    , 'PRODUCT':'' \
    }

def ae_mapper(aeL):
    new_aeL = []
    for ae in aeL:
        found = 0
        for todelete in replD:
            if replD[todelete] == '': newStr = todelete + '_DERIVED'
            else                    : newStr = replD[todelete] + '_DERIVED'
            if ae.startswith(todelete) == True:
                new_aeL.append(newStr)
                found = 1
                break
        if found == 0:
            new_aeL.append(ae)
    return list(set(new_aeL))

