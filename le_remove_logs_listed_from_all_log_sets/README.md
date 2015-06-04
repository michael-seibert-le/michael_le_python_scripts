le_remove_logs_listed_from_all_log_sets.py
-------------------
-------------------

THIS SCRIPT WILL:
 1. Takes a python List of "Delete_log_names" and delete these logs from each an every Log Set in your Logentries Account.
 2. It checks the name of the item in "delete_log_names" List against the log names in each Log Set of your account.
    If the log name matches the item in the delete list, it will be deleted.  
    This script will remove each specific log from ALL Log Sets in your Account.

  This will not prompt you at any stage, so know what this script does by reading it before you use it.

REQUIREMENT(S) - You must have your Logentries Account_Key 

BE SURE TO CHECK THIS SCRIPT WILL WORK FOR YOU SMALL SCALE BEFORE IMPLEMENTING IT ON A LARGE SCALE!

ALSO
DOUBLE CHECK & ALTER
    The 'delete_log_names' list inside this script.
    to be sure your list matches (case and letters, .log and otherwise) precisely the log names you wish to delete permanently.

ONCE DELETED, A LOG AND ITS CONTENTS CANNOT BE RECOVERED, SO USE THIS SCRIPT ONLY IF YOU KNOW WHAT YOUR ARE DOING AND WHAT IT IS DOING.


Usage:
-----

To run the script:

Download it from github and save it in a directory. 

From the Terminal move into that directory and run the following: 

	python le_remove_logs_listed_from_all_log_sets.py ACCOUNT_KEY

Where ACCOUNT_KEY is the key of your Logentries account

Note:
-----
This Document shows you where to get the ACCOUNT_KEY (https://logentries.com/doc/accountkey/)
