import os
import csv

path = 'C:\\Users\\564930\\desktop\\pysa\\kag\\data\\competition_data'
data = []
allheaders = []
allh = []
	
def File_Analysis(data):
	headers = data[:1]
	noheaders = data[1:]
	return headers

def Unique_Val_s(datafile, ip):
	list(set((x[item_position[ip]]) for x in datafile))

def regImport(path, fileName):
    infile = open(os.path.join(path, fileName), 'rb')
    reader = csv.reader(infile)
    print "import finished...."
    print "Printing the Titles"
    count = 0
    lst = []
    for line in reader:
        lst.append(line)
        if count <=0:
          print ""+str(line)+"\n"
        count += 1
    return lst
    infile.close()	

'''	
for fn in os.listdir(path):
	data = regImport(path, fn)
	for line in data:
	'''	


for fn in os.listdir(path):
	f = open(os.path.join(path, fn), 'rb')
	file1 = csv.reader(f)
	data = list(file1)
	print ""
	print fn
	print "================"
	h = File_Analysis(data)
	count = 0
	for item in h[0]:
		unique_vals = len(list(set((x[count]) for x in data if x != "NA")))
		count += 1
		print item, ":", unique_vals
	for e in h:
		for f in e:
			allheaders.append(f)

print ""
print "All Headers"
print "================"
allh = set(allheaders)
print "Total headers:", len(allh)
for item in allh:
	print item