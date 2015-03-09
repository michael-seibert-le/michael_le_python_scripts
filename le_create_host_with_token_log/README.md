le_create_host_with_token_log.py
-------------------
-------------------

 THIS SCRIPT WILL:
 1. CREATE A NEW HOST OF YOUR NAME WITH AN ALTERNATIVE HOST NAME OF YOUR CHOICE
 2. IT WILL THEN CREATE A TOKEN-BASED LOG, WHICH YOU WILL ALSO NAME IN THE COMMAND LINE UTILITY
 

REQUIREMENT(S) - YOU MUST HAVE YOUR LOGENTRIES ACCOUNT_KEY.  YOU MUST INPUT 4 ARGUMENTS INTO THE CLI WHEN RUNNING THIS SCRIPT.
THESE 4 ARGUMENTS IN ORDER ARE:
1.  YOUR LOGENTRIES' ACCOUNT_KEY.
2.  A HOST NAME
3.  AN ALTERNATIVE HOST NAME 
4.  A NAME FOR YOUR TOKEN-BASED LOG


Usage:
-----

To run the script:

Download it from github and save it in a directory. 

From the Terminal move into that directory and run the following: 

	python le_create_host_with_token_log.py ACCOUNT_KEY HOST_NAME ALT_HOST_NAME LOG_NAME

Where ACCOUNT_KEY is the key of your Logentries account

EXAMPLE:
    python le_create_host_with_token_log.py xxxxxxxx-xxxxx-xxxxx-xxxx-xxxxxxxxxxxx "A_New_Host" "A_new_Host_Alt" "My_new_log_name"


Note:
-----
This Document shows you where to get the ACCOUNT_KEY (https://logentries.com/doc/accountkey/)

