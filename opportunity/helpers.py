"""
Helper classes for views, like generators for generic views
"""
from flask import render_template

def generate_list_and_detail(model):
    view_name = model.__name__.lower()
    def model_view(id=None):
        context = dict()
        if id:
            context[view_name] = model.objects(id=id).get_or_404()
            return render_template('%s/detail.html' % view_name, **context)
        else:
            context['%s_list' % view_name] = model.objects.all()
            return render_template('%s/list.html' % view_name, **context)
    return model_view
