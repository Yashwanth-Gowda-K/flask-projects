from flask import Flask

app = Flask(__name__)

@app.route('/')         #Defines a route for the home page (/).
def hello_World():
    return 'Hello'

if __name__ =='__main__':
    app.run(debug=True)