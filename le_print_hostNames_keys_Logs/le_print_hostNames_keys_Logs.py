# coding: utf-8
#!/usr/bin/python

# THis script prints an alphabetically sorted list of host names, respective host keys, associated logs and log details 
# The log details include: Token-based or agent-based, log name, log token and log key 

# REQUIREMENTS - You must have the Account Key of the Logentries Account on which you wish to run this script.
# This script was written and tested on Python 2.7.5.

# TO RUN:  python print_all_hostNames_keys_logs.py <ACCOUNT_KEY_HERE>

import urllib
import json
import sys
import os
import collections
import operator


ACCOUNT_KEY = ''
EXISTING_HOST_KEY = ''
HOST_NAMES_KEYS_DICT = {}

#gets host names
def get_host_name():
    req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + '/hosts/')
    response = json.load(req)
    for hosts in response['list']:
        HOST_NAMES_KEYS_DICT[hosts['key']] = hosts['name']


    i=0
    # the line below sorts the dictionary by the Values, which are the names of the Hosts.
    for k, v in sorted(HOST_NAMES_KEYS_DICT.iteritems(), key=operator.itemgetter(1)):
    #for k,v in HOST_NAMES_KEYS_DICT.items():
        print "["+str(i) +"] " + v + ' - ' + k
        i=i+1
        get_log_name_and_token(k)


def get_log_name_and_token(host_key):
    req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + '/hosts/' + host_key + '/')
    response = json.load(req)
    for log in response['list']:
        if log['type']== 'agent':
            print "\t"+ "AGENT path:" + log['filename'] + "  Log key:" + log['key']
        elif log['type']=='token':
            print "\t"+"TOKEN Name:" +log['name'] + "  Token:" + log['token'] + "  Log key:" + log['key']
        


if __name__ == '__main__':
    ACCOUNT_KEY = sys.argv[1]
    get_host_name()

