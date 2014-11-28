le_create_log_under_specific_host.py
-------------------
-------------------

# THIS SCRIPT WILL:
# 1. LISTS ALL OF YOUR HOST NAMES FOR A SPECIFIC ACCOUNT_KEY (not in order)
# 2. ALLOWS YOU TO SPECIFY A HOST NAME IN THE COMMAND sys.argv[2] IN WHICH TO CREATE A NEW LOG 
# 3. ALLOWS YOU TO SPECIFY A NEW LOG NAME IN THE COMMAND sys.argv[3]  
# 4. IT CREATES A LOG NAME UNDER THE SPECIFIED HOST NAME


# REQUIREMENT - you must have your Logentries Account_Key and have at least one host in your account.


Usage:
-----

To run the script:

Download it from github and save it in a directory. 

From the Terminal move into that directory and run the following: 

	python le_create_log_under_specific_host.py ACCOUNT_KEY HOST_NAME NEW_LOG_NAME
	Example: python_le_create_log_under_chosen_host.py xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx DataHub new_connection_log

Where ACCOUNT_KEY is the key of your Logentries account

Note:
-----
This Document shows you where to get the ACCOUNT_KEY (https://logentries.com/doc/accountkey/)
