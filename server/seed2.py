from random import choice as rc
from app import app 
from models import Hero,Hero_Powers,Power,db
import datetime


""" powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]

heroes_data = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
]

strengths = ["Strong", "Weak", "Average"]

with app.app_context():
    # Deleting existing data
    Hero_Powers.query.delete()
    Power.query.delete()
    Hero.query.delete()

    # Seeding powers
    for power in powers_data:
        p = Power(name=power["name"], description=power["description"])
        db.session.add(p)

    db.session.commit()
    print("🦸‍♀️ Seeded powers...")

    # Seeding heroes
    for hero in heroes_data:
        h = Hero(name=hero["name"], super_name=hero["super_name"])
        db.session.add(h)

    db.session.commit()
    print("🦸‍♀️ Seeded heroes...")

    # Adding powers to heroes
    all_heroes = Hero.query.all()
    all_powers = Power.query.all()

    for hero in all_heroes:
        for _ in range(rc([1, 2, 3])):
            power = rc(all_powers)
            strength = rc(strengths)
            hp = Hero_Powers(hero_id=hero.id, power_id=power.id, strength=strength)
            db.session.add(hp)

    db.session.commit()
    print("🦸‍♀️ Added powers to heroes...") """


heroes_data = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
]

powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]


with app.app_context():
    # Deleting existing data
    Hero_Powers.query.delete()
    Power.query.delete()
    Hero.query.delete()

    x = datetime.datetime.now()

    for hero in heroes_data:
        h = Hero(name=hero["name"], super_name=hero["super_name"],created_at=x,updated_at=x)
        db.session.add(h)

    for power in powers_data:
        p = Power(name=power["name"], description=power["description"])
        db.session.add(p)    


    db.session.commit()    

"""     hero1 = Hero(
        name = "Kamala Khan",
        super_name = "Ms. Marvel",
        created_at = x,
        updated_at = x,
    ) """
    

print("🦸‍♀️ Done seeding!")