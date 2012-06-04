from models import *
from api import Resource

class GroupResource(Resource):
    model = Group
    name = 'group'

class OpportunityResource(Resource):
    model = Opportunity
    name = 'opportunity'

class QuestionResource(Resource):
    model = Question
    name = 'question'

class AnswerResource(Resource):
    model = Answer
    name = 'answer'

resources = []
for resource in [GroupResource, 
                OpportunityResource,
                QuestionResource,
                AnswerResource]:
    resources.append(resource)
