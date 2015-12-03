Your client thinks you know everything there is to know about databases. So she gives you three different spreadsheets and wants to know the following:
a.	Which Installations/Sites are in the original (pysa_hacker1.xlsx)?
b.	I don't know which kind of Installation it is, Active or BRAC.  I need to know that as well.
c.	Could you add the CTCs (Cost to Complete) and TTCs (Time to Complete) for each Installation/Site/Technology?
d.	Oh, and can you also provide a column with the averages for each?



-- Challenge 3 --

OBJ
Level 1
1. Configure SQLite3
2. Create Action Plan for Kaggle

Level2
3. Import data from file into SQLite3 DB table
4. Evaluate 1 Script from kaggle.com and research some of the operations used

Level3
5. Find unique values from a SQL table using Python

Level4 - Should you dare...
6. Create your client's spreadsheet


Kaggling
- Identify what goes with what (column names match what column names in what file)
- Pick a Script (any script) from Kaggle and:
                -evaluate what their doing and what library their using
                -research any terms unknown
                -Be prepared to give a 3 sentence summation of Lessons Learned



SQL 
- first test "import sqlite3" to see if you have it (sometimes it comes with the installation)
- pip install sqlite3 if it's not there
- http://sqlitebrowser.org/  <-- download this browser so you can read the .db files and see the data
- Import data files and create a table
- Find the unique Installations and Sites
- Get data from 3 different tables and print out an array with specific information

-Make the Below Array
[Kind (BRAC or Active?),Installation,Site,Technology,CTC_Calc_H,TTC_Calc_H,CTC_ACT,TTC_ACT, Average_CTC_H,Average_TTC_H,Average_CTC_ACT,Average_TTC_ACT]
                #hints -- use numpy to find averages...its just easier
                       -- sql formats look like this:
                                  SELECT <columns you want> FROM <some table>
                                  SELECT <""> FROM <""> WHERE <Column to Match> = <Value to Match>
                     -- lookup INSERT INTO  and SELECT DISTINCT


-Print the above array to a .CSV file for delivery





