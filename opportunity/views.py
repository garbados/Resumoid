from flask import Blueprint, render_template
from opportunity.models import *
from helpers import generate_list_and_detail
from api.helpers import register_api
from controllers import resources

views = Blueprint('views',
                  __name__,
                  template_folder="templates",
                  static_folder="static")

for resource in resources:
    register_api(views, resource)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/groups/')
@views.route('/group/<id>')
def groups(id=None):
    return generate_list_and_detail(Group)(id)

@views.route('/opportunities/')
@views.route('/opportunity/<id>')
def opportunities(id=None):
    return generate_list_and_detail(Opportunity)(id)

@views.route('/questions/')
@views.route('/question/<id>')
def questions(id=None):
    return generate_list_and_detail(Question)(id)
