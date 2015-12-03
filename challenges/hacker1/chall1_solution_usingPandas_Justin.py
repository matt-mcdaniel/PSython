#!/usr/bin/python2.7

'''
Pandas is a Python Package widely used for data analysis
http://pandas.pydata.org/
	-it also supports a function to import directly from excel
'''

import pandas as pd
import numpy as np

####Level 1
##bring in the data
data = pd.read_excel('PySA_hacker1.xlsx')

##print all the data
#print data

##Find the unique Installations
#make an empty uniques array
uniqueInst = []
#loop through the Installation data
for inst in data['Installation']:
	#if the Inst name is not found in the array
	if inst not in uniqueInst:
		#add it to the array
		uniqueInst.append(inst)

	else:
		#this is a duplicate so I don't need it
		pass

'''
#check the uniques?
for unique in uniqueInst:
	print unique
'''

##Find the unique Installation/Site Combos
#Pandas makes it easy to print the uniques
columns_You_want = ['Installation','Site']
instSiteCombos = data[columns_You_want]
#print instSiteCombos


##Get the cumulutive total
columns_You_want = ['Branch','Installation','Site','Total Amount']
instSiteAmount = data[columns_You_want]

#shows the total sum of just Installations
by_Inst = instSiteAmount.groupby(['Installation'])
#print by_Inst.sum()

#shows the total sum for an Inst/Site combo
by_InstSite = instSiteAmount.groupby(['Branch','Installation','Site'],as_index=False)
summed = by_InstSite.sum()


#shows the average for each Site
by_Site = instSiteAmount.groupby(['Branch','Installation','Site'],as_index=False)
avged = by_Site.mean()

#makes the solutions a dataframe in Pandas
s = pd.DataFrame(summed).reset_index()
a = pd.DataFrame(avged).reset_index()
a.rename(columns= {'Total Amount':'Average Cost'},inplace=True)

#writes the values to the excel files
writer = pd.ExcelWriter('answer1_summed.xlsx')
s.to_excel(writer,'Sheet1')
writer.save()

writer = pd.ExcelWriter('answer1_averaged.xlsx')
a.to_excel(writer,'Sheet1')
writer.save()







