le_disable_specific_tag_by_tagID.py
-------------------
-------------------

THIS SCRIPT WILL:
 1. DIASBLE YOUR TAG / ALERT BY REFERRING TO THE CORRECT TAG / ALERT ID IN LINE 22 OF THIS SCRIPT

 2. TO RETRIEVE YOUR TAG ID YOU CAN FIND IT IN YOUR DEVELOPER CONSOLE OF YOUR BROWSER
    CLICK ON THE ENABLE / DISABLE BUTTON OF TAG - FROM YOUR WEB UI
    AND LOOK UNDER THE NETWORK TAB FOR THE SECOND OCCURRENCE OF 'actions  /api/v2'
 		actions
 		/api/v2
 	The id you need is UNDER 'id":"xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx" at the beginning of this JSON object
 
3.  COPY AND PASTE THIS ID INTO YOUR CODE ON LINE 22 INSIDE THE QUOTATION MARKS.

REQUIREMENT(S) - You must have your Logentries Account_Key and have the Tag Alert ID inserted in your script on line 22 as shown below
line 22 - if action['type'] != 'tagit' and action['id'] == 'YOUR_TAG_ALERT_ID_GOES_HERE':


Usage:
-----

To run the script:

Download it from github and save it in a directory. 

From the Terminal move into that directory and run the following: 

	python le_disable_specific_tag_by_tagID.py ACCOUNT_KEY

Where ACCOUNT_KEY is the key of your account

If checking your Tags / Alerts from your Web UI you may need to reload your web page of your browser.

Note:
-----
This Document shows you where to get the ACCOUNT_KEY (https://logentries.com/doc/accountkey/)
