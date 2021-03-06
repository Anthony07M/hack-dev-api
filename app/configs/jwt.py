from flask import Flask
from flask_jwt_extended import JWTManager


def init_app(app: Flask):
    jwt = JWTManager(app)
