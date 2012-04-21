from google.appengine.ext import db
from django.utils import simplejson as json

class Tasklist(db.Model):
    value = db.TextProperty()
    
    @staticmethod
    def get(user):
        tasklist = Tasklist.get_by_key_name(user)
        return tasklist and json.loads(tasklist.value)
    
    @staticmethod
    def set(user, tasklist):
        tasklist = json.dumps(tasklist)
        Tasklist(key_name=user, value=tasklist).put()

