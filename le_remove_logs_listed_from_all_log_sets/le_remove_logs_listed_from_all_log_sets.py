# le_remove_logs_listed_from_all_log_sets.py
# coding: utf-8
#!/usr/bin/python

'''
DO NOT USE THIS SCRIPT IF YOU ARE UNCERTAIN OF WHAT IT WILL DO TO YOUR LOG SETS OR LOGS.

USE AT YOUR OWN RISK AS THE DELETED LOGS WILL BE PERMANETLY DELETED AND CANNOT BE REVERTED.
'''


# THIS SCRIPT:
# 1. Examines all of your Log Sets / Hosts for the names currently in the Log set logs and compares them against log names in 'delete_log_names' List

# 2.  If the log names matches the element in 'delete_log_names' List
#     It then takes that log_key and host_key (log set key) adds that to a dictionary

# 3. Once all Log Sets (hosts) have been checked for matching log names, it will then remove these logs
#    from all Log Sets permanently -  THIS CANNOT BE UNDONE.

'''
BE SURE TO CHECK THIS SCRIPT WILL WORK FOR YOU SMALL SCALE BEFORE IMPLEMENTING IT ON A LARGE SCALE!

ALSO
DOUBLE CHECK & ALTER
    The 'delete_log_names' list
    to be sure your list matches (case and letters) precisely the 
    log names you wish to delete permanently.
'''

# REQUIREMENT - you must have a valid ACCOUNT_KEY

# TO USE:  python le_remove_log_list_from_all_hosts.py <ACCOUNT_KEY>

import urllib
import json
import sys
import os


ACCOUNT_KEY = ''
HOST_NAME = ''


#LISTS
HOST_NAMES =[]
HOST_KEYS = []
host_key_log_key_dict = {}
log_names = []
log_keys = []

# List of log names to delete from each and every log set  <<< Double check case and spelling of logs >>>
######### REVISED THIS "delete_log_names" FOR YOUR OWN PURPOSES #########
delete_log_names = ["alternatives.log", "anaconda.log", "auth.log", "btmp", "cups", "daemon.log", "dkpg.log", "user.log", "wtmp", "Xorg.x.log"]



#gets host names
def get_host_name():
    req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + '/hosts/')
    response = json.load(req)
    for hosts in response['list']:
        HOST_KEYS.append(hosts['key'])
        # print "---------------------------------------------------"
        # print hosts['name'] + " has a host key of: " + hosts['key']
        # print hosts['name'] +" ---- " + hosts['key']
        # print "getting log name and key"
    
    print "HOST_KEY length of list: %d" % len(HOST_KEYS)   
    print "------------------------"
    print HOST_KEYS
    print "------------------------"
    print "------------------------"

    get_log_name_and_key()

# This takes the log_key and host_key (a.k.a. log set key) and if the log name in the log set is in the delete_log_names List, 
#  Add the log_key as the key and the host_key as a value in the dictionary.   (log key will be unique so it must be the key in the dict)
def get_log_name_and_key():
    for host in HOST_KEYS:
        req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + '/hosts/' + host + '/')
        response = json.load(req)
        for log in response['list']:
            if log['name'] in delete_log_names:
                #print "Log name: " + log['name']
                log_names.append(log['name'])
                #print "Log key: " + log['key']
                log_keys.append(log['key'])
                host_key_log_key_dict[log['key']] = host 
        

    print len(log_names)
    print "log Names\n----------------------------" 
    print log_names
    print len(log_keys)
    print "log Keys\n----------------------------" 
    print log_keys

    print "host_key_log_key_dict Dictionary "
    
    for log_k,host_v in host_key_log_key_dict.items():
        print log_k + " ----- " + host_v
    remove_log_name()


# this removes the log from the log set permanently using the 'rm_log' request to the api
def remove_log_name():
    for log_k,host_v in host_key_log_key_dict.items():
        request = urllib.urlencode({
            'request':'rm_log', 
            'user_key': ACCOUNT_KEY,
            'host_key': host_v,
            'log_key': log_k
        })
        print "\n =========================================================="
        print "A Log Key of %s within your Host key of %s has been deleted" % (log_k, host_v)
        print "\n\n"

        req = urllib.urlopen("http://api.logentries.com/", request)
        response_log = json.loads(req.read())


if __name__ == '__main__':
    ACCOUNT_KEY = sys.argv[1]
    get_host_name()
