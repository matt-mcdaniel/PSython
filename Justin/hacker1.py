import csv
import os
import time
import numpy as np
import PySAengine as Engine

#go find all the values in this folder
def directory_listing(dir_name):
    dir_file_list = {}
    dir_root = None
    dir_trim = 0
    for path,dirs,files in os.walk(dir_name):
        if dir_root is None:
            dir_root = path
            dir_trim = len(dir_root)
            print "dir",dir_name
            print "root is",dir_root
        trimmed_path = path[dir_trim:]
        if trimmed_path.startswith(os.path.sep):
            trimmed_path = trimmed_path[1:]
        for each_file in files:
            file_path = os.path.join(trimmed_path,each_file)
            dir_file_list[file_path] = True
            #print file_path
    return (dir_file_list,dir_root)


#gets the contents of the current folder
def getContents(folderLocation):
    """point to a 'folderLocation' """
    dir_file_list,dir_root = directory_listing(folderLocation)
    print "There are ",len(dir_file_list)," files in this folder"
    contents = dir_file_list.items()
    for name in contents:
        print name
    return contents

#import the file you want
def regImport(fileName):
    infile = open(fileName,'rb')
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



#WRITE FILE - define a funtion to write to a file
def writeThis(dataArray,Name):
    count = 0
    for few in dataArray:
        if count <= 5:
            print few
        count += 1
    print "Printing the above format..."
    yes = "Y"#str(raw_input("Is the above what you want to print? (Y/N) "))
    #print yes
    if yes == "Y":
        outfile = open(""+Name+".csv",'w')
        out = csv.writer(outfile,lineterminator='\n')
        #out.writerow(headerArray)
        for data in dataArray:
            #print "This made it"
            #print data
            out.writerow(data)
        outfile.close()
        print "Your file ",Name," has been written"


#get unique values of one table
def getUniques(whatDB,whatCols,fromTable,numVar):
    """returns unique values for 'whatCols' in 'fromTable' and 'numVar' is equal to the number of input variables"""
    sql = "SELECT DISTINCT "+whatCols+" FROM "+fromTable+""

    values = Engine.runSQL(whatDB,sql,numVar)

    return values
        
#get where Something is equal to something
def getWhere2(whatDB,whatCols,fromTable,fromCol,equalTo,fromCol2,equalTo2,numVar):
    """returns 'whatCols' values 'fromTable' where 'fromCol' is 'equalTo' some input, 'numVar' is equal to the number of input variables"""
    fixedEqualTo = "'"+equalTo+"'"
    fixedEqualTo2 = "'"+equalTo2+"'"
    sql = "SELECT "+whatCols+" FROM "+fromTable+" WHERE "+fromCol+" = "+fixedEqualTo+" and "+fromCol2+" = "+fixedEqualTo2+""

    return Engine.runSQL(whatDB,sql,numVar)




########WORK LINE###########
def doHw1():
    #get a subfolder and the fileName of associated CSVs in it
    a = getContents(whatFolder)
    CSVs = [x for x in a if x[0].endswith(".csv")]
    fileName = CSVs[0][0]
    #create a new DB table using the contents of the csv
    Engine.createNewTable(fileName)
    #get the unique values in the contents
    uniques = getUniques(whatDB,whatCols,fromTable,numVar)

    #get all associated values that match inst/site combo
    answerArray = []
    for combo in uniques:
        branch = combo[0]
        inst = combo[1]
        site = combo[2]
        amounts = getWhere2(whatDB,"total_amount",fromTable,"Installation",inst,"Site",site,1)
        #print amounts
        amt = [] 
        for each in amounts:
            each = float(each[0])
            amt.append(each)

        #check lengths
        if len(amt) == 1:
            total = amt[0]
            av = amt[0]
        else:
            total = sum(amt)
            #for num in each:
                #total += num[0]
            av = np.average(amt)
           
        answerArray.append([branch,inst,site,total,av])
    
    #split brac sites, and print both
    bracs = []
    for each in answerArray:
        if each[0] == "BRAC":
            bracs.append(each)

    #print files
    #add headers
    h = ['BRANCH','Installation','Site','Total','Average']
    answerArray.insert(0,h)
    bracs.insert(0,h)
    writeThis(answerArray,"answer1All")
    writeThis(bracs,"answer2BRACs")

    

whatDB = "PySA.db"
whatCols = "Branch,Installation,Site"
fromTable = "hackerHW1"
whatFolder = "hw1"
numVar = 3



