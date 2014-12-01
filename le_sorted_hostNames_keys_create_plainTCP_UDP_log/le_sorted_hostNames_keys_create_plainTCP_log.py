# coding: utf-8
#!/usr/bin/python


# THIS SCRIPT WILL:
# 1. LISTS ALL OF YOUR HOST NAMES & HOST KEYS FOR AN ACCOUNT (Host Names are in alphabetical order)
# 2. UNDERNEATH EACH HOST, THE LOGS FOR THAT HOST WILL BE LISTED (In no order)
#    LOG DETAILS INCLUDE: TOKEN-BASED OR AGENT-BASED, LOG NAME, LOG TOKEN AND LOGKEY
# 3. IT WILL PROMPT YOU TO PICK A NUMBER ASSIGNED TO EACH HOST TO CREATE A LOG UNDER THIS HOST NAME 
# 4. IT THEN PROMPTS YOU FOR A NEW LOG NAME
# 5. IT CREATES A PLAIN TCP UDP LOG NAME UNDER YOUR SELECTED HOST AND CONFIRMS IT.

# REQUIREMENT - you must have your Logentries Account_Key and have at least one host in your account.
# TO RUN:  python print_sorted_hostNames_keys_and_logs.py <ACCOUNT_KEY>


import urllib
import json
import sys
import os
import collections
import operator


ACCOUNT_KEY = ''
EXISTING_HOST_KEY = ''
HOST_NAME = ''
NEW_LOG_NAME = ''

#LISTS
HOST_NAMES =[]
HOST_KEYS = []
HOST_NAMES_KEYS_DICT = {}
host_key_list = []

#gets host names
def get_host_name():
    req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + '/hosts/')
    response = json.load(req)
    for hosts in response['list']:
        HOST_NAMES_KEYS_DICT[hosts['key']] = hosts['name']
        # HOST_NAMES.append(hosts['name'])
        # HOST_KEYS.append(hosts['key'])

    i =0
    # the line below sorts the dictionary by the Values, which are the names of the Hosts.
    for k, v in sorted(HOST_NAMES_KEYS_DICT.iteritems(), key=operator.itemgetter(1)):
    #for k,v in HOST_NAMES_KEYS_DICT.items():
        print "["+str(i) +"] " + v + ' - ' + k
        HOST_KEYS.insert(i, k)
        HOST_NAMES.insert(i, v)
        i=i+1
        get_log_name_and_token(k)


    select_host()


def get_log_name_and_token(host_key):
    req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + '/hosts/' + host_key + '/')
    response = json.load(req)
    for log in response['list']:
        if log['type']== 'agent':
            print "\t"+ "AGENT path:" + log['filename'] + " log key:" + log['key']
        elif log['type']=='token':
            print "\t"+"TOKEN Name:" +log['name'] + " Token:" + log['token'] + " log key:" + log['key']
        

def select_host():
    
    number = raw_input("Select the number of the Host in which you would like to add a new log: ")
 
    int_number = int(number)
    while int_number > len(HOST_NAMES_KEYS_DICT)-1 or int_number < 0:
        print "INVALID NUMBER Please pick a number between 0 and " + str(len(HOST_NAMES_KEYS_DICT)-1) + "."
        number = raw_input("Select the number of the Host in which you would like to add a new log: ")
        int_number = int(number)
   
    new_log_name = raw_input("Please enter the name of your new log to be created under your Host- " + HOST_NAMES[int_number] + '. ')
        

    print "Creating Log titled \'" + new_log_name + "\' in host " + HOST_NAMES[int_number] + ". "
    create_log_in_host(HOST_KEYS[int_number], new_log_name, number)


#create a new log under the Host Name that is listed.
# might need to check for duplicates as this can be an issue
def create_log_in_host(existing_host_key, log_name, number):
    request = urllib.urlencode({
        'request': 'new_log',
        'user_key': ACCOUNT_KEY,
        'host_key': existing_host_key,
        'name': log_name,
        'type': '',
        'filename': '',
        'retention': '-1',
        'source': 'syslog'
    })
    req = urllib.urlopen("http://api.logentries.com", request)

    response = json.load(req)
      
    # print "name: " + response['log']['name'] + " port: " + str(response['log']['port']) + " type: " + response['log']['type']
    print "name:{0[name]}  port:{0[port]}  type:{0[type]}".format(response['log'])

if __name__ == '__main__':
    ACCOUNT_KEY = sys.argv[1]
    get_host_name()

