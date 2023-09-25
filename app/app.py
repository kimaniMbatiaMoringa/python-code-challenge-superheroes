#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate

from models import db, Hero,Hero_Powers,Power

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def request():
    response =make_response(
        '<h4>Request is working</h4>'
    )
    return response

@app.route('/heroes')
def heroes():
    heroes = []
    heroes_exist = Hero.query.all()

    if not heroes_exist:
        response_content= '<h3>No heros in the database!</h3>'
        response = make_response(response_content)
        return response
    
    for hero in Hero.query.all():
        hero_dict={
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            #"created_at": hero.created_at,
            #"updated_at": hero.updated_at
        }
        heroes.append(hero_dict)
    response = make_response(
        '<h1>Parse Hero JSON here</h1>',
        jsonify(heroes),
        200
    )
    return response

@app.route('/heroes/<int:id>')
def heroes_by_id(id):
    hero = Hero.query.filter(Hero.id == id).first()

#    hero_powers = Hero_Powers.query.filter(Hero_Powers.hero_id == id)

    hero_object = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
#        "powers": [
#            {
#                "id": hero_powers.id,
#                "name": hero_powers.strength,
#                "description": "gives the wielder super-human strengths"
#            },
#            {
#                "id": 2,
#                "name": "flight",
#                "description": "gives the wielder the ability to fly through the skies at supersonic speed"
#            }
#        ]
    }

    response = make_response(
        jsonify(hero_object),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response



if __name__ == '__main__':
    app.run(port=5555, debug=True)


#hero1 = Hero()
