from flask import flask 

application = flask (__name__)

@application.route('/')
def home():
    return "hello"

if__name__=="__main__"
  application.run(debug=true)    