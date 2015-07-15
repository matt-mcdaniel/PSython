import csv
import operator
from collections import defaultdict

print ""
headers = []
first = []
second = []
third = []
fourth = []
fifth = []
sixth = []
all = []
twothree = []
islist = []

with open('PySA1.csv', 'rb') as csvfile:
	sortfile = csv.reader(csvfile)
	sortheaders = sortfile.next()
	headerindex1 = sortheaders.index('Site')
	sortedlist1 = sorted(sortfile, key=operator.itemgetter(headerindex1))
	headerindex2 = sortheaders.index('Installation')
	sortedlist2 = sorted(sortedlist1, key=operator.itemgetter(headerindex2))
	headerindex3 = sortheaders.index('Branch')
	sortedlist3 = sorted(sortedlist1, key=operator.itemgetter(headerindex3))
	csvfile.close()
	
	
	
sorter = open('sorted.csv', 'wb')
sortedfile = csv.writer(sorter)
sortedfile.writerow(sortheaders)
for row in sortedlist3:
	if "Flag" not in row and "n/a" not in row:
		sortedfile.writerow(row)
sorter.close()

d = defaultdict(int)

with open("sorted.csv", "rb") as f:
	fheaders = f.next()
	stream = csv.reader(f)
	data = list(stream)
	for line in data:
		try:
			instsite = (line[1], line[2])
			cost = int(line[4])
		except ValueError:
			print line
		d[instsite] += cost
f.close()
print type(data)

for key, value in d.iteritems():
	k = list(key)
	k.append(value)
	islist.append(k)

with open('sorted.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	headers = reader.next()
	brac = open("BRAC_Sites.csv", "wb")
	act = open("Active_Sites.csv", "wb")
	stat = open("Stats.csv", "wb")
	oview = open("Installation_Site_Cost.csv", "wb")
	bracwrite = csv.writer(brac)
	actwrite = csv.writer(act)
	statwrite = csv.writer(stat)
	oviewwrite = csv.writer(oview)
	for row in reader:
		first.append(row[0])
		second.append(row[1])
		third.append(row[2])
		fourth.append(row[3])
		fifth.append(row[4])
		twth = row[1] + row[2]
		twothree.append(twth)
		if "BRAC" in row:
			bracwrite.writerow(row)
		else:
			actwrite.writerow(row)
	for r in islist:
		oviewwrite.writerow(r)

statdict = {}
		
print "Total entries: ", len(first)
statdict["Total entries:"] = len(first)

print "Headers are: ",
y = ", ".join(headers)
print y
statdict["Headers:"] = y
		
firstset = set(first)	
print "All Unique values for ", headers[0], ": ", 
x = ", ".join(firstset)
print x
stat1 = str(headers[0] + " Unique Values:")
statdict[stat1] = x

twothreeset = set(twothree)
stat2 = str(headers[1] + " and " + headers[2] + "Unique Values:")
print "Unique values for ", headers[1], " and ", headers[2], ": ", len(twothreeset)
statdict[stat2] = len(twothreeset)

fifthint = map(int, fifth)
totalcost = sum(fifthint)
print "Total cost is: $", totalcost
twthst = len(twothreeset)
averagecost1 = totalcost / twthst
averagecost2 = sum(d.itervalues()) / len(d)
print "Average cost per entry: $", averagecost1
statdict["Entry Average Cost:"] = averagecost1
print "Average cost per Installation/Site: $", averagecost2
statdict["Inst/Site Average Cost:"] = averagecost2

secondset = set(second)
print "Unique values for ", headers[1], ": ", len(secondset)
stat3 = str(headers[1] + " No. of Unique Entries:")
statdict[stat3] = len(secondset)

thirdset = set(third)
print "Unique values for ", headers[2], ": ", len(thirdset)
stat4 = str(headers[2] + " No. of Unique Entries:")
statdict[stat4] = len(thirdset)

fourthset = set(fourth)
print "Unique values for ", headers[3], ": ", len(fourthset)
stat5 = str(headers[3] + " No. of Unique Entries:")
statdict[stat5] = len(fourthset)

fifthset = set(fifth)
print "Unique values for ", headers[4], ": ", len(fifthset)
stat6 = str(headers[4] + " No. of Unique Entries:")
statdict[stat6] = len(fifthset)

print ""

for key, value in statdict.items():
	statwrite.writerow([key, value])

brac.close()
act.close()
stat.close()
oview.close()