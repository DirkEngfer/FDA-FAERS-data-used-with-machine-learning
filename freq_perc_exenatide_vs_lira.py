from collections import defaultdict
import os
homedir = os.getenv('HOME')

# unpickle aedrugLD

dataoutpath = os.path.join(homedir, 'Dokumente', 'tensorflow', 'fda_faers_data_tensorflow', 'faers_pickled')

import pickle, numpy as np
pickling = open(dataoutpath, 'rb')
aedrugLD = pickle.load(pickling)
pickling.close()

aedrugLD2 = []
for subjD in aedrugLD:
   if subjD['target'] in ('EXENATIDE', 'LIRAGLUTIDE'):
      aedrugLD2.append(subjD)


total_subjects = sum((1 for subjD in aedrugLD2))
#total_lira = sum((1 for subjD in aemod.aedrugLD if subjD['target'] == 'LIRAGLUTIDE'))

ae_count = defaultdict(int)
G = (subjD['ae'] for subjD in aedrugLD2)
for subj_aes in G:
    for ae in subj_aes:
        ae_count[ae] += 1

ae_ge_01percL = []
  
for ae, cnt in ae_count.items():
   if (cnt/float(total_subjects)*100) >= 0.1:
      ae_ge_01percL.append(ae)

ae_ge_01percL.sort()

ae_ini_A = np.zeros(len(ae_ge_01percL), dtype=int)

for s_offset, subj in enumerate(aedrugLD2):
   aeA = np.copy(ae_ini_A)
   for subj_ae in subj['ae']:
      for offset, ae01perc in enumerate(ae_ge_01percL):
         if subj_ae == ae01perc:
            aeA[offset] = 1
   aedrugLD2[s_offset]['ae_vector'] = np.copy(aeA)
     
        
 
print (aedrugLD2[3])      
#print(len(ae_ge_10percL))

