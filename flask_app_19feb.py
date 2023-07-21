#pip install flask
from flask import Flask
from flask import request

#flask is python library 
app = Flask(__name__)

@app.route("/")  #here we decorated from app
def hello_world():
    return "<h1>Hello, World!</h1>"
# here we use html for tag

@app.route("/hello_world1")  #here we decorated from app
def hello_world1():
    return "<h2>Hello, World 1!</h2>"

@app.route("/hello_world2")  #here we decorated from app
def hello_world2():
    return "<h3>Hello, World 2!</h3>"

@app.route("/test")
def test():
    a= 5+ 6
    return"This is My Function to run App. {}".format(a)
    #print("This is My Function to run App") #here print function not return 

@app.route("/test2/test2")
def test2():
    data = request.args.get('x')  # here we have to give a key.
    return "this is my data input from my url {}".format(data)
#here it try to get argument from url

if __name__=="__main__":
    app.run(host="0.0.0.0")

# when we run the code, the pythonic code will run as server for further,
# now thiis whole program will run on server.
# the url is the way to  reach server "https://gray-dentist-ucgff.pwskills.app/"
# here we are binding the server and client by @app.route and app.run(host="0.0.0.0")

