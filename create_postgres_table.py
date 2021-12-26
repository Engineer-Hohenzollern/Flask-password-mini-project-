# we are using SqlAlchemy ORM object-relational map) to create a Postgres table using Python classes
# Please disregard this script. I'm experiencing difficulties creating tables using ORM and classes, so I'm going to use psycopg2 and SQL queries instead . 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(

    SECRET_KEY='Antz.Ai',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:richy@localhost/password_project_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)


class user (db.Model):
    __tablename__ = 'user'

    userid = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, userid, password):
        self.userid = userid
        self.password = password

    def __repr__(self):
        return 'This is your userid  {}, your password  is {}'.format(self.userid, self.password)


if __name__ == '__main__':          # If the table does not exist in the database, it is created.
    db.create_all()
    app.run(debug=True)
