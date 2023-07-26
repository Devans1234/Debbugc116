#Importing flask module in the project
from flask import Flask,render_template

#Create an object of the Flask class
app = Flask(__name__)

@app.route("/index")
def first_webpage():
    name='Flask'
    return render_template('./template/index.html',index_variable=name)

app.run(debug=True)