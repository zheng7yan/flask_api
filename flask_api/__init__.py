from flask import Flask

from blueprints.predict import predict

app = Flask(__name__)
app.register_blueprint(predict)

