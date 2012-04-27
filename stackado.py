"""
    Stackado
===============================================================================

    Stack-a-do, a task management system that lets you get distracted or dig
    deeper into the task at hand and come back to whatever you were doing.
    From as many levels deep as you choose to go.

    This module exposes an API that we can use to write command-line app,
    chat-bots or even email or sms-based applications to manipulate our
    todo-stack.

"""
import re
import json
import copy


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
        return 'DO: %s' % (task)

    def done(self, task=None):
        """Marks a task as done, and removes it from the stack."""
        if task is None:
            try:
                self.save_undo()
                self.stack.pop()
                task = self.current()
                return 'DO: %s' % (task)
            except IndexError:
                raise IndexError('There are no tasks to mark done!')
        else:
            # Here, we simply use previously created code that does the job
            # make the given task as current, and mark as done.
            output = self.current(task)
            return self.done()

    def current(self, task=None):
        """Returns the topmost task in the stack."""
        if task is None:
            try:
                task = self.stack[-1]
                return task
            except:
                return 'Nothing more to do!'
        else:
            self.save_undo()
            try:
                task = self.stack[-int(task)]
                self.stack.remove(task)
                self.stack.append(task)
                return task
            except IndexError:
                raise IndexError('Task (%s) could not be found.' % (task))

    def list(self):
        """Returns a list of all pending tasks."""
        nlist = []
        x = len(self.stack)
        for task in self.stack:
            nlist.append("%d. %s" % (x, task))
            x -= 1

        return '\n'.join(nlist)

    def save_undo(self, reset_redo=True):
        """Saves current state of stack into undo_list.
        Versions of our stack are stored into another stack.
        Resets redo_list by default.
        """
        current_state = copy.deepcopy(self.stack)
        self.undo_list.append(current_state)

        # save limited undo steps
        if len(self.undo_list) > 10:
            self.undo_list.remove(self.undo_list[0])

        if reset_redo is True:
            self.redo_list = []

    def save_redo(self):
        """Saves current state of stack into redo_list."""
        current_state = copy.deepcopy(self.stack)
        self.redo_list.append(current_state)

    def undo(self, x=1):
        """Reverses last action, allows user to make mistakes."""
        x = int(x)

        if x > len(self.undo_list):
            return 'Can undo %s times!' % len(self.undo_list)

        while x:
            try:
                # store current state in redo_list
                self.save_redo()
                # get previous state from undo_list
                self.stack = self.undo_list.pop()
            except:
                pass
            x -= 1

        return 'OK'

    def redo(self, x=1):
        """Un-does undo. Gets reset by save_undo()
        A user can call redo only if they are not changing the state
        in between consecutive undo and redo."""
        x = int(x)

        if x > len(self.redo_list):
            return 'Can redo %s times!' % len(self.redo_list)

        while x:
            try:
                # save current state into undo_list
                self.save_undo(reset_redo=False)
                # get state from redo_list
                self.stack = self.redo_list.pop()
            except:
                pass
            x -= 1

        return 'OK'

    def dump_state(self):
        """Returns JSON string of full state of TodoStack object."""
        state = {
            'stack': self.stack,
            'undo_list': self.undo_list,
            'redo_list': self.redo_list,
        }

        return json.dumps(state)

    def load_state(self, data):
        """Expects JSON string as saved by dump_state, loads the data into
        object's data structures."""
        state = json.loads(data)

        self.stack = state['stack']
        self.undo_list = state['undo_list']
        self.redo_list = state['redo_list']

    def parse_command(self, line):
        """Expects a string, parses commands and executes actions
        and returns results."""
        cmdmap = (
            ('^a (?P<task>(.*))$', self.add),
            ('^d$', self.done),
            ('^d (?P<task>(\d+))$', self.done),
            ('^c$', self.current),
            ('^c (?P<task>(\d+))$', self.current),
            ('^l$', self.list),
            ('^ls$', self.list),
            ('^undo$', self.undo),
            ('^undo (?P<x>(\d+))$', self.undo),
            ('^redo$', self.redo),
            ('^redo (?P<x>(\d+))$', self.redo),
        )

        for cmd in cmdmap:
            regex = cmd[0]
            func = cmd[1]

            cregex = re.compile(regex)
            line = line.lower().strip()

            r = cregex.match(line)
            if r is not None:
                kwargs = r.groupdict()
                return func(**kwargs)

        return None
