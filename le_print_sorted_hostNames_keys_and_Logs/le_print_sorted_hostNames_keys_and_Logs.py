# coding: utf-8

#!/usr/bin/python


# THIS SCRIPT PRINTS AN ALPHABETICALLY SORTED LIST OF HOST NAMES, THEIR HOST KEYS AND THEIR ASSOCIATED LOGS AND LOG DETAILS 
     #LOG DETAILS INCLUDE: TOKEN-BASED OR AGENT-BASED, LOG NAME, LOG TOKEN AND LOGKEY
#   

# REQUIREMENT - You must have the Account Key of the Logentries Account you wish to run this script against.

# TO RUN:  python print_sorted_hostNames_keys_and_logs.py <ACCOUNT_KEY_HERE>


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
        i=i+1
        get_log_name_and_token(k)

    #select_host()


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

    new_log_name = raw_input("Please enter the name of your new log to be created under - " + HOST_NAMES[int_number] + '. ')
        

    print "Creating Log titled " + new_log_name + " in host " + HOST_NAMES[int_number] + ". "
    create_log_in_host(HOST_KEYS[int_number], new_log_name)


#create a new log under the Host Name that is listed.
# might need to check for duplicates as this can be an issue
def create_log_in_host(existing_host_key, log_name):
    request = urllib.urlencode({
        'request': 'new_log',
        'user_key': ACCOUNT_KEY,
        'host_key': existing_host_key,
        'name': log_name,
        'type': '',
        'filename': '',
        'retention': '-1',
        'source': 'token'
    })
    req = urllib.urlopen("http://api.logentries.com", request)


    print "log " + log_name + " has been created."


if __name__ == '__main__':
    ACCOUNT_KEY = sys.argv[1]
    # HOST_NAME = sys.argv[2]
    # NEW_LOG_NAME = sys.argv[3]
    get_host_name()

