# coding: utf-8
#!/usr/bin/python

# THIS SCRIPT FINDS LOGS WITHIN THE SPECIFIED ACCOUNT_KEY & HOST_NAME, THEN OUTPUTS A JSON OBJECT IN THE FORM OF: 
'''
{
    "logs": [
        {
            "path": "/home/stephen/LE/Languages/python/test.log",
            "name": "test.log",
            "token": "LOG_TOKEN"
        }
    ]
}
'''

# REQUIREMENTS - LOGENTRIES ACCOUNT KEY & SPECIFIC HOST NAME  (This Host Name is Case-Sensitive) 
# THIS SCRIPT ONLY PRINTS TOKEN-BASED LOGS, IF YOUR HOST ONLY HAS AGENT BASED LOGS, NO JSON OBJECT WILL BE WRITTEN TO FILE.


import urllib
import json
import sys
import os

ACCOUNT_KEY = ''
HOST_NAME = ''


#first get all the hosts....
def get_host():
	req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + "/hosts/")
	response = json.load(req)
	for hosts in response['list']:
		if HOST_NAME == hosts['name']:
			print HOST_NAME + " --- " + hosts['key']
			print " "
			host_key = hosts['key']
			get_log_names(host_key)


def get_log_names(host_key):
	req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + "/hosts/" + host_key + "/")
	response = json.load(req)

	f = open("logs.json", "w")
	f.write("{\n\t\"logs\": [\n")
	#print "{\n\t\"logs\": [\n"

# ONLY WRITE TOKEN BASED LOGS
	count = 0
	for log in response['list']:
		if 'token' not in log:
			token = ''
		else:  
			count+=1
			token = log['token']
			name = log['name']
			path = log['filename']
		
		
		#print name + " " + path + " " + token 
		#print 
	#		print "\t\t{\n\t\t\t\"path\": \"" + path +"\",\n\t\t\t\"name\": \"" + name + "\",\n\t\t\t\"token\": \"" + token +"\"\n\t\t}\n"
			f.write("\t\t{\n\t\t\t\"path\": \"" + path +"\",\n\t\t\t\"name\": \"" + name + "\",\n\t\t\t\"token\": \"" + token +"\"\n\t\t}\n")
	#print "\t]\n}"
	f.write("\t]\n}")

	f.close()

	if count==0:
		f = open("logs.json", "w")
		f.write("NO TOKEN BASED LOGS IN YOUR SELECTED HOST")
		f.close()

	print "READING AND PRINTING CONTENTS OF \'logs.json\' FILE TO SCREEN AS CONFIRMATION"
	print "-------------------------------------------------------"
	f = open('logs.json', 'r')
	print f.read()
	f.close()


if __name__ == '__main__':
    ACCOUNT_KEY = sys.argv[1]
    HOST_NAME = sys.argv[2]
    get_host()

