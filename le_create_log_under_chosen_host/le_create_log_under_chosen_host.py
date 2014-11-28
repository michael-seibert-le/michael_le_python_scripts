# coding: utf-8
#!/usr/bin/python


# THIS SCRIPT 
# 1. LISTS ALL OF YOUR HOST NAMES FOR A SPECIFIC ACCOUNT_KEY
# 2. ALLOWS YOU TO SELECT A SPECIFIC HOST IN WHICH TO CREATE A NEW LOG 
# 3. IT THEN PROMPTS YOU FOR A NEW LOG NAME
# 4. IT CREATES A LOG NAME UNDER YOUR SELECTED HOST

# REQUIREMENT - you must have your Logentries Account_Key and have at least one host in your account.

import urllib
import json
import sys
import os

ACCOUNT_KEY = ''
EXISTING_HOST_KEY = ''
HOST_NAME = ''
NEW_LOG_NAME = ''

#LISTS
HOST_NAMES =[]
HOST_KEYS = []


#gets host names and print to screen with numbers from which to choose 
def get_host_name():
    req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + '/hosts/')
    response = json.load(req)
    for hosts in response['list']:
        HOST_NAMES.append(hosts['name'])
        HOST_KEYS.append(hosts['key'])


    for i in range(0, len(HOST_NAMES)):
        print "["+str(i) +"] " + HOST_NAMES[i] + ' - ' + HOST_KEYS[i]
        get_log_name_and_token(HOST_KEYS[i])

    select_host()


def get_log_name_and_token(host_key):
    req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + '/hosts/' + host_key + '/')
    response = json.load(req)
    for log in response['list']:
        if log['type']== 'agent':
            print "\t"+ "AGENT path:" + log['filename'] + " key:" + log['key']
        elif log['type']=='token':
            print "\t"+"TOKEN name=" +log['name'] + " key:" + log['key'] + " Token:" + log['token']
        

def select_host():
    number = raw_input("Select the number of the Host in which you would like to add a new log: ")
 
    int_number = int(number)
    
    while int_number > len(HOST_NAMES)-1 or int_number < 0:
        print "INVALID NUMBER Please pick a number between 0 and " + str(len(HOST_NAMES)-1) + "."
        number = raw_input("Select the number of the Host in which you would like to add a new log: ")
        int_number = int(number)

    new_log_name = raw_input("Please enter the name of your new log to be created under - " + HOST_NAMES[int_number] + '. ')
        

    print "Creating Log titled " + new_log_name + " in host " + HOST_NAMES[int_number] + ". "
    create_log_in_host(HOST_KEYS[int_number], new_log_name, int(number))


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
        'source': 'token'
    })
    req = urllib.urlopen("http://api.logentries.com", request)


    print "log " + log_name + " has been created under host - " + HOST_NAMES[number] + "."


if __name__ == '__main__':
    ACCOUNT_KEY = sys.argv[1]
    get_host_name()

