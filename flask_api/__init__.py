from flask import Flask

from flask_api.blueprints.predict import predict

app = Flask(__name__)
app.register_blueprint(predict)

