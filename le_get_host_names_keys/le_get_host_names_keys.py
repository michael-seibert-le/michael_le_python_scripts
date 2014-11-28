# coding: utf-8
#!/usr/bin/python


# THIS SCRIPT LIST ALL HOST NAMES and HOST KEYS FROM AN ACCOUNT_KEY

import urllib
import json
import sys
import os

ACCOUNT_KEY = ''

def get_host_name():
    req = urllib.urlopen("http://api.logentries.com/" + ACCOUNT_KEY + '/hosts/')
    response = json.load(req)
    for host in response['list']:
        print host['name'] + " -- " + host['key']
            
if __name__ == '__main__':
    ACCOUNT_KEY = sys.argv[1]
    get_host_name()

