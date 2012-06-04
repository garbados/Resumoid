from db import db
from auth.models import User
import datetime

def TagField():
    return db.ListField(db.StringField(max_length=30))

class TimeStampDoc(db.Document):
    """
    Adds timestamps to documents
    """
    created_on = db.DateTimeField(default=datetime.datetime.now())
    updated_on = db.DateTimeField()
    meta = dict(allow_inheritance=True)

    def save(self):
        if self.created_on:
            self,updated_on = datetime.datetime.now()
        super(TimeStampDoc, self).save()

class Group(db.Document):
    name = db.StringField()
    tagline = db.StringField()
    description = db.StringField()
    users = db.ListField(db.ReferenceField(User))

    def get_tag_dict(self):
        """
        Returns a dictionary of all the tags associated with the group
        with frequencies for each tag. Used to establish interests.
        NOTE: Currently only collects tags from opportunities, not 
        questions."""
        opportunities = Opportunity.objects(group=self)
        tags  = dict()
        for opportunity in opportunities:
            for tag in opportunity.tags:
                tags[tag] = tags[tag] + 1 if tags.has_key(tag) else 1
        return tags

class Opportunity(db.Document):
    group = db.ReferenceField(Group)
    title = db.StringField(max_length=100)
    description = db.StringField()
    tags = TagField()

class Question(TimeStampDoc):
    opportunity = db.ReferenceField(Opportunity)
    title = db.StringField(max_length=100)
    description = db.StringField()
    tags = TagField()

    def get_tags(self):
        return self.tags + self.opportunity.tags

class Answer(TimeStampDoc):
    user = db.ReferenceField(User)
    question = db.ReferenceField(Question)
    body = db.StringField()
    is_draft = db.BooleanField(default=True)

    def get_tags(self):
        return self.question.get_tags()

    def save(self):
        """
        If the answer is no longer a draft, create an application.
        """
        if not self.is_draft:
            app_kwargs = dict(answer=self,
                    question=self.question)
            application = Application.objects(**app_kwargs)
            if not application:
                Application(**app_kwargs).save()
        super(Answer, self).sav()
