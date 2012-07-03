"""
Controllers that implement the API for the Opportunity module's models.
"""
from models import Group, Opportunity, Question, Answer

def _serialize(obj):
    """
    Converts mongoengine model objects to JSON.
    """
    return obj.to_mongo

class Resource(object):
    """
    Generic RESTful API class. Subclass and customize to generate resources
    for specific models.
    Params:
        `model` The model object for this Resource
        `form`  A form object for validating POST and PUT requests.
    """
    model = None
    form = None

    def get(self, id=None):
        response = dict()
        if id:
           queryset = self.model.objects(id=id)
        else:
            queryset = self.model.objects
        response['total'] = queryset.count()
        # todo: pagination
        response['objects'] = \
                [model._serialize() for model in queryset.all()]
        return response

    def post(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass
