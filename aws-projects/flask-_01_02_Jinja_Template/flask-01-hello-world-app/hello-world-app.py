from flask import Flask 
app = Flask(__name__)
@app.route('/')
def head ():
     return("Hello World")    

@app.route('/mult')
def second ():
     return("This is the second page")
@app.route('/third')     
def third ():
     return("This is the third page")
@app.route('/forth')
def forth ():
     return f'id of this page is {4*4}'
@app.route('/forth/<string:id>')
@app.route('/fifth')

def fifth ():
     return render_template("index.html")

if __name__== "__main__":

     # app.run(debug=True, port=3000)
     app.run(host= '0.0.0.0', port=80)