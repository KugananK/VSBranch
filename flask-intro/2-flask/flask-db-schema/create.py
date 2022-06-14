from app import db, Users, Games

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
db.session.add(testuser)
db.session.commit()

testgame = Games(game_name='Borderlands', gore=True)
db.session.add(testgame)
db.session.commit()