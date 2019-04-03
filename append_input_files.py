# Data source: FDA quarterly update adverse events (FAERS) CSV files downloaded from
# https://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm

import os

datapath = os.path.join('F:/','data','fda_adverse_events_data','ascii')

indifile = 'diabetes.txt'
drugfile = 'DRUG.txt'
aefile   = 'REAC.txt'

with open(datapath + '/' + indifile, 'wt') as my_file:
    inputf = open(datapath + '/' + 'INDI18Q2.txt', 'rt')
    for line in inputf:
        if line.upper().find('DIABET') >= 0:
            my_file.write('vali' + line)
    inputf.close()

    inputf = open(datapath + '/' + 'INDI18Q1.txt', 'rt')
    for line in inputf:
        if line.upper().find('DIABET') >= 0:
            my_file.write(line)
    inputf.close()

    inputf = open(datapath + '/' + 'INDI17Q4.txt', 'rt')
    for line in inputf:
        if line.upper().find('DIABET') >= 0:
            my_file.write(line)
    inputf.close()

    inputf = open(datapath + '/' + 'INDI17Q3.txt', 'rt')
    for line in inputf:
        if line.upper().find('DIABET') >= 0:
            my_file.write(line)
    inputf.close()

    inputf = open(datapath + '/' + 'INDI17Q2.txt', 'rt')
    for line in inputf:
        if line.upper().find('DIABET') >= 0:
            my_file.write(line)
    inputf.close()

    inputf = open(datapath + '/' + 'INDI17Q1.txt', 'rt')
    for line in inputf:
        if line.upper().find('DIABET') >= 0:
            my_file.write(line)
    inputf.close()


confirmed_drugL = ['EXENATIDE', 'GLIPIZIDE', 'TRULICITY', 'CANAGLIFLOZIN', 'GLICLAZIDE', 'GLIMEPIRIDE', 'LINAGLIPTIN', 'LIRAGLUTIDE']

with open(datapath + '/' + drugfile, 'wt') as my_file:
    inputf = open(datapath + '/' + 'DRUG18Q2.txt', 'rt')
    for line in inputf:
        for confdrug in confirmed_drugL:
            if line.upper().find(confdrug) >= 0:
                my_file.write('vali' + line)
                break
    inputf.close()

    inputf = open(datapath + '/' + 'DRUG18Q1.txt', 'rt')
    for line in inputf:
        for confdrug in confirmed_drugL:
            if line.upper().find(confdrug) >= 0:
                my_file.write(line)
                break
    inputf.close()

    inputf = open(datapath + '/' + 'DRUG17Q4.txt', 'rt')
    for line in inputf:
        for confdrug in confirmed_drugL:
            if line.upper().find(confdrug) >= 0:
                my_file.write(line)
                break
    inputf.close()

    inputf = open(datapath + '/' + 'DRUG17Q3.txt', 'rt')
    for line in inputf:
        for confdrug in confirmed_drugL:
            if line.upper().find(confdrug) >= 0:
                my_file.write(line)
                break
    inputf.close()

    inputf = open(datapath + '/' + 'DRUG17Q2.txt', 'rt')
    for line in inputf:
        for confdrug in confirmed_drugL:
            if line.upper().find(confdrug) >= 0:
                my_file.write(line)
                break
    inputf.close()

    inputf = open(datapath + '/' + 'DRUG17Q1.txt', 'rt')
    for line in inputf:
        for confdrug in confirmed_drugL:
            if line.upper().find(confdrug) >= 0:
                my_file.write(line)
                break
    inputf.close()



with open(datapath + '/' + aefile, 'wt') as my_file:
    inputf = open(datapath + '/' + 'REAC18Q2.txt', 'rt')
    for line in inputf:
        my_file.write('vali' + line)
    inputf.close()

    inputf = open(datapath + '/' + 'REAC18Q1.txt', 'rt')
    data = inputf.read()
    inputf.close()
    my_file.write(data)

    inputf = open(datapath + '/' + 'REAC17Q4.txt', 'rt')
    data = inputf.read()
    inputf.close()
    my_file.write(data)

    inputf = open(datapath + '/' + 'REAC17Q3.txt', 'rt')
    data = inputf.read()
    inputf.close()
    my_file.write(data)

    inputf = open(datapath + '/' + 'REAC17Q2.txt', 'rt')
    data = inputf.read()
    inputf.close()
    my_file.write(data)

    inputf = open(datapath + '/' + 'REAC17Q1.txt', 'rt')
    data = inputf.read()
    inputf.close()
    my_file.write(data)


