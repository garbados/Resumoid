from db import db
from flask_login import UserMixin

class User(db.Document, UserMixin):
    """
    Local store for some LinkedIn data, such as linkedin id
    and public profile url
    """
    # todo: flesh out set_profile and the fields it will populate
    id = db.StringField(required=True, 
            primary_key=True)

    def set_profile(self):
        """
        Retrieves the user's public profile and updates
        the model's fields with it.
        """
        pass
