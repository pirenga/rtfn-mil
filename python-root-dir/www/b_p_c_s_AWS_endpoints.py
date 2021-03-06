#!/usr/bin/env python
'''
 * FILENAME: b_p_c_s_AWS_endpoints.py
 * PURPOSE: Allow the use of python virtual environment through a webserver call. 
            Provide AWS endpoints through Level3/CenturyLink.
 * AUTHORS: Mr. David J. Stern
 * DATE: DEC 2017
 * AGENCY: Defense Information Systems Agency
 * DEPARTMENT: Defense
 * GOVERNMENT: United States
 * THIS WORK IS IN THE PUBLIC DOMAIN. See relevant license information for its
   intended use. 
 * This work is solely a Government work product and no contractors participated
   in its creation.
'''
# this activates the python virtual environment
activate_env="/home/id22/.virtualenvs/ydk-py/bin/activate_this.py"
execfile(activate_env, dict(__file__=activate_env))
import sys
# this sets the python path for execution
sys.path.insert(0,"/home/id22/Desktop/ydk-py-master/core/samples")
import Calls2Level3 as L3_io
import json

print ("Content-Type: application/json\r\nAccess-Control-Allow-Origin: *\r\n"+
"Access-Control-Allow-Credentials: true\r\nAccess-Control-Allow-Methods:*\r\n"+
"Access-Control-Allow-Headers:*\r\nAccess-Control-Expose-Headers\r\n")
# note: account numbers have been removed. Replace the 0 with your account 
# number. We've also anonymized the account number 
# TODO: clean up anonymizing account numbers for carrier/endpoint scale.

#get the Base Post Camp Staton AWS endpoints 
print (L3_io.queryUnisByAccountJSON(0,"").replace('{"billingAccountNumber":"0"}','{"billingAccountNumber":"1"}'))   #for Level3 v1.2 use "" or "2.0"
