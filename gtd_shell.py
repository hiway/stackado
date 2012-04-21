#!/usr/bin/env python

# Command line interface to gtdstack.py

from gtdstack import GTDStack
import pickle

# set up variables
filename = "autosaved.gtd"
data = None
loop = True

# try to load autosaved file
try:
    infile = open(filename, "r+")
    data = pickle.load(infile)
    infile.close()
except:
    pass

# Initialize the object
s = GTDStack(data)


while loop:
    
    # get user's command
    input_str = raw_input("> ")
    
    # check if user wants to quit, else continue
    if not input_str == "q":
        
        # this is all we have to do to make the gtdstack work
        # for us ;)
        print s.parse_command(input_str)
        
        # autosave after every command
        outfile = open(filename,"w+")
        pickle.dump(s.get_data(), outfile)
        outfile.close()
        
    else:
        # bye bye
        loop = False

print "Bye!"