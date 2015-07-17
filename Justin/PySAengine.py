import sqlite3
import csv


##################-- THIS IS A MODULE FOR USE OF PySA ONLY --##########################

#de-string-ifies a string to print better
def deStringify(x):
    startingInfo = str(x).replace('[','').replace(']','').replace(')','').replace('(','').replace('u\'','').replace("'","")
    #print startingInfo
    return startingInfo


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

    

#############--EVERYTHING SQL--##########################
def returnTableColNames(whatDB,whatTable):
    """This takes the table name and returns all its col names"""
    con = sqlite3.connect(whatDB)
    c = con.cursor()
    c.execute("PRAGMA table_info("+whatTable+")")
    
    #create an array to return
    returnArray = []
    for row in c.fetchall():
        #destringify return values
        startingInfo = str(row).replace('[','').replace(']','').replace(')','').replace('(','').replace('u\'','').replace("'","").replace(" ","")
        splitInfo = startingInfo.split(',')
        returnArray.append(splitInfo)
    
    return returnArray


def runSQL(whatDB,sql,numVar):
    #connect to DB
    conn = sqlite3.connect(whatDB)
    conn.text_factory = str
    c = conn.cursor()
    print "Executing ",sql
    print "Numvar is =",numVar
    
    #create an array to return
    returnArray = []
    for row in c.execute(sql):
        #print row
        #destringify return values
        startingInfo = str(row).replace('[','').replace(']','').replace(')','').replace('(','').replace('u\'','').replace("'","")
        splitInfo = startingInfo.split(',')

       
        returnArrayAppend = []
        for i in range(numVar):
            if i <= numVar-1:
                #print i
                #print splitInfo[i]
                #if it starts with a blank, delete the first blank
                if splitInfo[i].startswith(" "):
                    toFix = splitInfo[i]
                    fixed = toFix[1:]
                    #print "After",fixed
                    returnArrayAppend.append(fixed)

                #if it ends with a blank, delete that   
                #if splitInfo[i].endswith(" "):
                    #each = each[:-1]
                    #print "After",each
                    #c.append(each)
                    
                #if it doesn't have a starting blank, then continue adding the original
                else:
                    #print "This did not have a starting blank",splitInfo[i]
                    returnArrayAppend.append(splitInfo[i])

                #returnArrayAppend.append(splitInfo[i])
                
        returnArray.append(returnArrayAppend)
        #returnArray.append(splitInfo[0])

    #check return array for [] -- this means I need to check the aliases
	#print "I made it here"
    if returnArray != []:
        #print returnArray
		
        return returnArray
        #return A.find_Dupes(returnArray)
        
    else:
        print returnArray
        print ""*5
        print "I'm sorry, your Installation names do not match..."
        print "Troubleshooting your information..... "+sql+""

   
def selectAll(whatDB,whatTable):
    #connect to DB
    conn = sqlite3.connect(whatDB)
    c = conn.cursor()
    sql = "SELECT * FROM "+whatTable+""
 
    #create an array to return
    returnArray = []
    #start loop to dump values
    for row in c.execute(sql):
        #destringify return values
        startingInfo = str(row).replace('[','').replace(']','').replace(')','').replace('(','').replace('u\'','').replace("'","")
        splitInfo = startingInfo.split(',')
        returnArray.append(splitInfo)
        
    return returnArray
    #return find_Dupes(returnArray)


        
#using writeThis, dump just a table name
def dumpTable(whatTable,whatDB):
    """Prints 'whatTable' to CSV file """
    dateFormat = "%m/%d/%Y"
    today = time.strptime(time.strftime(dateFormat),dateFormat)
    print "Writing this ",whatTable
    writeThis(selectAll(whatDB,whatTable),""+whatTable+"_"+str(today.tm_mon)+"_"+str(today.tm_mday)+"")


#update a table with some information
def simpUp(whatDB,updateTable,updateWith,delYes=None,headrzYes=None):
    """delete and update query, if you want the deletion, delYes = YY """
    sqlDel = "DELETE FROM "+updateTable+""
    #get table names
    if headrzYes != "YY":
        colNames = returnTableColNames(whatDB,updateTable)
        cols = []
        for lin in colNames:
            cols.append(lin[1])
    else:
        colNames = updateWith.pop(0)
        print "I have these for ",updateTable,"'s column names:"
        cols = []
        for lin in colNames:
            cols.append(lin)

    
    q = []
    for i in range(len(colNames)):
        q.append('?')
    
    sql = "INSERT INTO "+updateTable+"("+deStringify(cols)+") VALUES ("+deStringify(q)+");"
    #print sql
    #connect to DB
    conn = sqlite3.connect(whatDB)
    conn.text_factory = str
    c = conn.cursor()
    #first we delete the previous data
    #delYes = str(raw_input("Updating....This will delete everything currently in "+updateTable+", enter YY to agree, otherwise anything else > "))
    if delYes == "YY":
        c.execute(sqlDel)
        print "Deleted what was there...updating with new data"
    print sql
    c.executemany(sql,updateWith)
    conn.commit()
    print "Updated "+updateTable+" with ",sql


#make headers for DB
def makeHeader(headers):
    fixedHeader = []
    newHeader = []
    print "These are the headers from your file:"
    #get the headers to make a table
    for lin in headers:
        #lowers all words, replaces any spaces with underscore
        hdr = lin.lower().replace(" ","_").replace("&","_").replace(".","_").replace("/","_")
        print hdr
        #put the fixed header name to save for data entry
        fixedHeader.append(hdr)
        #you must define the types...will probably need if/then one day
        tpe = "TEXT"#raw_input("What type is this header: "+hdr+" (text,real,date,etc)? ")
        print "Used",tpe,"as for this field"
        #joins them together and adds them to an array
        joinThem = hdr+" "+tpe
        newHeader.append(joinThem)
    return (newHeader,fixedHeader)



#create a DB and a Table
def createNewTable(whatFile):    
    print "Opening the file and grabbing the headers..."
    
    master = regImport(whatFile)
    #filelist = [line.rstrip('\n') for line in file]
    headers = master[0]
    nameDB = raw_input("What is the name of the database? ")
    
    print "So you have database named "+nameDB+""
    print "now we'll make a new table"
   
    newTable = str(raw_input("What is the name of the New Table?: "))

    #this is the new header
    newHeader,fixedHeader = makeHeader(headers)      
    newHeader = deStringify(newHeader)

    print "These are the new headers, I'm ready to make the "+newTable+" table:"
    print newHeader,len(newHeader)
    yesVal = raw_input("Are the above values correct?(Y/N) ")
    if yesVal == "Y":
        try:
            #connect to DB
            conn = sqlite3.connect(nameDB)
            #establish the cursor
            c = conn.cursor()
            #add the syntax to the new header formats
            create = "CREATE TABLE "+newTable+"("+newHeader+")"
            print create
            #at the cursor, create a table
            c.execute(create)
            
            #enter the data
            conn.commit()
            print "You have successfully created "+nameDB+""
            print ".......This is the first and only time you do this....."
            print ".......Forevermore you shall only connect...."

            yesInput = raw_input("Should I input the data?(Y/N) ")
            if yesInput != "N":
                #dataEntry(nameDB,whatFile,newTable,fixedHeader)
                simpUp(nameDB,newTable,master[1::])
                #see if we should start mining
                startMine = str(raw_input("Do you want to start other algorithms here?> "))
                if startMine == "Y":
                    #ez.mineForMatches()
                    pass
        except:
            c.close()
            raw_input("This will delete what was already in "+newTable+", press ENTER to continue...")
            simpUp(nameDB,newTable,master[1::],"YY")
    else:
        print "Sorry, I will have to run this again"
