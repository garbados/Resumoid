from flask import Blueprint, render_template
from flask_login import current_user
from models import *

views = Blueprint('views', __name__)

@views.route('/<id>')
def portfolio(id):
    """
    A user's portfolio.
    """
    if id == current_user.id:
        render_template('admin_portfolio.html')
    else:
        render_template('portfolio.html')

@views.route('/questions')
@views.route('/questions/<id>')
def questions(id=None):
    if id:
        question = Question.objects(id=id).first()
        render_template('question_detail.html', question=question)
    else:
        questions = Question.objects.all()
        render_template('question_index.html', questions=questions)

@views.route('/answers')
@views.route('/answers/<id>')
def answers(id=None):
    if id:
        answer = Answer.objects(id=id).first()
        render_template('answer_detail.html', answer=answer)
    else:
        answers = Answer.objects.all()
        render_template('answer_index.html', answers=answers)

# todo: MethodViews for CRUDing answers and questions