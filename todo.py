#!/usr/bin/env python

# importing readling makes raw_input behave better
# refer: http://docs.python.org/library/functions.html#raw_input

import readline  # NOQA
import stackado

stack = stackado.TodoStack()
filename = 'autosave.json'

try:
    # Try to load data from disk
    data = open(filename, 'r+').read()
    stack.load_state(data)
except:
    # Unable to load data, ignore
    pass

carry_on = True
while carry_on is True:
    line = raw_input("> ")
    if line != 'q':
        try:
            output = stack.parse_command(line)
        except Exception, e:
            output = e

        if output is not None:
            print output
        else:
            print "Did not understand the command!"

        # Save state
        open(filename, 'w+').write(stack.dump_state())

    else:
        carry_on = False
