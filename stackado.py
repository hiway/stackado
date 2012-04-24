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
import copy

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

    # This list holds previous copies of the stack - useful to undo state
    # change.
    undo_list = []

    # Keeps a list of redo actions - whatever is undone can be redone
    # However, it will be wiped out every time save_undo() is called
    redo_list = []

    # Now add a few functions that make things easier for us to
    # manipulate the stack.
    def add(self, task):
        """Adds a task to stack. Always converts text string to UTF-8."""
        self.save_undo()

        task = task.encode('utf-8')
        self.stack.append(task)

    def done(self):
        """Marks a task as done, and removes it from the stack.
        Returns a UTF-8 object."""
        self.save_undo()

        task = self.stack.pop()
        return task

    def next(self):
        """Returns the topmost task in the stack."""
        self.save_undo()

        task = self.stack[-1]
        return task

    def save_undo(self, reset_redo=True):
        """Saves current state of stack into undo_list.
        Versions of our stack are stored into another stack
        """
        current_state = copy.deepcopy(self.stack)
        self.undo_list.append(current_state)

        if reset_redo is True:
            self.redo_list = []

    def save_redo(self):
        """Saves current state of stack into redo_list."""
        current_state = copy.deepcopy(self.stack)
        self.redo_list.append(current_state)

    def undo(self):
        """Reverses last action, allows user to make mistakes."""
        # Now this is an important function to have in an application
        # where the user is constantly interacting, especially in
        # text format - we all make mistakes and it is painful to
        # be forced to type out everything once again if you
        # accidentally mark a task as done.
        #
        # Since we have the whole state stored in self.undo_list, we
        # simply restore it back!
        try:
            # store current state in redo_list
            self.save_redo()
            # get previous state from undo_list
            self.stack = self.undo_list.pop()
        except:
            raise

    def redo(self):
        """Un-does undo. Gets reset by save_undo()
        A user can call redo only if they are not changing the state
        in between consecutive undo and redo."""
        try:
            # save current state into undo_list
            self.save_undo(reset_redo=False)
            # get state from redo_list
            self.stack = self.redo_list.pop()
        except:
            raise


    def dump_state(self):
        """Returns JSON string of full state of TodoStack object."""
        state = {
            'stack':self.stack,
            'undo_list':self.undo_list,
            'redo_list':self.redo_list,
        }

        return json.dumps(state)


# Also, let us add some code here which will be run whenever this file is
# run via the python command instead of simply importing.
# like: python stackado.py
if __name__ == '__main__':
    # This part is not executed if imported into another python file.

    # Create an instance of TodoStack
    mystack = TodoStack()

    # Add an item into the stack
    mystack.add(u'get a chai')
    mystack.add(u'get a cookie')
    mystack.add(u'blabber a bit')

    print mystack.stack
    print "-"*30

    mystack.undo()
    print mystack.stack
    print "-"*30

    mystack.redo()
    print mystack.stack
    print "-"*30

    print mystack.dump_state()
