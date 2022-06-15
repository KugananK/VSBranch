from application import app, db
from application.models import Games

@app.route('/add/<gname>')
def add(gname):
    new_game = Games(name=gname)
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/')
@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/read/count')
def count(): 
    number_of_games = Games.query.count()
    return str(number_of_games)

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/newupdate/<oldname>/<newname>')
def newupdate(oldname, newname):
    game_to_update = Games.query.filter_by(name=oldname).first()
    game_to_update.name = newname
    db.session.commit()
    return game_to_update.name

@app.route('/delete/<gname>')
def delete(gname):
    game_to_delete = Games.query.filter_by(name=gname).first()
    db.session.delete(game_to_delete)
    db.session.commit()
    return "Removed {gname} from database"
