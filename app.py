from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('weather.html')


if __name__ == "__main__":
    app.run(debug=True)
