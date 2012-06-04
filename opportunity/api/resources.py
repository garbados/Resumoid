from flask.views import MethodView
from helpers import unravel
from flask.ext.mongoengine.wtf import model_form
from flask import jsonify, request
from flask.ext.login import login_required

class Resource(MethodView):
    """
    Generic model resource, for building APIs from mongoengine models.
    """
    model = None
    name = None
    # Meta class for further options

    def get_form(self):
        """
        Generates the form used for validating POST input
        """
        return model_form(self.model)

    def process_form(self, form):
        if form.validate():
            form.save()
            return ''
        else:
            bundle = form.errors
            # accomodate more serialization formats
            response = jsonify(bundle)
            response.status_code = 400
            return response

    def get(self, obj_id):
        """
        Return a list of Group objects defined by the kwargs
        Returned list serialized as JSON
        """
        # curate querystring args
        query_options = dict(request.args)
        if obj_id:
            obj = self.model.objects(id=id, **query_options).first()
            bundle = unravel(obj)
        else:
            query = self.model.objects(**query_options)
            bundle = dict(
                    objects=[unravel(obj) for obj in query.all()],
                    meta=dict(
                        total=query.count()))
        # accomodate more serialization formats
        return jsonify(bundle)

#    @login_required
    def post(self):
        """
        Given a set of named params, attempts to create a new object
        or update an existing one from those params. If the params don't 
        validate, return the errors that prevented saving the object.
        """
        form = self.get_form()(**request.form)
        return self.process_form(form)

#    @login_required
    def put(self, obj_id):
        """
        Given a set of named params, attempts to update an existing object
        with those params. If the object doesn't exist, attempt to create it.
        Returns either the created object or the errors that prevented 
        updating.
        """
        try:
            obj = self.model.objects(id=obj_id).get()
        except Exception as e:
            error = jsonify(dict(e))
            error.status_code = 400
            return error
        form = self.get_form()(instance=obj, **request.form)
        return self.process_form(form)

#    @login_required
    def delete(self, obj_id):
        """
        Marks the named object for deletion.
        If `force` is True, actually delete the object.
        Accepts `id` as either a string or ObjectId.
        """
        obj = self.model.objects(id=obj_id)
        if 'force' in request.args.keys():
            try:
                obj.delete(safe=True)
            except Exception as e:
                # todo: check for specific exceptions
                error = jsonify(dict(e))
                error.status_code = 500
                return error
        else:
            # todo: create a matching `deleted` field in our models
            obj.deleted = True
        return ''
