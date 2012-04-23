"""
    Stackado
================================================================================

    Stack-a-do, a task management system that lets you get distracted or dig
    deeper into the task at hand and come back to whatever you were doing.
    From as many levels deep as you choose to go.

    This module exposes an API that we can use to write command-line app,
    chat-bots or even email or sms-based applications to manipulate our
    todo-stack.

"""

# We'll be using json to save user's data into files for persistent memory.
import json

# Let us define a class to hold the data and manipulate it. Having a class
# allows us to create one instance of the object and hold it in memory
# without re-loading the data over and over again - useful in apps that
# work on desktop. Web-applications will need to create an instance for
# every request since the state is always new for every request.

class TodoStack:
    """Holds a stack of TODOs."""
    # Use a list to store the stack, simply because lists in Python have
    # all the functions necessary for implementing stacks built into them.
    # Also because lists maintain their order of elements, which is
    # important for our application.
    stack = []

    # Now add a few functions that make things easier for us to
    # manipulate the stack.
    def add(self, task):
        """Adds a task to stack. Always converts text string to UTF-8."""
        # Create a unicode object from the text string (or utf object)
        task = task.encode('utf-8')
        # Save into the stack
        self.stack.append(task)

    def done(self):
        """Marks a task as done, and removes it from the stack.
        Returns a UTF-8 object."""
        # Temporarily store the task
        task = self.stack.pop()
        # Return it to the calling function
        return task



# Also, let us add some code here which will be run whenever this file is
# run via the python command instead of simply importing.
# like: python stackado.py
if __name__ == '__main__':
    # This part is not executed if imported into another python file.

    # Create an instance of TodoStack
    mystack = TodoStack()

    # Add an item into the stack
    mystack.add(u'this is a tad bit better')

    # That little u in front of the string tells Python that we are dealing
    # with Unicode strings - they let us handle all languages and characters.
    # http://eric.themoritzfamily.com/python-encodings-and-unicode.html

    # Check if that actually worked
    print mystack.stack

    # Remove the item
    item = mystack.done()

    # Popping a stack returns the topmost item
    print item
