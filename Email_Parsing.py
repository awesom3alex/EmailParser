#!/usr/bin/env python
#
# Extracts email addresses from one or more plain text files.
#
# Notes:
# - Does not save to file (pipe the output to a file if you want it saved).
# - Does not check for duplicates (which can easily be done in the terminal).
# - Does not save to file (pipe the output to a file if you want it saved).
# TWITTER = Awesom3_Alex 


from optparse import OptionParser
import os.path
import re
#import resource
#resource.setrlimit(resource.RLIMIT_AS, (megs * 1048576L, -1L))

regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_" "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|" "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

def file_to_str(filename):
    """Returns the contents of filename as a string."""
    with open(filename) as f: #Added encoding='utf-8'
        return f.read().lower() # Case is lowered to prevent regex mismatches.

def get_emails(s):
    """Returns an iterator of matched emails found in string s."""
    # Removing lines that start with '//' because the regular expression
    # mistakenly matches patterns like 'http://foo@bar.com' as '//foo@bar.com'.
    return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))

def linefrom_file(filename):
    with open(filename) as f:
        for line in f:
            yield line

import os
not_parseble_files = ['.txt', '.csv']
for root, dirs, files in os.walk('.'):#This recursively searches all sub directories for files
    for file in files:
        _,file_ext = os.path.splitext(file)#Here we get the extension of the file
        file_path = os.path.join(root,file)
        # if file_ext in not_parseble_files:#We make sure the extension is not in the banned list 'not_parseble_files'
          # print("File %s is not parseble"%file_path)
          # continue #This one continues the loop to the next file
        if os.path.isfile(file_path):
            for line in linefrom_file(file_path):
                for email in get_emails(line):
                    print(email)