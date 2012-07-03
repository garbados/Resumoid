"""
File from which all database-related files should import from, as it sets up
the database connection, and other pre-work business.
"""
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()
db.connect('resumoid_db')
