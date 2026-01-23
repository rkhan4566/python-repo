from flask import Flask,render_template,request
"""it creates an instance of the flask class,
which will be your WSGI (web server gateway interface)application.
"""
#WSGI application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H1>welcome to the flask course</H1></html>"
@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'hello {name}!'
    return render_template('form.html')


if __name__=="__main__": 
    app.run(debug=True)











