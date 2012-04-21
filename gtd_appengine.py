#!/usr/bin/env python

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.api import xmpp
from google.appengine.api import mail

from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import xmpp_handlers

import logging
import cgi

from models import *
from gtdstack import GTDStack


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Redirecting to <a href="https://bitbucket.org/hiway/gtdstack/"https://bitbucket.org/hiway/gtdstack/</a>')
        self.redirect(URL)
        

class XmppHandler(xmpp_handlers.CommandHandler):
    def unhandled_command(self, message=None):
        # Display help message.
        message.reply("Uh oh!")

    def text_message(self, message=None):        
        # get only the email/jabber ID, not the resource, so skip
        # everything after the /
        user = str(message.sender).split("/")[0]
        
        input_str = str(message.arg)
        
        userdata = Tasklist.get(user)        
        stack = GTDStack(userdata)
        
        if input_str == "email":
            # Intercept regular operation, this isn't common feature
            body = stack.get_all_task_lists()
            
            mail.send_mail(sender="GTDStack <tasks@gtdstack.appspotmail.com>",
                           to=user,
                           subject="GTDStack: All Tasks",
                           body=body
                )
            
            message.reply("Email sent to %s!" %user)
            
        else:
            response = stack.parse_command(input_str)
            
            if response[0] == ".":
                # all our methods to parse failed, mail admin for debugging
                # or the chatbot has reported low confidence.
                mail.send_mail(sender="GTDStack <tasks@gtdstack.appspotmail.com>",
                           to="harshad.sharma+gtdstack@gmail.com",
                           subject="GTDStack: Parsing Error",
                           body=input_str
                )
                
                response = response[1:]
                
                message.reply("Oops! Looks like this wasn't an answer you expected,")
                message.reply("I've notified administrator, anonymously.")
            
            message.reply(response)    
            
        Tasklist.set(user, stack.get_data())

def main():
    application = webapp.WSGIApplication([
                                    ('/', MainHandler),
                                    ('/_ah/xmpp/message/chat/', XmppHandler),
                                    ],
                                    debug=True)
    
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
