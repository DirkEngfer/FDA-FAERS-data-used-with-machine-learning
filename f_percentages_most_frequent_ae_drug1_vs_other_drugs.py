import csv

'''
Most frequent reactions (>={perc}%) of learned drug1 subjects, compared to learned  drug3 and  drug2 subjects
'''

learned_groupD = {'drug3':{'total':0}, 'drug2':{'total':0}, 'drug1':{'total':0}}
with open('drug1.csv', 'r') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_ALL, lineterminator='\n')
    for (offset,row) in enumerate(reader):
        if offset > 1 and row[1] == 'y':
            learned_groupD['drug1']['total'] += 1
            aeL = row[3].replace('"','').replace("'","").replace("[","").replace("]","").split(',')
            for ae in aeL:
                ae = ae.strip()
                learned_groupD['drug1'].setdefault(ae,0)
                learned_groupD['drug1'][ae] += 1
                learned_groupD['drug3'].setdefault(ae, 0)
                learned_groupD['drug2'].setdefault(ae, 0)

with open('drug3.csv', 'r') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_ALL, lineterminator='\n')
    for (offset,row) in enumerate(reader):
        if offset > 1 and row[1] == 'y':
            learned_groupD['drug3']['total'] += 1
            aeL = row[3].replace('"','').replace("'","").replace("[","").replace("]","").split(',')
            for ae in aeL:
                ae = ae.strip()
                learned_groupD['drug3'].setdefault(ae,0)
                learned_groupD['drug3'][ae] += 1

with open('drug2.csv', 'r') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_ALL, lineterminator='\n')
    for (offset,row) in enumerate(reader):
        if offset > 1 and row[1] == 'y':
            learned_groupD['drug2']['total'] += 1
            aeL = row[3].replace('"','').replace("'","").replace("[","").replace("]","").split(',')
            for ae in aeL:
                ae = ae.strip()
                learned_groupD['drug2'].setdefault(ae,0)
                learned_groupD['drug2'][ae] += 1

min_percent=5 # Most frequent reactions in % of subjects in the Learned group (Target=Answer of the NN)
data_drug3L = []
data_drug2L = []
data_drug1L = []
ticklabelsL = []
for k, vD in learned_groupD.items():
    for ae_key, ae_val in vD.items():
        if ae_key != 'total':
            learned_groupD[k][ae_key] = ae_val * 100 / float(learned_groupD[k]['total'])


learned_most_frequentLT = []
for ae_key, ae_val in learned_groupD['drug1'].items():
    if ae_key != 'total':
        if ae_val >= min_percent:
            learned_most_frequentLT.append((ae_val,ae_key))

for (perc, ae) in sorted(learned_most_frequentLT, reverse=True):
    data_drug1L.append(perc)
    ticklabelsL.append(ae)
    data_drug3L.append(learned_groupD['drug3'][ae])
    data_drug2L.append(learned_groupD['drug2'][ae])


print(ticklabelsL)
print('drug1 %', data_drug1L)
print(' drug2 %', data_drug2L)
print(' drug3 %', data_drug3L)

from plot_barchart import make_barchart3

make_barchart3(figname='perc_most_frequent_learned_drug1_vs_other.png', figwidth=12, figheight=8, adjust_bottom=0.65,
              title='Most frequent reactions (>={perc}%) of learned drug1 subjects,\ncompared to learned  drug3 and  drug2 subjects'.format(perc=min_percent),
              ticklabels=ticklabelsL, data1=data_drug1L, data2=data_drug3L, data3=data_drug2L,
              label1='Learned drug1 subjects N={}'.format(learned_groupD['drug1']['total']),
              label2='Learned  drug3 subjects N={}'.format(learned_groupD['drug3']['total']),
              label3='Learned  drug2 subjects N={}'.format(learned_groupD['drug2']['total']),
               c1='g', c2='b', c3='r')

