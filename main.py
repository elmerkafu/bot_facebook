from flask import Flask
from pymessenger.bot import Bot

app = Flask(__name__)

if __name__ == '__main__':
    app.run()