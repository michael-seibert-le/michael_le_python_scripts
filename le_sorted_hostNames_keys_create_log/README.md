le_sorted_hostNames_keys_create_log.py
-------------------
-------------------

THIS SCRIPT WILL:
 1. LISTS ALL OF YOUR HOST NAMES & HOST KEYS FOR AN ACCOUNT (Host Names are in alphabetical order)
 2. UNDERNEATH EACH HOST, THE LOGS FOR THAT HOST WILL BE LISTED (In no order)
    LOG DETAILS INCLUDE: TOKEN-BASED OR AGENT-BASED, LOG NAME, LOG TOKEN AND LOGKEY
 3. IT WILL PROMPT YOU TO PICK A NUMBER ASSIGNED TO EACH HOST TO CREATE A LOG UNDER THIS HOST NAME 
 4. IT THEN PROMPTS YOU FOR A NEW LOG NAME
 5. IT CREATES A LOG NAME UNDER YOUR SELECTED HOST AND CONFIRMS IT.

REQUIREMENT(S) - You must have your Logentries Account_Key and have at least one host in your account.

Usage:
-----

To run the script:

Download it from github and save it in a directory. 

From the Terminal move into that directory and run the following: 

	python le_sorted_hostNames_keys_create_log.py ACCOUNT_KEY

Where ACCOUNT_KEY is the key of your account

Note:
-----
This Document shows you where to get the ACCOUNT_KEY (https://logentries.com/doc/accountkey/)
