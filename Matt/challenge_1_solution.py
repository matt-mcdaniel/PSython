import sys
import csv

item_position = { 'branch': 0, 'inst': 1, 'site': 2, 'typ': 3, 'amt': 4 }

f = open(sys.argv[1], 'rd') # 1.1 Bring data into Python
reader = csv.reader(f)
data = list(reader)[1:]
# print data # 1.2 Print all the data

f2 = open(sys.argv[2], 'wt')
file1 = csv.writer(f2)

f3 = open(sys.argv[3], 'wt')
file2 = csv.writer(f3)

brac = [ x for x in data if x[item_position['branch']] == 'BRAC' ]
non_brac = [ x for x in data if x[item_position['branch']] != 'BRAC' ]

def unique(dataset):
    return list(set((x[item_position['inst']]) for x in dataset))

def unique_multiple(dataset):
    tpls = list(set((x[item_position['inst']], x[item_position['site']]) for x in dataset))
    return [[i[0], i[1]] for i in tpls] # Identify Unique Installation/Site Combinations # Returns [ [ 'inst', 'site' ] ]
    
unique_inst = unique(data) # 1.3 Identify Unique Installations

unique_inst_site = unique_multiple(data) # 1.4 Identify Unique Inst/Site Combos
brac_unique_inst_site = unique_multiple(brac)
non_brac_unique_inst_site = unique_multiple(non_brac)
 
def get_total_average(match_list):
    avgList = []
    for e in match_list:
        count = 0
        amount = 0
        for l in data:
            if all(i in l for i in e):
                amount += int(l[item_position['amt']])
                count += 1
        avgList.append(e + [amount] + [amount/count])
    return avgList

all_avg = get_total_average(unique_inst_site) # 2.1, 2.2, 2.3 Sum Costs and Average for Inst/Site Combo
brac_avg = get_total_average(brac_unique_inst_site)
non_brac_avg = get_total_average(non_brac_unique_inst_site)

def print_to_csv(header, item, which_file):
    which_file.writerow([value for value in header])
    for i in range(len(item)):
        which_file.writerow(item[i])

# 2.4 Write the answer to .csv
# print_to_csv(['Installation', 'Site', 'Total', 'Average'], all_avg, file1)

# 3.1
# Prints All Unique Inst/Site Combos for BRAC Data
print_to_csv(['Installation', 'Site', 'Total', 'Average'], brac_avg, file1)
# Prints All Unique Inst/Site Combos for Non-BRAC Data
print_to_csv(['Installation', 'Site', 'Total', 'Average'], non_brac_avg, file2)

f.close()
f2.close()
f3.close()