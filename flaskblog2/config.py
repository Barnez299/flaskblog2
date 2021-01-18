import os

class Config:
    SECRET_KEY = 'fb1a97349eaa6286b0d65b08bcdf6917'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456789@localhost:5432/flaskblog2'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'

    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = '**********'
    MAIL_PASSWORD = '**********'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
