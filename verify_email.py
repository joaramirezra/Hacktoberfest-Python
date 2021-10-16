"""
This script contains a helper function that uses regex to check 
if a given string input has a valid email format.


Author: <Curiouspaul1>
Email: paulcurious7@gmail.com
"""

import re

def check_email(email: str):
    emailreg = re.compile(r'''
        # username
        ([a-zA-Z0-9_\-+%]+|[a-zA-Z0-9\-_%+]+(.\.))
        # @ symbol
        [@]
        # domain name
        [a-zA-Z0-9.-]+
        # dot_something
		[\.]
        ([a-zA-Z]{2,4})
    ''',re.VERBOSE)
    try:
        if emailreg.search(email):
            return True
        else:
            return False
    except AttributeError:
        raise False

