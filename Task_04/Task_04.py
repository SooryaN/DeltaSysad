#!/usr/bin/python3
cmd="cat access.txt | awk '{print $9}'"
import os
from ipaddress import ip_address
res=os.popen(cmd).read()
res=res.split('\n')
status_code={}
for i in res:
	if i.isdigit():
		if i in status_code:
			status_code[i]+=1
		else:
			status_code[i]=1
print ("Status codes")
for i in status_code:
	print (i,':',status_code[i])
cmd="cat access.txt | awk '{print $1}'"
res=os.popen(cmd).read()
res=res.split('\n')
IP={}
for i in res:
	try:
		ip_address(i)
		if i in IP:
			IP[i]+=1
		else:
			IP[i]=1
	except:
		pass
print ("\nIPs")
for i in IP:
	print (i,':',IP[i])
