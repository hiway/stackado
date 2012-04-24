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
    """Holds and manipulates a stack of TODOs."""
    stack = []  # Stack of TODO items
    undo_list = []  # Stack of previous versions of 'stack'
    redo_list = []  # Stack of undone versions of 'stack'

    def add(self, task):
        """Adds a task to stack."""
        self.save_undo()

        task = task.decode('utf-8')
        self.stack.append(task)

    def done(self):
        """Marks a task as done, and removes it from the stack."""
        self.save_undo()
        try:
            task = self.stack.pop()
            return task.encode('utf-8')
        except:
            return None

    def next(self):
        """Returns the topmost task in the stack."""
        self.save_undo()
        try:
            task = self.stack[-1]
            return task
        except:
            return None

    def save_undo(self, reset_redo=True):
        """Saves current state of stack into undo_list.
        Versions of our stack are stored into another stack.
        Resets redo_list by default.
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
        # Since we have the whole state stored in self.undo_list, we
        # simply restore it back!
        try:
            # store current state in redo_list
            self.save_redo()
            # get previous state from undo_list
            self.stack = self.undo_list.pop()
        except:
            pass

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
            pass


    def dump_state(self):
        """Returns JSON string of full state of TodoStack object."""
        state = {
            'stack':self.stack,
            'undo_list':self.undo_list,
            'redo_list':self.redo_list,
        }

        return json.dumps(state)

    def load_state(self, data):
        """Expects JSON string as saved by dump_state, loads the data into
        object's data structures."""
        state = json.loads(data)

        self.stack = state['stack']
        self.undo_list = state['undo_list']
        self.redo_list = state['redo_list']
