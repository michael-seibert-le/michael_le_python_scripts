import urllib2
import urllib
import json
import sys

ACCOUNT_KEY = ''

def get_hosts():
    url = 'https://api.logentries.com/' + ACCOUNT_KEY + '/hosts/'
    response = urllib2.urlopen(url).read()
    hosts = json.loads(response)
    print 'Getting Host names and keys'
    for host in hosts['list']:
        host_name = urllib.quote_plus(host['name'])
        host_key = host['key']

        print host_name + " --- " + host_key
        if host_name=="DemoHost":
            print "*** DEMO HOST **** " + host_name + " --- " + host_key
            print "------------------------------------------------------"

            request = urllib.urlencode({
            'request':'rm_host',
            'user_key': ACCOUNT_KEY,
            'host_key': host_key
            })

            req = urllib.urlopen("http://api.logentries.com/", request)
            response_dict = json.loads(req.read())
            print "Host with DemoHost Host name has been deleted"
    print "------------------"
    print "SCRIPT COMPLETED"
           

if __name__ == '__main__':
    ACCOUNT_KEY = sys.argv[1]
    print "ACCOUNT_KEY = " + ACCOUNT_KEY
    # try:
    #     TAGS = sys.argv[2:]
    # except NameError:
    #     TAGS = []
    get_hosts()
