from flask import Flask
"""it creates an instance of the flask class,
which will be your WSGI (web server gateway interface)application.
"""
#WSGI application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to this best flask course this should be an amazing course"
@app.route("/index")
def index():
    return "welcome to this index page"

if __name__=="__main__": 
    app.run(debug=True)











