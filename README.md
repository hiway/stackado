stackado
========

TODO manager that uses stacks to let you dive deep into a debugging task and
come back to previous tasks wherever you left them. Mighty useful if you are
into [yak shaving](http://www.hanselman.com/blog/YakShavingDefinedIllGetThatDoneAsSoonAsIShaveThisYak.aspx).

## Usage:

### Running on your own machine, locally:

    python todo.py

### Commands

#### Add a task

    Type a task and hit enter, if it does not match any of the commands - 
    it is automatically considered as a new task. Or if you want to keep a
    consistent command pattern - type `a` followed by task and hit enter.
    
    a <task>

#### Show current task
    <enter> without any keys typed at the prompt.

#### Mark a task as done
    d

#### Check next task
    n

#### List of all pending tasks
    l

#### Undo last action
    undo

#### Redo last undo
    redo

