from db import db
from bson.objectid import ObjectId

def unravel(obj):
    """
    Dereferences an object, and all relations, into dict form,
    for serialization.
    """
    serialization = dict()
    for field in obj._fields.keys():
        value = getattr(obj, field)
        if issubclass(type(value), db.Document):
            serialization[field] = unravel(value)
        elif issubclass(type(value), ObjectId):
            # get str value for id
            serialization[field] = str(value)
            pass
        else:
            serialization[field] = value
    return serialization

def ravel(bundle):
    """
    Converts querystring and form nonsense into a real, live object.
    Equivalent to tastypie's "hydrate" process.
    """
    pass

def register_api(app, resource):
    """
    Registers the resource with an app or blueprint.
    """
    obj_view = resource.as_view('{0}_api'.format(resource.name))
    app.add_url_rule('/api/{0}/'.format(resource.name), 
                        defaults={'obj_id': None},
                        view_func=obj_view, 
                        methods=['GET',])
    app.add_url_rule('/api/{0}/'.format(resource.name), 
                        view_func=obj_view, 
                        methods=['POST',])
    app.add_url_rule('/api/{0}/<int:obj_id>'.format(resource.name), view_func=obj_view,
                        methods=['GET', 'PUT', 'DELETE'])

