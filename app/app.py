#!/usr/bin/env python3

from flask import Flask, jsonify,request, make_response
from flask_migrate import Migrate

from models import db, Hero,Hero_Powers,Power

import datetime

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

@app.route('/heroes', methods=['GET','POST'])
def heroes():
    heroes = []
    heroes_exist = Hero.query.all()

    if not heroes_exist:
        response_content= '<h3>No heros in the database!</h3>'
        response = make_response(response_content)
        return response
    
    if request.method == 'GET':
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

@app.route('/powers')
def powers():
    powers=[]
    for item in Power.query.all():
        item_dict={
            "id":item.id,
            "name":item.name,
            "description":item.description,
        }
        powers.append(item_dict)

    resp = make_response(
        jsonify(powers),
        200
    )
    return resp    


@app.route('/powers/<int:id>')
def power_by_id(id):
    power = Power.query.filter(Power.id == id).first()
    power_object = {
        "id": power.id,
        "name": power.name,
        "description": power.description,
    }

    response = make_response(
        jsonify(power_object),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/hero_powers', methods=['GET', 'POST'])
def post_hero_powers():

    if request.method == 'POST':
        new_hero_power=Hero_Powers(
            id = request.form.get("name"),
            strength = request.form.get("super_name"),
            hero_id = request.form.get("hero_id")
        )
        db.session.add(new_hero_power)
        db.session.commit()

        hero_power_dict = new_hero_power.to_dict()

        response = make_response(
            jsonify(hero_power_dict),
            201
        )
        return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)

x = datetime.datetime.now()

hero1 = Hero(
    name = "Kim",
    super_name = "Ratman",
    created_at = x,
    updated_at = x,)

db.session.add(hero1)
db.session.commit()
