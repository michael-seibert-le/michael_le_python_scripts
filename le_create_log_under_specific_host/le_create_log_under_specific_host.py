# coding: utf-8
#!/usr/bin/python

# THIS SCRIPT 
# 1. Finds a host named from  from sys.argv[2]
# 2. It then takes that host_key for the host and uses it to create a new log under that host
# 3. The new log name is specified from sys.argv[3]

# REQUIREMENT - you must have a valid ACCOUNT_KEY
# And have a host name that matches matches sys.argv[2] (case sensitive) for this script to work.
# TO USE:  python create_log_in_host <ACCOUNT_KEY> <EXISTING_HOST_NAME> <NEW_LOG_NAME>

import urllib
import json
import sys
import os


ACCOUNT_KEY = ''
HOST_NAME = ''
NEW_LOG_NAME = ''

#LISTS
HOST_NAMES =[]
HOST_KEYS = []


#gets host names
def get_host_name():
    req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + '/hosts/')
    response = json.load(req)
    for hosts in response['list']:
        if HOST_NAME == hosts['name']:
            print HOST_NAME + " has a host key of: " + hosts['key']
            print hosts['name'] +" ---- " + hosts['key']
            create_log_in_host(hosts['key'], hosts['name'])
     

#create a new log under the Host Name that is listed.
# might need to check for duplicates as this can be an issue
def create_log_in_host(existing_host_key, a_host_name):
    request = urllib.urlencode({
        'request': 'new_log',
        'user_key': ACCOUNT_KEY,
        'host_key': existing_host_key,
        'name': NEW_LOG_NAME,
        'type': '',
        'filename': '',
        'retention': '-1',
        'source': 'token'
    })
    req = urllib.urlopen("http://api.logentries.com", request)

    print "log \'" + NEW_LOG_NAME + "\' has been created under \'" + a_host_name + "\' Host."


if __name__ == '__main__':
    ACCOUNT_KEY = sys.argv[1]
    HOST_NAME = sys.argv[2]
    NEW_LOG_NAME = sys.argv[3]
    get_host_name()

