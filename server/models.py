from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    #hero_powers = db.relationship('Hero_Powers',backref='hero')

        
class Hero_Powers(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))

    @validates('strength')
    def validate_strength(self, key, value):
        if value != "Strong" or "Weak" or "Average":
            raise ValueError("invalid strength attribute")
        return value


class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    @validates('description')
    def validate_description(self, key, value):
        if value == "":
            raise ValueError("Powers must have a description")
        return value
   

# add any models you may need. 