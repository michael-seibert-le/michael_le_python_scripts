le_remove_all_hosts_but_DataHub.py
-------------------
-------------------

THIS SCRIPT WILL:
 1. REMOVE ALL HOSTS AND LOGS FROM YOUR ACCOUNT EXCEPT THE ONE SPECIFICALLY LABELLED "DataHub" (case sensitive).
 2. THIS WILL ESSENTIALLY WIPE ALL HOST AND LOG DATA FROM YOUR GIVEN ACCOUNT EXCEPT "DataHub".
 
 THIS CANNOT BE UNDONE OR REVERSED!
 
IF YOU HAVE A DATAHUB INSTANCE THAT FILTERS IT'S LOGS ANYWHERE OUTSIDE OF THE "DataHub" HOST, DO NOT USE THIS AS YOUR CONNECTIONS WILL NO LONGER HAVE ANY LOGS TO FILTER LOG EVENTS INTO.

REQUIREMENT(S) - you must have your Logentries Account_Key and have at least one host in your account.


Usage:
-----

To run the script:

Download it from github and save it in a directory. 

From the Terminal navigate into that directory and run the following: 

	python le_remove_all_hosts_but_DataHub.py ACCOUNT_KEY 
	Example: python le_remove_all_hosts_but_DataHub.py xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 

Where ACCOUNT_KEY is the Account key of your specific Logentries account

Note:
-----
This Document shows you where to get the ACCOUNT_KEY (https://logentries.com/doc/accountkey/)

IMPORTANT:
-----
Once this script is run, all data for your account will be deleted except for your "DataHub" (case sensitive) Host, essentially clearing all Host and Logs from your account.
IT CANNOT BE REVERTED OR UNDONE 
-----
SO ONLY USE THIS SCRIPT ONLY IF YOU WISH TO COMPLETELY CLEAR YOUR ACCOUNT OF ALL DATA EXCEPT YOUR HOST NAMED "DataHub"! (case sensitive).