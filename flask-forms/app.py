from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date_of_birth = DateField('Date of birth')
    favourite_number = IntegerField('Favourite number')
    favourite_food = SelectField('Enter favourite food', choices = ["pizza","Spaghetti", "chilli"] )
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        date_of_birth = form.date_of_birth.data
        favourite_number = form.favourite_number.data
        favourite_food = form.favourite_food.data

        if len(first_name) == 0 or len(last_name) == 0 or date_of_birth == 0 or len(str(favourite_number)) == 0 or len(favourite_food) == 0:
            message = "Please supply all information"
        else:
            message = f'Thank you, {first_name[0:2]}{last_name[2:-2]}{date_of_birth.year}{favourite_number}{favourite_food[0:-4]}'

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')