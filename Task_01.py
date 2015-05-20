import os
curr=os.getcwd()
for i in range (1,101):
	folderName='folder'+str(i)
	os.mkdir(folderName)
	cmd1='chmod 0700 '+folderName
	os.system(cmd1)
	os.chdir(folderName)
	filename=folderName+'.txt'
	file=open(filename,'a')
	file.close()
	cmd2='chmod 0700 '+filename
	os.system(cmd2)
	os.chdir(curr)
