from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI='postgresql://localhost:5432/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)

@app.route('/index')
@app.route('/')
def hello():
    return 'Hello Flask'

@app.route('/new/')
def query_strings(greeting = 'hello'):
    q_val = request.args.get('greeting', greeting)
    return f'<h1>The greeting is: {q_val}!</h1>'

@app.route('/user/')
@app.route('/user/<name>')
def no_query_strings(name='Augie'):
    return f'<h1>Hey, {name}!'


@app.route('/template')
def rend_temp():
    return render_template('hello.html')

class Stadium(db.Model):
    __tablename__ = 'stadium'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    team = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name, team):
        self.id = id
        self.name = name
        self.team = team

    def __repr__(self):
        return f'Id: {self.id}. {self.name} is the home of the {self.team}'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
