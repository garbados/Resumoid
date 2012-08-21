from db import db
from auth.models import User
import datetime

def TagField():
    return db.ListField(db.StringField())

class TimeStampDoc(db.Document):
    """
    Adds timestamps to documents
    """
    created_on = db.DateTimeField(default=datetime.datetime.now())
    updated_on = db.DateTimeField()
    meta = dict(allow_inheritance=True)

    def save(self):
        if self.created_on:
            self.updated_on = datetime.datetime.now()
        super(TimeStampDoc, self).save()

class Question(TimeStampDoc):
    author = db.ReferenceField(User)
    title = db.StringField(max_length=100)
    tags = TagField()

class Answer(TimeStampDoc):
    user = db.ReferenceField(User)
    question = db.ReferenceField(Question)
    tags = TagField()
    body = db.StringField(max_length=1000)
    is_draft = db.BooleanField(default=True)