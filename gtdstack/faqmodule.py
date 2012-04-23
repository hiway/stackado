
import re     


# TO DO:  Improve normalization, by eliminating apostrophes, punctuation, etc.
def normalize(textin):
    return textin.lower()


kb = [('how do i use this gtdstack bot',
  "When working on something, if you have to do something else first, type 'a' followed by task description, when done 'd' to mark it as done. Type 'l' (L) to see a list of all tasks."),
 ('how to add create a task',
  "To add a task type in 'a' followed by task description. Example: 'a get a cup of coffee'."),
 ('low priority task below current',
  'You can add a "I\'ll do that after I\'m done with current" by putting a \'#\' at the end. Example: \'a take a vacation#\''),
 ('how to delete remove finish done a task',
  "Send 'd' to mark current task as finished. Press 'l' to get a list of all tasks, and then send 'd <task-number>' where task-number is the number next to the task you want to mark as done."),
 ('how to get a list of all tasks and projects',
  "Send 'L' (uppercase L) to list all tasks across all projects."),
 ('how to find search a task', 'Search is not currently implemented, sorry!'),
 ('how to see current task', "Send 'c' to display the current task"),
 ('how can i get an email of all tasks and projects',
  "Just type 'email' and send to me, I'll email to your chat ID."),
 ('how to email to another address',
  "I can't send email to any address other than your chat ID."),
 ('how to change switch make create a project',
  "Send 'p <project-name>' to create a project, same to switch to a project. Send 'p' to go back to general task list."),
 ('how to get see a list of all projects',
  'Send uppercase P to see all projects'),
 ('why do you have lowercase small and uppercase capital commands it is confusing',
  "The case sensitive commands are meant for better efficiency, you don't have to remember another command. 'l' for list of topics in current project. 'L' for list of topics in all projects."),
 ('how can i skip a task and do it later',
  "Send 'g <task-number>', pick task-number from the list of tasks. 'g 2' is a shortcut to going to whatever you were supposed to do next."),
 ('how can i select a task to do first now',
  "Check the task's number by listing all tasks and then send 'g <task-number>' to go-to that task and do it first."),
 ('what is task-number task number',
  "When you list all tasks, you'll see numbers next to the tasks, use these numbers as shortcuts in commands."),
 ('how to list tasks for current project',
  "Send lowercase L 'l' to list all tasks."),
 ('is it possible to get a print out of all tasks and projects',
  "You can send yourself an email (command: 'email' ) and print it out."),
 ('can I send you an email with all my tasks',
  'I cannot receive emails at this moment, but it should be implemented soon.'),
 ('where can i complain suggest report bug feature request',
  'Head over to: http://goo.gl/7JSpN and see if it has been reported already, if not, Create new report!'),
 ('why should i use you bot gtdstack',
  "If like my creator, you 'live in the moment' and have a wild trail behind your train of thought, you should use me."),
 ('give me a brief introduction about yourself',
  "Hi, I'm a system for managing tasks while dealing with distractions, my creator has non-creatively named me gtdstack, but you can call me whatever you want!"),
 ('i will am going to call you', 'Sure!'),
 ('i name you ', 'Okay!'),
 ('how can my friend add use you too',
  "Add 'gtdstack@appspot.com' to Gtalk or Jabber contacts (or send Invite) and start chatting!"),
 ('how can i remember to use you bot gtdstack',
  "Now that's a difficult one! I guess you just need some motivation and discipline for that! :-P"),
 ('are you available on msn aol facebook',
  "No, I'm currently only chatting on Gtalk and other Jabber compliant networks."),
 ('what is jabber',
  'Jabber is what Gtalk is based on - an open and secure technology for instant messaging.'),
 ('how can I get create make jabber id',
  'Head over to: http://www.jabber.org/'),
 ('how can i un do undo a command',
  "Undo is in testing, but you can try sending 'u' if you make a mistake. Most commands can be un done, not all. And it doesn't work sometimes."),
 ('how can i move a task from one project to another', 'Not implemented yet!'),
 ('i need a break',
  "Send 'a take a break', log out and do something else! Never tire yourself out :-) I'm right here whenever you want to get back to work."),
 ('i need a coffee',
  'I wish I could help you with that, but please, take a break and go get a walk and a coffee.'),
 ('i am sleepy', 'Add that to the stack and go take a nap!'),
 ("i cannot can't", ':-('),
 ('yeah yes ya yup', 'okay'),
 ('what do you mean', 'hmm... try rephrasing your original question, please?'),
 ("i didn't do not don't understand",
  'If you think I can be improved in some way, please report that here: http://goo.gl/7JSpN . Thanks in advance!'),
 ('how to change order reorder rearrange priority of tasks',
  "That's not possible right now, but someday it should be. "),
 ('i need help',
  "Try asking a specific question, I'll do my best to answer :-)"),
 ('Where is your tutorial guide manual',
  'you can read through the tutorial on web: https://bitbucket.org/hiway/gtdstack/wiki/tutorial'),
 ('Are you open source',
  "Yes, I'm open source and available here... https://bitbucket.org/hiway/gtdstack/src"),
 ('Are you on twitter',
  "Yes, follow me at @gtdstack , I don't chat there as of now, but might start soon."),
 ('Are you on facebook', 'No I am not on facebook.'),
 ('who made you your creator',
  'Harshad Sharma created me. He can be found at http://harshadsharma.com/'),
 ('how to take backup of my tasks list',
  "You can send yourself an email. Try the command: 'email'")]

vocab = {'about': [20],
 'add': [1, 23],
 'address': [8],
 'all': [4, 7, 10, 16, 17],
 'am': [21, 32],
 'an': [7, 17],
 'another': [8, 29],
 'aol': [25],
 'available': [25],
 'backup': [44],
 'below': [2],
 'bot': [0, 19, 24],
 'break': [30],
 'brief': [20],
 'bug': [18],
 'call': [21],
 "can't": [33],
 'cannot': [33],
 'capital': [11],
 'change': [9, 37],
 'coffee': [31],
 'command': [28],
 'commands': [11],
 'complain': [18],
 'confusing': [11],
 'create': [1, 9, 27],
 'creator': [43],
 'current': [2, 6, 15],
 'delete': [3],
 "didn't": [36],
 "don't": [36],
 'done': [3],
 'email': [7, 8, 17],
 'facebook': [25, 42],
 'feature': [18],
 'find': [5],
 'finish': [3],
 'first': [13],
 'friend': [23],
 'from': [29],
 'give': [20],
 'going': [21],
 'gtdstack': [0, 19, 24],
 'guide': [39],
 'help': [38],
 'how': [0,
         1,
         3,
         4,
         5,
         6,
         7,
         8,
         9,
         10,
         12,
         13,
         15,
         23,
         24,
         27,
         28,
         29,
         37,
         44],
 'id': [27],
 'introduction': [20],
 'jabber': [26, 27],
 'later': [12],
 'list': [4, 10, 15, 44],
 'low': [2],
 'lowercase': [11],
 'made': [43],
 'make': [9, 27],
 'manual': [39],
 'me': [20],
 'mean': [35],
 'move': [29],
 'msn': [25],
 'my': [17, 23, 44],
 'name': [22],
 'need': [30, 31, 38],
 'not': [36],
 'now': [13],
 'number': [14],
 'one': [29],
 'open': [40],
 'order': [37],
 'possible': [16],
 'print': [16],
 'priority': [2, 37],
 'project': [9, 15, 29],
 'projects': [4, 7, 10, 16],
 'rearrange': [37],
 'remember': [24],
 'remove': [3],
 'reorder': [37],
 'report': [18],
 'request': [18],
 'search': [5],
 'see': [6, 10],
 'select': [13],
 'send': [17],
 'should': [19],
 'skip': [12],
 'sleepy': [32],
 'small': [11],
 'source': [40],
 'suggest': [18],
 'switch': [9],
 'take': [44],
 'task': [1, 2, 3, 5, 6, 12, 13, 14, 29],
 'task-number': [14],
 'tasks': [4, 7, 15, 16, 17, 37, 44],
 'too': [23],
 'tutorial': [39],
 'twitter': [41],
 'un': [28],
 'understand': [36],
 'undo': [28],
 'uppercase': [11],
 'use': [0, 19, 23, 24],
 'what': [14, 26, 35],
 'where': [18, 39],
 'who': [43],
 'why': [11, 19],
 'will': [21],
 'ya': [34],
 'yeah': [34],
 'yes': [34],
 'you': [11, 17, 19, 21, 22, 23, 24, 25, 35, 40, 41, 42, 43],
 'your': [39, 43],
 'yourself': [20],
 'yup': [34]}

synvocab = {'take_out': [3], 'represent': [32, 21], 'all': [16, 17, 10, 4, 7], 'admirer': [23], 'consider': [10, 44, 6], 'founder': [20, 30], 'one_and_only': [29], 'skip': [12], 'low-spirited': [2], 'find_oneself': [5], 'call_off': [21], 'soften': [30], 'commute': [9, 37], 'skim': [12], 'abject': [2], 'go': [29, 30, 21], 'follow': [32, 21], 'research': [5], 'minuscule': [11], 'obnubilate': [11], 'empathize': [36], 'gaolbreak': [30], 'regularize': [37], 'lean': [44, 10, 4, 15], 'later': [12], 'violate': [30], 'hunting': [5], 'open_up': [40], 'paint_a_picture': [18], 'attention_deficit_disorder': [1, 23], 'electrical_switch': [9], 'send': [17], 'former': [12], 'charge': [17], 'behave': [3], 'indicate': [18], 'swap': [9], 'come_apart': [30], 'presentation': [20], 'news_report': [18], 'fill-in': [44], 'pull_in': [27, 9, 43], 'chip_in': [20], 'song': [21], 'let_on': [30], 'lowercase': [11], 'take_in': [6, 9, 10, 43, 44, 27], 'starting_time': [13], 'written_report': [18], 'print': [16], 'chirrup': [41], 'candid': [40], 'decamp': [12], 'govern': [37], 'microbe': [18], 'affect': [29], 'margin_call': [21], 'grant': [20], 'encounter': [10, 5, 6], 'look': [10, 5, 6], 'break_of_serve': [30], 'down_in_the_mouth': [2], 'dampen': [30], 'uncovering': [5], 'die': [21, 30], 'give_out': [21, 30], 'snuff_it': [21], 'blue-ribbon': [13], 'electronic_mail': [8, 17, 7], 'leave': [20, 21], 'bequeath': [21], 'world-class': [13], 'atomic_number_95': [32, 21], 'feature_of_speech': [18], 'United_Nations': [28], 'small': [2, 11], 'inclination': [44, 10, 4, 15], 'necessitate': [44, 38, 30, 31], 'break_down': [21, 30], 'ane': [29], 'regain': [5], 'abbreviated': [20], 'cap': [11], 'nigh': [20], 'maneuver': [39], 'use_up': [44], 'ready': [27, 9, 43], 'Holy_Order': [37], 'discover': [10, 22, 6, 5, 30], 'jump': [12], 'Sir_David_Low': [2], 'imply': [35], 'reorder': [37], 'design': [4, 7, 9, 10, 15, 16, 29], 'spread_out': [40], 'pass': [20, 21, 39], 'protrude': [4, 7, 9, 10, 15, 16, 29], 'first_appearance': [20], 'append': [1, 23], 'shout_out': [21], 'blue': [2], 'employ': [0, 24, 19, 23], 'recollect': [24], 'rate': [37], 'birdcall': [21], 'assistance': [38], 'stool': [27, 9, 43], 'brief': [20], 'find': [10, 5, 6], 'current': [2, 6, 15], 'cave_in': [20, 30], 'undecided': [40], 'capital': [11], 'fall_in': [20, 30], 'numeral': [14], 'Call': [21], 'netmail': [8, 17, 7], 'amplitude_modulation': [32, 21], 'stopping_point': [3], 'feature_article': [18], 'movement': [29], 'afterward': [12], 'some_other': [8, 29], 'exchange': [9, 37], 'ulterior': [12], 'leaning': [44, 10, 4, 15], 'modify': [9, 37], 'springiness': [20], 'explore': [5], 'intercept': [18], 'will': [21], 'address': [8, 21], 'rescript': [37], 'interpret': [10, 36, 6], 'handle': [8], 'rules_of_order': [37], 'great': [11], 'engage': [44], 'MA': [32, 21], 'boast': [18], 'get_a_line': [10, 6], 'receive': [5], 'shift': [9, 37, 30], 'study': [18, 44], 'intromission': [20], 'bot': [0, 24, 19], 'bestow': [1, 23], 'experience': [10, 6], 'leaving': [21], 'subscribe_to': [44], 'amount': [14], 'kvetch': [18], 'summate': [1, 23], 'personify': [32, 21], 'permutation': [9], 'guide_on': [39], 'chapiter': [11], 'to_a_lower_place': [2], 'stand-in': [44], 'Maine': [20], 'vociferation': [21], 'point': [39], 'give-up_the_ghost': [21], 'infract': [30], 'projection': [4, 7, 9, 10, 15, 16, 29], 'search': [5], 'manage': [3], 'jailbreak': [30], 'at_a_lower_place': [2], 'exercise': [0, 19, 3, 24, 23], 'utilisation': [0, 24, 19, 23], 'glitch': [18], 'electric_switch': [9], '1st': [13], 'open_frame': [30], 'apply': [0, 24, 19, 20, 23], 'total': [1, 14, 23], 'establish': [27, 9, 43, 20], 'manoeuver': [39], 'select': [44, 13], 'ordinate': [37], 'plow': [8], 'make_believe': [27, 9, 43], 'crap': [27, 9, 43], 'proceed': [29, 21], 'manual_of_arms': [39], 'ease_up': [20], 'motivate': [29], 'visit': [10, 21, 6], 'arrive_at': [27, 9, 43], 'germ': [40, 18], 'Pine_Tree_State': [20], 'live': [32, 21], 'manoeuvre': [39], 'call': [8, 21, 22], 'backup_man': [44], 'turn_over': [20], 'strike': [44, 29], 'survive': [21], 'coiffure': [3], 'tell': [37], 'today': [13], 'phone': [21], 'at_present': [13], 'almost': [20], 'dispirited': [2], 'take_up': [44], 'break_up': [30], 'afford': [40, 20], 'as_well': [23], 'expose': [30], 'give_way': [20, 21, 30], 'impress': [16, 29], 'scummy': [2], 'depression': [2], 'chocolate': [31], 'downhearted': [2], 'disruption': [30], 'computer_backup': [44], 'breach': [30], 'hold': [9, 27, 20, 43, 44], 'add_together': [1, 23], 'shoot': [44], 'involve': [44, 38, 30, 31], 'account': [18], 'unrivalled': [29], 'micturate': [27, 9, 43], 'befuddle': [11], 'work': [27, 9, 43, 21], 'close_to': [20], 'request': [18], 'channelise': [39], 'learn': [10, 44, 6], 'commemorate': [24], 'meet': [10, 6], 'americium': [32, 21], 'root': [40], 'control': [10, 11, 28, 6], 'claim': [44, 21], 'loosen': [28], 'prompt': [29], 'want': [38, 30, 31], 'figure': [4, 6, 7, 9, 10, 14, 15, 16, 22, 29], 'give': [40, 9, 43, 20, 27, 30], 'predict': [21], 'choice': [13], 'Capital': [11], 'tax': [1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 29, 37, 44], 'accept': [44], 'get_off': [17], 'Almighty': [43], 'recall': [24], 'progress_to': [27, 9, 43], 'attain': [27, 9, 43], 'dictation': [11, 28], 'jumble': [11], 'Lord': [43], 'dress': [3], 'happy_chance': [30], 'weaken': [30], 'end': [3], 'bankrupt': [30], 'turn': [14], 'tilt': [44, 10, 4, 15], 'travel': [29, 21], 'breaking': [30], 'economic_consumption': [0, 24, 19, 23], 'feature': [18], '1': [29], 'purchase_order': [37], 'UN': [28], 'hop': [12], 'musical_accompaniment': [44], 'answer': [3], 'telephone_number': [14], 'construe': [10, 6], 'fare': [3], 'regularise': [37], 'bidding': [11, 28], 'attend': [10, 6], 'peerless': [29], 'watch': [10, 6], 'sacrifice': [20], 'after': [12], 'sympathize': [36], 'substitute': [44], 'David_Low': [2], 'modest': [2, 11], 'produce': [1, 27, 43, 9], 'induce': [27, 9, 43], 'open_air': [40], 'date': [10, 6], 'get_along': [3], 'outcry': [21], 'coif': [3], 'goal': [3], 'prison-breaking': [30], 'scurvy': [2], 'Divine': [43], 'remember': [24], 'break_dance': [30], 'stand_for': [35], 'shout': [21], 'spout': [26, 27], 'seduce': [27, 9, 43], 'departure': [21], 'pocket-size': [11], 'recrudesce': [30], 'switch': [9, 37], 'foretell': [21], 'break_out': [30], 'suggest': [18], 'offend': [30], 'bastardly': [35], 'subsequently': [12], 'operate': [21], 'good_luck': [30], 'go_through': [10, 6], 'feed': [20], 'gloomy': [2], 'pester': [18], 'afterwards': [12], 'help': [38], 'reservoir': [40], 'devote': [20], 'move': [29, 21], 'vary': [9, 37], 'previous': [12], 'kickoff': [13], 'sleepyheaded': [32], 'see_to_it': [10, 6], 'cook': [27, 9, 43], 'paper': [18], 'straight_off': [13], 'conk_out': [21, 30], 'inaugural': [13], 'indigence': [38, 30, 31], 'badger': [18], 'takings': [44], 'relegate': [30], 'nominate': [27, 9, 43, 22], 'assailable': [40], 'fit': [21], 'forthwith': [13], 'exact': [44], 'fix': [27, 9, 43], 'conduct': [44, 39], 'photographic_print': [16], 'labor': [1, 2, 3, 4, 37, 6, 7, 9, 10, 44, 13, 12, 15, 16, 17, 14, 29, 5], 'better': [30], 'grade': [37], 'templet': [39], 'choose': [44, 13], 'listing': [44, 10, 4, 15], 'bespeak': [18], 'mail': [17], 'arrange': [3, 37], 'alter': [9, 37], 'ally': [23], 'instantly': [13], 'count': [14], 'non': [36], 'savoir-faire': [8], 'unveiling': [20], 'smash': [30], 'fetch_up': [3], 'propose': [16, 18, 4, 7, 9, 10, 29, 15], 'origination': [20], 'practice': [0, 19, 3, 24, 23], 'pass_water': [27, 9, 43], 'break': [20, 21, 30], 'mention': [22], 'rank': [37], 'not': [36], 'suffice': [3], 'altogether': [16, 17, 10, 4, 7], 'now': [13], 'complain': [18], 'prize': [13], 'bedevil': [11], 'execute': [3], 'polish': [3], 'drop_dead': [21], 'defecate': [27, 9, 43], 'mastery': [11, 28], 'undertaking': [1, 2, 3, 4, 37, 6, 7, 9, 10, 44, 13, 12, 15, 16, 17, 14, 29, 5], 'make_a_motion': [29], 'debut': [20], 'infer': [36], 'consecrate': [20, 37], 'externalise': [4, 7, 9, 10, 15, 16, 29], 'realise': [36, 6, 9, 10, 43, 27], 'Associate_in_Nursing': [17, 7], 'entirely': [16, 17, 10, 4, 7], 'mean': [35], 'interruption': [30], 'retrieve': [24, 5], 'another': [8, 29], 'low-toned': [2], 'bump': [5, 30], 'list': [4, 10, 44, 14, 15, 22], 'yeah': [34], 'ordain': [37], 'breakthrough': [5], 'society': [37], 'call_for': [18, 44, 38, 30, 31], 'remove': [3, 44], 'first_off': [13], 'happen': [5], 'ring': [21], 'witness': [10, 5, 6], 'small-scale': [11], 'decree': [37], 'low-pitched': [2], 'opened': [40], 'jabber': [26, 27], 'publish': [16], 'wholly': [16, 17, 10, 4, 7], 'enjoyment': [0, 24, 19, 23], 'impart': [1, 20, 23], 'intermit': [30], 'overlook': [11, 28], 'dominate': [11, 28], 'issue': [44, 14], 'Das_Kapital': [11], 'pauperism': [38, 30, 31], 'disclose': [30], 'foundation': [20], 'get_hold': [5], 'perish': [21], 'contain': [44], 'little': [11], 'undo': [28], 'pop_off': [21], 'completely': [16, 17, 10, 4, 7], 'base': [35], 'faulting': [30], 'matchless': [29], 'besides': [23], 'ask': [44, 38, 30, 31], 'well-nigh': [20], 'working_capital': [11], 'beginning': [40, 13], 'generate': [20], 'skip_over': [12], 'patronage': [44], 'unresolved': [40], 'get_rid_of': [3], 'come_up': [5], 'diminished': [11], 'blue-pencil': [3], 'replacement': [9], 'motion': [29], 'let_out': [30], 'tack': [9], 'place': [17, 37], 'testament': [21], 'capital_letter': [11], 'time_out': [30], 'feature_film': [18], 'facilitate': [38], 'think': [24, 35], 'crushed': [2], 'first': [2, 13], 'origin': [40], 'render': [20], 'feel': [5], 'confuse': [11], 'number': [44, 10, 4, 14, 15], 'fancy': [4, 6, 7, 9, 10, 15, 16, 29], 'one': [29], 'rant': [26, 27], 'number_1': [13], 'done': [3], 'construct': [27, 9, 43], 'directly': [13], 'enumerate': [14], 'carry': [44], 'signify': [35], 'demote': [30], 'call_option': [21], 'open': [40, 20], 'mingy': [35], 'upper-case_letter': [11], 'interchange': [9, 37], 'story': [18], 'service': [38], 'utilization': [0, 24, 19, 23], 'introduction': [20], 'think_back': [24], 'creator': [43], 'occupy': [44], 'tot': [1, 23], 'legal_brief': [20], 'priority': [2, 37], 'telephone_call': [21], 'station': [17], 'flip-flop': [9], 'motility': [29], 'escort': [10, 6], 'postulate': [44, 38, 30, 31], 'recent': [12], 'enjoin': [37], 'cite': [22], 'friend': [23], 'too': [23], 'murder': [3], 'collapse': [20, 30], 'charter': [44], 'discombobulate': [11], 'pee-pee': [27, 9, 43], 'acquire': [44], 'serve': [3, 38], 'yield': [44, 20], 'direct': [8, 17, 44, 39], 'broadcast': [17], 'guidebook': [39], 'part': [30], 'incur': [5], 'rifle': [21], 'send_for': [21], 'get_word': [10, 6], 'on_a_lower_floor': [2], 'institution': [20], 'reliever': [44], 'guild': [37], 'by_and_by': [12], 'Creator': [43], 'depressed': [2], 'split': [30], 'require': [38, 11, 44, 28, 30, 31], 'like_a_shot': [13], 'Am': [32, 21], 'project': [1, 2, 3, 4, 37, 6, 7, 9, 10, 44, 13, 12, 15, 16, 17, 14, 29, 5], 'just_about': [20], 'cost': [32, 21], 'endure': [21], 'take_a_leak': [27, 9, 43], 'outdoors': [40], 'embody': [32, 21], 'lease': [44], 'birdsong': [21], 'attention_deficit_hyperactivity_disorder': [1, 23], 'motivation': [38, 30, 31], 'instauration': [20], 'entail': [35], 'slay': [3], 'pretend': [27, 9, 43], 'swop': [9], 'penury': [38, 30, 31], 'coffee_bean': [31], 'seed': [40], 'minimal_brain_damage': [1, 23], 'depleted': [2], 'close': [3], 'need': [44, 38, 30, 31], 'right_away': [13], 'put_off': [11], 'recover': [5], 'seek': [5], 'Idaho': [27], 'low_gear': [2, 13], 'channelize': [39], 'beleaguer': [18], 'spend_a_penny': [27, 9, 43], 'make_up': [32, 9, 43, 21, 27], 'pocket-sized': [11], 'divulge': [30], 'also': [23], 'potential': [16], 'take': [3, 38, 39, 9, 43, 44, 13, 27, 30, 31], 'institutionalise': [17], 'call_back': [24], 'transmit': [17], 'prisonbreak': [30], 'switching': [9], 'club': [37], 'pick_up': [10, 6], 'regard': [10, 6], 'maiden': [13], 'take_a_shit': [27, 9, 43], 'reckon': [10, 6], 'reach': [9, 27, 20, 43], 'regulate': [37], 'rearrange': [37], 'most': [20], 'miserly': [35], 'visualize': [4, 6, 7, 9, 10, 15, 16, 29], 'plan': [4, 7, 9, 10, 15, 16, 29], 'utilize': [0, 24, 19, 23], 'number_one': [13], 'why': [19, 11], 'pauperization': [38, 30, 31], 'live_on': [21], 'demand': [44, 38, 30, 31], 'cause': [27, 43, 3, 9], 'get-go': [13], 'eat_up': [3], 'average': [35], 'adopt': [44], 'cover': [8, 18], 'institutionalize': [17], 'order': [37], 'split_up': [30], 'reputation': [18], 'hyperkinetic_syndrome': [1, 23], 'accompaniment': [44], 'pick_out': [44, 13], 'Godhead': [43], 'blend': [21], 'sum': [1, 23], 'take_aim': [44], 'or_so': [20], 'first_base': [13], 'parliamentary_law': [37], 'recess': [30], 'set': [3], 'lower-case_letter': [11], 'wiretap': [18], 'rabbit_on': [26, 27], 'manipulation': [0, 24, 19, 23], 'terminate': [3], 'skitter': [12], 'hemipterous_insect': [18], 'ending': [3], 'bring': [1, 44, 23], 'uncommitted': [25], 'supporter': [38, 23], 'for_the_first_time': [13], 'cease': [3], 'pause': [30], 'Gem_State': [27], 'shuffling': [9, 27], 'Friend': [23], 'sleepy-eyed': [32], 'ruin': [30], 'bust': [30], 'falling_out': [30], 'theme': [18], 'going': [21], 'asking': [18], 'lodge': [37], 'orderliness': [37], 'sound_off': [18], 'plump': [21], 'edict': [37], 'run_short': [21], 'hit': [27, 43, 3, 9], 'template': [39], 'first_of_all': [13], 'assistant': [38], 'coiffe': [3], 'blur': [11], 'stop': [3, 30], 'break_off': [30], 'foremost': [13], 'beam': [17], 'go_bad': [21, 30], 'nearly': [20], 'later_on': [12], 'hop-skip': [12], 'report': [18], 'humbled': [2], 'coating': [3], 'unfastened': [40], 'insertion': [20], 'World_Health_Organization': [43], 'reveal': [30], 'earn': [27, 9, 43], 'fox': [11], 'wind_up': [3], 'transposition': [9], 'cry': [21], 'Washington': [11], 'alteration': [9, 37], 'at_once': [13], 'erupt': [30], 'undefendable': [40], 'evoke': [18], 'ascertain': [10, 5, 6], 'release': [21], 'through': [3], 'obscure': [11], 'key_out': [22], 'anticipate': [21], 'quetch': [18], 'view': [10, 6], 'ca-ca': [27, 9, 43], 'call_up': [24, 21], 'omission': [12], 'stick_out': [4, 7, 9, 10, 15, 16, 29], 'reference': [8, 40], 'burst': [30], 'puddle': [27, 9, 43], 'unmake': [28], 'flip': [9], 'use_of_goods_and_services': [0, 24, 19, 23], 'culture': [3], 'see': [4, 5, 6, 7, 9, 10, 15, 16, 36, 29], 'usance': [0, 24, 19, 23], 'phone_call': [21], 'prognosticate': [21], 'fail': [21, 30], 'miserable': [2], 'sport': [18], 'program_line': [11, 28], 'subject': [40], 'majuscule': [11], 'empathise': [36], 'detect': [5], 'call_in': [21], 'end_up': [3], 'utilise': [0, 24, 19, 23], 'incite': [29], 'equal': [32, 21], 'quality': [13], 'antecedency': [2, 37], 'belittled': [11], 'shuffle': [9, 27], 'score': [27, 9, 43], 'Master_of_Arts': [32, 21], 'finishing': [3], 'routine': [14], 'polish_off': [3], 'email': [8, 17, 7], 'discovery': [5], 'available': [25], 'notice': [5], 'loose': [40], 'add_up': [1, 14, 23], 'extend': [21], 'visualise': [4, 6, 7, 9, 10, 15, 16, 29], 'look_at': [44], 'lineament': [18], 'job': [1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 29, 37, 44], 'wear': [30], 'key': [22], 'distinguish': [22], 'umber': [31], 'Maker': [43], 'aim': [44], 'undetermined': [40], 'useable': [25], 'last': [3, 21], 'hemipteran': [18], 'move_out': [3], 'write_up': [18], 'fault': [30], 'cancel': [3], 'hint': [18], 'dedicate': [20], 'contract': [44], 'assure': [10, 6], 'initiatory': [13], 'steer': [39], 'help_oneself': [38], 'prescribe': [37], 'whole': [16, 17, 10, 4, 7], 'down_the_stairs': [2], 'to_a_fault': [23], 'alternate': [9], 'small_letter': [11], 'unfold': [40], 'stream': [2, 6, 15], 'supply': [1, 23], 'fiat': [37], 'mean_value': [35], 'switch_over': [9], 'dispatch': [3], 'public_figure': [22], 'commend': [24], 'subscribe': [44], 'initiative': [13], 'Low': [2], 'lowly': [2, 11], 'rave': [26, 27], 'line_up': [5], 'coffee_berry': [31], 'sledding': [21], 'speak': [8], 'late': [12], 'java': [31], 'capable': [40], 'come': [3, 14], 'damp': [30], 'buy_the_farm': [21], 'God_Almighty': [43], 'tote_up': [1, 23], 'unmatchable': [29], 'advert': [22], 'showtime': [13], 'make_out': [3], 'initiation': [20], 'treat': [8], 'likewise': [23], 'report_card': [18], 'make_water': [27, 9, 43], 'I.D.': [27], 'phone_number': [14], 'sum_up': [1, 23], 'jabbering': [26, 27], 'ME': [20], 'contribute': [1, 20, 23], 'champion': [23], 'break-dance': [30], 'tap': [18], 'deep_brown': [31], 'change_over': [9], 'gap': [30], 'habituate': [0, 24, 19, 23], 'ordering': [37], 'observe': [5], 'locomote': [29, 21], 'hateful': [35], 'suspension': [30], 'catch': [10, 6], 'deepen': [9, 37], 'rupture': [30], 'Sir_David_Alexander_Cecil_Low': [2], 'present': [20], 'sound': [21], 'practise': [3], 'take_care': [10, 6], 'send_off': [4, 7, 9, 10, 15, 16, 17, 29], 'plain': [18], 'examine': [10, 6], 'air': [17], 'think_of': [24, 35], 'cast': [4, 7, 9, 10, 15, 16, 29], 'near': [20], 'intro': [20], 'expiration': [21], 'computer_address': [8], 'pass_over': [12], 'aid': [38], 'piddle': [27, 9, 43], 'guide': [44, 39], 'pack': [44], 'unitary': [29], 'get_out': [30], 'helper': [38], 'backing': [44], 'dictate': [37], 'contrive': [16, 4, 7, 9, 10, 29, 15], 'coffee': [31], 'surface': [40], 'gens': [22], 'confound': [11], 'parliamentary_procedure': [37], 'excessively': [23], 'kick_the_bucket': [21], 'get_wind': [10, 6], 'run_into': [10, 6], 'return': [44, 20], 'conk': [21], 'id': [27], 'volition': [21], 'ordination': [37], 'urinate': [27, 9, 43], 'develop': [30], 'author': [40], 'MBD': [1, 23], 'pay': [20], 'make': [27, 1, 3, 20, 22, 9, 43, 44], 'belong': [21], 'admit': [44], 'externalize': [4, 7, 9, 10, 15, 16, 29], 'check': [10, 6, 30], 'unity': [29], 'wherefore': [19, 11], 'speech': [8], 'be_active': [29], 'get_hold_of': [44], 'modification': [9, 37], 'blend_in': [21], 'advise': [18], 'fill': [44], 'Order': [37], 'composition': [18], 'finish': [3], 'keep_down': [14], 'I': [29], 'get_around': [30], 'assist': [38], 'epithet': [22], 'possible': [16], 'flurry': [11], 'postulation': [18], 'purpose': [0, 24, 19, 23], 'rootage': [40], 'come_across': [10, 6], 'find_out': [10, 5, 6], 'build': [27, 9, 43], 'overt': [40], 'totally': [16, 17, 10, 4, 7], 'passing': [21], 'disconcert': [11], 'booster': [23], 'insure': [10, 6], 'rift': [30], 'expend': [0, 24, 19, 23], 'task': [1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 14, 15, 16, 17, 29, 37, 44], 'off': [3], 'humble': [2, 11], 'roughly': [20], 'gabble': [26, 27], 'chore': [1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 29, 37, 44], 'command': [11, 28], 'relief': [44], 'withdraw': [3, 44], 'firstly': [13], 'entry': [20], 'comprise': [32, 21], 'have_in_mind': [35], 'wee-wee': [27, 9, 43], 'tot_up': [1, 23], 'name_and_address': [8], 'identification_number': [14], 'precedence': [2, 37], 'anteriority': [2, 37], 'yea': [34], 'going_away': [21], 'out-of-doors': [40], 'sleepy': [32], 'obtain': [5], 'get_to': [27, 9, 43], 'interrupt': [30], 'identify': [22], 'lay_down': [27, 9, 43], 'depart': [21], 'yes': [34], 'run_across': [10, 6], 'bit': [14], 'go_steady': [10, 6], 'consume': [44], 'cut': [12], 'generator': [40], 'founding': [20], 'fall_apart': [30], 'instruction': [11, 28], 'realize': [36, 6, 9, 10, 43, 27], 'source': [40], 'add': [1, 23], 'spread': [40], 'crack': [30], 'usage': [0, 24, 19, 23], 'lookup': [5], 'electric_current': [2, 6, 15], 'kick': [18], 'beggarly': [35], 'give_away': [30], 'usable': [25], 'fracture': [30], 'habit': [0, 24, 19, 23], 'read': [44, 36], 'bid': [11, 28, 21], 'discontinue': [30], 'displace': [29], 'proceeds': [44], 'quest': [18], 'moo': [2], 'take_on': [44], 'immediately': [13], 'breakage': [30], 'grim': [2], 'name': [27, 4, 21, 22, 9, 10, 43, 44, 15], 'wear_out': [30], 'loss': [21], 'Jehovah': [43], "cash_in_one's_chips": [21], 'gift': [20], 'low-down': [2], 'hunt': [5], 'manual': [39], 'substitution': [9], 'tardy': [12], 'undefended': [40], 'edit': [3], 'destination': [8, 3], 'through_with': [3], 'bound_off': [12], 'become': [21], 'break_in': [30], 'transgress': [30], 'scout': [39], 'decease': [21], 'stimulate': [27, 9, 43], 'envision': [4, 6, 7, 9, 10, 15, 16, 29], 'propel': [29], 'exposed': [40], 'uppercase': [11], 'get_going': [21], 'creation': [20], 'some': [20], 'telephone': [21], 'send_out': [17], 'motive': [38, 30, 31], 'accost': [8], 'erase': [3], 'holler': [21], 'convey': [44], 'intend': [35], 'antecedence': [2, 37], 'informant': [40], 'employment': [0, 24, 19, 23], 'unrivaled': [29], 'transport': [17], 'absent': [3], 'Artium_Magister': [32, 21], 'acquaintance': [23], 'lead': [44, 21, 39], 'severance': [30], 'separate': [30], 'bring_up': [22], 'overly': [23], 'unmatched': [29], 'e-mail': [8, 17, 7], 'breakout': [30], 'exit': [21], 'innovation': [20], 'look_for': [5], 'pee': [27, 9, 43], 'pass_on': [20], 'refer': [22], 'go_against': [30], 'be': [32, 21], 'precedency': [2, 37], 'run': [39, 29, 21], 'intimate': [18], 'more_or_less': [20], 'use': [0, 24, 19, 23], 'infra': [2], 'squall': [21], 'broken': [2], 'rent': [44], 'expire': [21], 'respite': [30], 'offset': [13], 'astir': [20], 'post': [17], 'throw': [11, 4, 7, 9, 10, 43, 15, 16, 20, 27, 29], 'finish_up': [3], 'about': [20], 'consumption': [0, 24, 19, 23], 'ace': [29], 'tease': [18], 'choke': [21], 'ingest': [44], 'range': [37], 'statement': [11, 28], 'ensure': [10, 6], 'heel': [44, 10, 4, 15], 'protagonist': [23], 'act': [3, 29, 14], 'fuddle': [11], 'commit': [17, 20], 'jut_out': [4, 7, 9, 10, 15, 16, 29], 'backup': [44], 'create': [1, 27, 43, 9], 'come_up_to': [8], 'croak': [21], 'outset': [13], 'WHO': [43], 'film': [44], 'kick_in': [20], 'kick_downstairs': [30], 'image': [4, 6, 7, 9, 10, 15, 16, 29], 'actuate': [29], 'monastic_order': [37], 'set_up': [37], 'down': [2], 'promise': [21], 'determine': [10, 5, 6], 'ADHD': [1, 23], 'approximately': [20], 'bump_off': [3], 'mark': [16], 'nowadays': [13], 'numerate': [14], 'beneath': [2], 'vamoose': [12], 'refinement': [3], 'chitter': [41], 'deal': [8, 44], 'prepare': [27, 9, 43], 'transfer': [9, 3, 37], 'support': [44], 'take_away': [3, 44], 'relocation': [29], 'posterior': [12], 'submit': [44], 'avail': [38], 'start': [21, 13], 'cultivation': [3], 'low': [2, 11, 13], 'spring': [20], 'untie': [28], 'translate': [36], 'mix_up': [11], 'twitter': [41], 'launching': [20], 'function': [0, 24, 19, 21, 23], 'head': [39], 'hemipteron': [18], 'perplexing': [11], 'complete': [3], 'form': [27, 9, 43], 'unwrap': [28, 30], 'gild': [37], 'geological_fault': [30], 'brand': [9, 27], 'tally': [1, 23], 'pathfinder': [39], 'change': [9, 37], 'pass_away': [21], 'ADD': [1, 23], 'hear': [10, 6], 'gain': [9, 27, 43], 'jut': [4, 7, 9, 10, 15, 16, 29], 'ID': [27], 'downstairs': [2], 'bug': [18], 'belated': [12], 'straightaway': [13], 'constitute': [32, 9, 43, 21, 22, 27], 'hire': [44], 'made': [43], 'perform': [3], 'piss': [27, 9, 43], 'intermission': [30], 'characteristic': [18], 'receptive': [40], 'move_over': [20], 'hold_up': [21], 'assume': [44], 'below': [2], 'turn_to': [8], 'minor': [11], 'hand': [20], 'usher': [39], 'clear': [40, 9, 43, 27], 'say': [37], 'delete': [3], 'diagnose': [22], 'land_up': [3], 'break_away': [30], 'bring_out': [30], 'flow': [2, 6, 15], 'describe': [18, 22], 'drive': [44], 'single': [29], 'meanspirited': [35], 'exist': [32, 21], 'burnt_umber': [31], 'first-class_honours_degree': [13], 'payoff': [44], 'ship': [17], 'petition': [18], 'nonpareil': [29], 'shit': [27, 9, 43], 'wee': [27, 9, 43], 'coffee_tree': [31], 'puzzling': [11], 'first_gear': [2, 13], 'variety': [9, 37], 'relieve_oneself': [27, 9, 43], 'prime': [13], 'hollo': [21], 'tight': [35], 'forebode': [21], 'role': [0, 24, 19, 23], 'tutorial': [39], 'confusing': [11], 'finis': [3], 'conclusion': [3], 'sympathise': [36], 'picture': [4, 6, 7, 9, 10, 15, 16, 29], 'draw': [27, 9, 43, 39], 'championship': [44], 'minimal_brain_dysfunction': [1, 23], 'lend': [1, 23], 'put': [37], 'order_of_magnitude': [37], 'finale': [3], 'AM': [32, 21], 'virtually': [20], 'AN': [17, 7], 'chance': [5], 'hold_out': [21], 'go_away': [21], 'mouth_off': [26, 27], 'run_low': [21], 'trade': [9], 'appoint': [22], 'bring_in': [27, 9, 43], 'go_out': [10, 6], 'overtop': [11, 28], 'downcast': [2], 'snap_off': [30], 'heart-to-heart': [40], 'humiliated': [2], 'Quaker': [23], 'rule': [5], 'scream': [21], 'train': [44], 'social_club': [37], 'understand': [10, 36, 6], 'yell': [21], 'take_a_crap': [27, 9, 43], 'convert': [9, 37], 'commencement': [13]}


def get_response(textin):        
    
    words=re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", textin)

    scores={}
    max_score=0.0
    syn_factor = 0.1

    for word in words:
        if word in vocab:
            for question_index in vocab[word]:
                s = scores.setdefault(question_index,0.0)
                scores[question_index] = s + 1.0/float(len(vocab[word]))
            max_score += 1.0/float(len(vocab[word]))
        if word in synvocab:
            for question_index in synvocab[word]:
                s = scores.setdefault(question_index,0.0)
                scores[question_index] = s + syn_factor/float(len(synvocab[word]))
            max_score += syn_factor/float(len(synvocab[word]))

    try:
        score,index = sorted([(v,k) for k,v in scores.iteritems()])[-1]
        return kb[index][1]
    except:
        return None
              