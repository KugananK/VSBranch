from flask import Flask

app = flask(__name__)

@app.route('/')
@app.route('/square/<int:number>')
def square(number):
    square_num = int(number) * int(number)
    return str(square_num)



if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)