import sys
import os
#accepts directory as argument  
where=sys.argv[1]
os.chdir(where)

#Script 1: This Script should create a new database. It should also create a table and a column in the newly created database.
filename="script1.py"
f=open(filename,'w')
os.system('chmod a+x '+filename)
f.write('#!/usr/bin/env python\n')
f.write('import sqlite3 as lite\n')
f.write('con = lite.connect("'+where+'/trial.db")\n')
f.write('with con:\n')
f.write('    cur = con.cursor()\n')
f.write('    cur.execute("CREATE TABLE Timer(Time TEXT)")\n')
f.write('con.commit()\n')
f.write('con.close()\n')
f.close() 
os.system('/usr/bin/python script1.py')	

#Script 2: This Script should insert the current time in the newly created table of the database, that was created by Python Script 1.
filename="script2.py"
f=open(filename,'w')
os.system('chmod a+x '+filename)
f.write('#!/usr/bin/env python\n')
f.write('import sqlite3 as lite\n')
f.write('from time import strftime\n')
f.write('con = lite.connect("'+where+'/trial.db")'+'\n')
f.write('time=strftime("%H:%M:%S")\n')
f.write('with con:\n')
f.write('	cur = con.cursor()\n')
f.write("	con.execute('INSERT INTO {} ({}) VALUES (?)'.format('Timer', 'Time'), (time,))\n")
f.write('con.commit()\n')
f.write('con.close()\n')
f.close() 
#writing to crontab
#(crontab -l ; echo "*/10 * * * * python script.py")| crontab -

wr= 'echo'+ ' "*/10 * * * * '+'/usr/bin/python '+where+'/script2.py"'
cmd= '(crontab -l;'+wr+')| crontab -'
os.system(cmd)
