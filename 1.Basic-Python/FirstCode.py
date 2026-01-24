from flask import Flask,render_template,request
"""it creates an instance of the flask class,
which will be your WSGI (web server gateway interface)application.
"""
#WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>welcome to the flask course</H1></html>"
"""
@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'hello {name}!'
    return render_template('form.html')
"""
## building url dinamically
## variable rule
## jinja 2 template engine
'''
{{  }} expression to print output in html
{%..%} confitions,for loops
{#..#} this is for comments
'''

#variable rule
@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res= "PASSED"
    else:
        "FAILED"
    
    return render_template('result.html',results=res)

#variable rule
@app.route('/successres/<int:score>')
def successres(score):
    res=''
    if score>=50:
        res= "PASSED"
    else:
        "FAILED"
    
    exp={'score':score,"res":res}
    
    return render_template('result1.html',results=exp)





if __name__=="__main__": 
    app.run(debug=True)











