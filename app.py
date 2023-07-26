#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")  

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"

@app.route("/flask_2")  

#‘/’ URL is bound with first_flask function.
def second_flask():

    return "This is my second flask program"

#run the application on local server
app.run()
