"""
Methods and classes for serializing models into various formats.
"""
import json

# to add more formats, give it a key and a function
# that takes a dict as its single argument
SERIALIZATION_FORMATS = {
    'json' : json.dumps,
    }

def serialize(obj, format=None):
    """
    Converts model instance `obj` to a serialized format such as JSON.
    Currently only does JSON.
    """
    obj_dict = dict()
    for key, value in obj.to_mongo().iteritems():
        if key in obj._fields.keys():
            obj_dict[key] = value
    if format:
        try:
            return SERIALIZATION_FORMATS[format.lower()](obj)
        except KeyError:
            # unrecognized format
            # todo: deal with unrecognized format
            pass
    else:
        # default to json
        return SERIALIZATION_FORMATS['json'](obj)


