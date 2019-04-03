# By Dirk Engfer, using Python 3 on ubuntu
#
# Data source: FDA quarterly update adverse events (FAERS) CSV files downloaded from
# https://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm
import os, csv, bisect
from ae_mapper import ae_mapper

homedir = os.getenv('HOME')

#print (homedir)


dataoutpath = os.path.join(homedir, 'Dokumente', 'tensorflow', 'fda_faers_data_tensorflow', 'faers_pickled')
indatapath = os.path.join(homedir, 'Dokumente', 'tensorflow', 'fda_faers_data_tensorflow')

datafile = 'diabetes.txt'
drugfile = 'DRUG.txt'
aefile = 'REAC.txt'

logfile1 = os.path.join(dataoutpath, 'log1.txt')


diabetes_subjL = []
with open(os.path.join(indatapath, datafile), 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='$')
    diabetes_subjL = [row[0] for row in reader if row[3].upper().find('DIABET') >= 0 and row[0].startswith(('vali','0','1','2','3','4','5','6','7','8','9'))]

diabetes_subjL = sorted(list(set(diabetes_subjL)))

drugs_occurrenceD = {}
#confirmed_drugL = ['EXENATIDE', 'GLIPIZIDE', 'TRULICITY', 'CANAGLIFLOZIN', 'GLICLAZIDE', 'GLIMEPIRIDE', 'LINAGLIPTIN', 'LIRAGLUTIDE']
confirmed_drugL = ['EXENATIDE', 'LIRAGLUTIDE', 'CANAGLIFLOZIN']
confirmed_drug_posL = [0,1,2]


drugrowsL = []
with open(os.path.join(indatapath, drugfile), 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='$')
    for row in reader:
        if row[0].startswith(('vali','0','1','2','3','4','5','6','7','8','9')):
            drugrowsL.append(row)
drugrowsL = sorted(drugrowsL)

for row in drugrowsL:
    if row[0] in diabetes_subjL:
        for confirmed_drug in confirmed_drugL:
            found = 0
            if row[4].upper().find(confirmed_drug) >= 0:
                drugs_occurrenceD.setdefault(row[0], set()).add(row[4].upper().replace('.', ''))
                found = 1
            elif row[5].upper().find(confirmed_drug) >= 0:
                drugs_occurrenceD.setdefault(row[0], set()).add(row[5].upper().replace('.', ''))
                found = 1
            if found == 1: break

# clean drug list - remove subjects with more than one drug term contained in the confirmed drug list:
for key_subject in drugs_occurrenceD:
    drugs_occurrenceD[key_subject] = list(drugs_occurrenceD[key_subject])
    found = 0
    for confirmed_drug in confirmed_drugL:
        for subject_drug in drugs_occurrenceD[key_subject]:
            if subject_drug.find(confirmed_drug) >= 0:
                found += 1
                break
        if found > 1:
            break
    if found > 1:
        drugs_occurrenceD[key_subject] = 'to delete'
drugs_occurrenceD2 = {}
for key_subject in drugs_occurrenceD:
    if drugs_occurrenceD[key_subject] != 'to delete':
        drugs_occurrenceD2[key_subject] = list(drugs_occurrenceD[key_subject])

drugS = set(drugs_occurrenceD2.keys())
aeD = {}
with open(os.path.join(indatapath, aefile), 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='$')
    for row in reader:
        if row[0].startswith(('vali','0','1','2','3','4','5','6','7','8','9')):
            aeD.setdefault(row[0], set()).add(row[2].upper())

print('Number of records from the reactions file, raw data', len(aeD))

# Keep subjects having at least 2 AE terms (remove subjects with insufficient AE pattern):
dropL = []
for key_subj in aeD:
    if len(aeD[key_subj]) < 2:
        dropL.append(key_subj)
for subj in dropL:
    aeD.pop(subj)

# Combine AE and Drugs BY subject having indication Diabetes, group AEs
aedrugLD = []
for subj_drug in drugS:
    for (subj_ae, ae_list) in aeD.items():
        if subj_ae == subj_drug:
            subjdict = {}
            subjdict['subjnum'] = subj_ae
            subjdict['drugs'] = drugs_occurrenceD2.get(subj_ae, None)
            subjdict['ae'] = ae_mapper(ae_list)
            for (confdrug, index) in zip(confirmed_drugL, confirmed_drug_posL):
                for drug_item in subjdict['drugs']:
                    if drug_item.find(confdrug) >= 0:
                        subjdict['target'] = confdrug
                        subjdict['targetnum'] = index
                        break
            aedrugLD.append(dict(subjdict))
            break


print('Number of diabetes subjects with reactions - filtered for relevant medication', len(aedrugLD))

# shrink validation cases i.e. subjects without the existence of predefined-AEs i.e. to be removed, provided a list of allowed reactions:
for (offset, subjD) in enumerate(aedrugLD):
    if subjD['subjnum'].startswith('vali') and subjD['target'] == 'EXENATIDE':
        ae_found = 0
        for ae in subjD['ae']:
            # Enter the reactions that are expected for validation (the existence of at least one of them returns a valid subject)
            if ae in ['INJECTION_SITE_DERIVED','PRODUCT_DERIVED','DEVICE_DERIVED','UNDERDOSE','WRONG TECHNIQUE IN PRODUCT USAGE PROCESS','NAUSEA','CIRCUMSTANCE_OR_INFORMATION_CAPABLE_OF_LEADING_TO_DERIVED','NEEDLE ISSUE','INCORRECT_DOSE_DERIVED','ABDOMINAL_DERIVED']:
                ae_found = 1
                break
        if ae_found == 0:
            aedrugLD[offset] = 999

ae_len = len(aedrugLD)
x = 0
while x < ae_len:
    mycnt = aedrugLD.count(999)
    if mycnt > 0:
        aedrugLD.remove(999)
    else:
        break
    x = x + 1

# Build up the full distinct AE list, sorted:
AE_full_list = [' ']
for rec in aedrugLD:
    for ae_candidate in rec['ae']:
        x_insert_point = bisect.bisect_right(AE_full_list, ae_candidate)
        x_is_present = AE_full_list and AE_full_list[x_insert_point-1] == ae_candidate
        if x_is_present == False:
            AE_full_list[x_insert_point:x_insert_point] = [ae_candidate]
del AE_full_list[0]

# For neural networks analysis:
# Build up the complete AE input list per subject, AE at index is 0 if AE not experienced, otherwise 1
# Devide inputs into training, test and validation data:
import math
for (offset, subjD) in enumerate(aedrugLD):
    ae_vectorL = []
    subj_aeL = sorted(list(subjD['ae']))
    for ae_term in AE_full_list:
        x_is_present = bool(0)
        x_insert_point = subj_aeL and bisect.bisect_right(subj_aeL, ae_term)
        x_is_present = subj_aeL and subj_aeL[x_insert_point-1] == ae_term
        if x_is_present != False:
            ae_vectorL.append(1)
        else:
            ae_vectorL.append(0)
    subjD['ae_vector'] = ae_vectorL
    if subjD['subjnum'].startswith('vali'):
        subjD['group'] = 'validation'
    else:
        if math.fmod(float(offset),3) == 0:
            subjD['group'] = 'test'
        else:
            subjD['group'] = 'training'


# pickle aedrugLD
import pickle
pickling = open(dataoutpath, 'wb')
pickle.dump(aedrugLD, pickling)
pickling.close()
# check success:
unpickling = open(dataoutpath, 'rb')
aedrugLD_unpickled = pickle.load(unpickling)
unpickling.close()

