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
ALT_HOST_NANE = ''

#create a new host under the exiting Account Key.
# might need to check for duplicates as this can be an issue
def create_host_in_account():
    request = urllib.urlencode({
        'request': 'register',
        'user_key': ACCOUNT_KEY,
        'name': HOST_NAME,
        'hostname': ALT_HOST_NANE,
        'distver': '',
        'system': '',
        'distname': '',
    })
    req = urllib.urlopen("http://api.logentries.com", request)

    print "log \'" + HOST_NAME + "\' has been created under your account with an alter host name of \'" + ALT_HOST_NANE + "\' ."


if __name__ == '__main__':
    ACCOUNT_KEY = sys.argv[1]
    HOST_NAME = sys.argv[2]
    ALT_HOST_NANE = sys.argv[3]
    create_host_in_account()

