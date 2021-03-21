from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Property(db.Model):
    
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    bedRoom_number = db.Column(db.String(80))
    bathRoom_number = db.Column(db.String(80))
    location = db.Column(db.String(200))
    price = db.Column(db.String(250))
    property_type = db.Column(db.String(80))
    description = db.Column(db.String(800))
    image = db.Column(db.String(80))


    def __init__(self,title,bedRoom_number,bathRoom_number,location,price,property_type,description,image):
        self.title
        self.bedRoom_number
        self.bathRoom_number
        self.location
        self.price
        self.property_type
        self.description
        self.image
        


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)