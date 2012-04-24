#!/usr/bin/env python

# importing readling makes raw_input behave better
# refer: http://docs.python.org/library/functions.html#raw_input
import readline
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
        output = stack.parse_command(line)
        if output is not None:
            print output

        # Save state
        open(filename, 'w+').write(stack.dump_state())

    else:
        carry_on = False
