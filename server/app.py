from flask import Flask
from flask_migrate import Migrate
import os
from models import db

app = Flask(__name__)

# Configuration management
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>404 - Not Found</h1>', 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
