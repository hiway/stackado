# gtdstack.py

# Author: Harshad Sharma
# h@harshadsharma.com
# https://bitbucket.org/hiway/gtdstack/

from languages import trans, is_valid_language
import pickle
import faqmodule

URL = "https://bitbucket.org/hiway/gtdstack/"

HELP_MSG = """
Sorry, but I cannot understand what you said, try asking
a question or use the following commands.

Commands:
a <task> : Add a new task
c : Current task; if you forget what you're working on ;-)
d : Mark current task as done
g <task-number> : Switch to a previously saved task, use task number from list.
l : Display a list of pending tasks

Also, you can visit: %s for more information.
""" %URL

chatbot_text = {
    "hi": "hello! Type in 'help' to get started.",
    "hello": "hey! Send 'help' to get assistance.",
    "hey":"hi! You can send 'help' to know more.",
    "help": HELP_MSG,
    "h": HELP_MSG,
    "?": HELP_MSG,
    "bored":"Hmm... go for a walk, maybe?",
    "website":URL,
    "url":URL,
    "link":URL,   
    }


class Error(Exception):
    """Generic exception raised for errors in GtdStack
    
    Attributes:
        msg -- explanation of the error
    """
    def __init__(self, msg):
        self.msg = msg    

class GTDStack:
    """Accepts a data structure and performs operations on it.
    
    """
    user_data = None
    projects = None
    current_project = None
    language = None
    undo_function = None
    undo_arg = None
    
    def __init__(self, user_data=None):
        """Loads given data structure, or creates one is none specified.
        
        Expected format:
        
            user_data = {
                "projects": {
                    "general": ["task1", "task2"],
                    "project1": ["task1, "task2"],
                    },
            
                "current_project":"general",
                "language":"en",
            }
            
        Note: The 'general' project is treated as special and is not included
        in the list of projects.  Also, we do not allow users to create a
        project with 'general' as its name.
        
        If data does not contain 'projects', raise error.
        If current_project is empty or invalid, revert to using 'general'.  
        If projects:general is empty or invalid, create an empty project.  
        """
        
        if not user_data:
            user_data = {"projects":{}}
        
        # Check if the given data is valid
        
        # Does the data contain a 'projects' dictionary?
        if 'projects' in user_data:
            self.projects = user_data["projects"]
            
        else:
            # Complain, this is definitely corrupt data and
            # we cannot use it.
            raise Error("'projects' dictonary not found in data.")
        
        
        # Do we have a valid current_project?
        if 'current_project' in user_data:
            self.current_project = user_data["current_project"]
            
        else:
            # Silently select a valid current_project
            self.current_project = "general"

        
        # Check if we have a valid 'general' project
        if 'general' not in self.projects:
            # silently ceate a new 'general' project
            self.projects.update({"general":[]})
        
        
        # Check if we have a language defined, else define "en" as default
        if 'language' not in user_data:
            self.language = "en"
        else:
            self.language = user_data["language"]


    def set_undo(self, function, arg):
        """Saves given function as undo function and arguments"""
        self.undo_function = function
        self.undo_arg = pickle.dumps(arg)
        
    
    def undo(self):
        """Uses previously saved data to undo last command"""
        function = self.undo_function
        arg = pickle.loads(self.undo_arg)
        
        try:
            response = function(arg)
            self.undo_arg = None
            self.undo_function = None
            
        except:
            response = trans("cannot undo", self.language)
        
        return response
    

    def set_language(self, language):
        """Sets given locale"""
        if is_valid_language(language):
            
            # what command to run if user asks to UnDo, with its arguments 
            self.set_undo(self.set_language, (language))
            
            self.language = language
            return trans("language set", self.language)
        
        else:
            return trans("language not supported", self.language, (language))


    def set_project(self, project):
        """Sets given project as current_project"""
        
        # Create a new project, if empty, reset to general
        if project not in self.projects:
            if project.strip() != '':
                self.projects.update({project:[]})
            else:
                project = "general"
            
        # save undo information
        self.set_undo(self.set_project, (self.current_project))
        
        self.current_project = project
        return trans("project set", self.language, project)
        
        #return trans("project not found", self.language, project)


    def get_project(self):
        """Returns the current_project"""
        return self.current_project



    def get_project_list(self):
        """Returns list of projects created by user."""
        
        response = u""
        
        for project in self.projects:                
            response = response + u"\n%s" %(project)
            
            # Mark current project
            if project == self.current_project:
                response = response + u" [current]"

            
        return response.strip()



    def get_data(self):
        """Constructs a proper data structure from current state of the object
        and passes it back, use to store the data structure in file/json."""
        
        user_data = {
            "projects": self.projects,
            "current_project": self.current_project,
            "language": self.language,
            }
        
        return user_data


    def get_task(self):
        """Returns current task"""
        try:
            task = self.projects[self.current_project].pop()
            self.projects[self.current_project].append(task)
            return trans("focus on task", self.language, (task))
        except:
            return trans("nothing", self.language)


    def task_add(self, task, project=None, do_later=False):
        """Adds task to project, uses current_project project if not specified.
        
        if do_later == True, task is added below the topmost task in the given
        project.
        
        Expected, a task as unicode string and a project name as unicode
        string.
        """
        
        if task.strip() == "":
            return self.get_task_list()
        
        if not project:
            project = self.current_project
        
        # Just making sure strings are unicode form this point onward
        task = u'%s' %task
        project = u'%s' %project
        
        # Check if the project name is valid
        if project in self.projects:
            
            if do_later:
                temp = self.projects[project].pop()
                self.projects[project].append(task)
                self.projects[project].append(temp)
                return trans("task added for later", self.language, (task))
            
            self.projects[project].append(task)
            return trans("task added", self.language, (task))
            
        else:
            # Create new project
            self.projects.update({project:[]})
            self.projects[project].append(task)
            
            return trans("task added", self.language, (task))


    def get_task_list(self, project=None):
        """Returns a numberd list of tasks (as string) for specified project,
        defaults to current_project if none specified.
        """
        
        if not project:
            project = self.current_project

        
        # Check if project name is valid, else complain.
        if project not in self.projects:
            return trans("project not found", self.language, (project))
        
        # make a copy of the list as we are going to change its order.
        tasklist = self.projects[project][:]
        
        tasklist.reverse()

        # Build the response
        response = u""
        response = '\n'.join([u'%2d. %s' % (len(tasklist)-x, tasklist[len(tasklist)-x-1]) for x in range(len(tasklist))])
        return response



    def get_all_task_lists(self):
        response = u""
        
        for project in self.projects:
            response = response + u"\n\n%s\n==========\n"% (project)
            response = response + u"%s" %(self.get_task_list(project))
            
        return response.strip()
    

    def task_done(self, task_number=None, project=None):
        """Marks the given task_number as done (removes from list)
        If task_number is None, defaults to the last task.
        If project is none, defaults to current_project
        """
        
        if not project:
            project = self.current_project
            
        if project not in self.projects:
            return trans("project not found", self.language, (project))
        
        # check if we have a task_number, if yes, delete the corresponding task
        if task_number:
            # since we're dealing with reversed numbers for tasks (1 being the
            # last task in list, handle it similarly here)
            
            task_count = len(self.projects[project])
            
            # Ensure we pass numbers
            task_number = task_count - int(task_number)
            

            try:
                task = self.projects[project][task_number]
                
                self.set_undo(self.task_add, (task))
                
                del(self.projects[project][task_number])
                
            except:
                return trans("cannot find task number", self.language,
                             (task_number))
                
        else:
            try:
                task = self.projects[project].pop()
            except:
                # project is empty, and everything is done, delete the project
                # don't worry about 'general' project, if deleted, it will
                # be automatically created again
                
                del(self.projects[project])
                
                return "%s\n%s" %(trans("list empty", self.language),
                                  self.set_project("general"))
        
        return trans("task done", self.language, (task, self.get_task()))
    
    
    def task_goto(self, task_number, project=None):
        """Sets given task number as current task.
        Can manually set the project, else defaults to current_project.
        """
        
        if not project:
            project = self.current_project
            
        if project not in self.projects:
            return trans("project not found", self.language, (project))
        
        try:
            # since we're dealing with reversed numbers for tasks (1 being the
            # last task in list, handle it similarly here)
            
            task_count = len(self.projects[project])
            
            # Ensure we pass numbers
            task_number = task_count - int(task_number)
            
            # Remove the task from its current position
            task = self.projects[project][task_number]
            del(self.projects[project][task_number])
            
            # Add the task back at top of the list 
            self.projects[project].append(task)
            
            return trans("focus on task", self.language, (task))
        
        except:
            return trans("cannot find task number", self.language, task_number)
    
    
    def parse_command(self, input_str):
        """A basic command parsing system is implemented right here, simply
        pass text lines and let magic happen!"""
        

        # Since commands are single letter with optional argument, split
        # the input_str on space
        commands = input_str.split(" ")
        
        # Take the first element, this is our command
        # I'm keeping this for later - if our commands get longer than a
        # single letter, nothing has to be changed here
        command = commands[0]
        
        # Join back the words that make up task
        task = " ".join(commands[1:]).strip()
        
        if command == 'a':
            # Issue #13
            # Check for a '#' at end, if found, add task below current task.
            if task[-1] == '#':
                return self.task_add(task[:-1], do_later=True)
            
            return self.task_add(task, do_later=False)
        
        elif command == 'c':
            return self.get_task()
        
        elif command == 'd':
            return self.task_done(task)
        
        elif command == 'p':
            return self.set_project(task)
            
        elif command == 'P':
            return self.get_project_list()
        
        elif command == 'g':
            return self.task_goto(task)

        elif command == 'l':
            return self.get_task_list()
            
        elif command == 'L':
            return self.get_all_task_lists()

        elif command == 'u':
            return self.undo()
        
        else:
            input_str = input_str.lower()
            
            # try basic chatbot (check dictionary at top)
            if input_str in chatbot_text:
                return chatbot_text[input_str]

            # try advanced chatbot
            response = faqmodule.get_response(input_str)
            
            # got something from advanced chatbot
            if response:
                return response
            
            # Can't even chat? Send help message!
            # use the preceeting dot "." to notify application this help message
            # is being sent because everything else has failed.
            return "." + HELP_MSG

        

    
    