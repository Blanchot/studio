# flask_test01.py
# http://mattrichardson.com/Raspberry-Pi-Flask/

# Import module and create a flask object called 'app'
from flask import Flask
app = Flask(__name__)

# Run the code below this function when someone accesses the root URL of the server
@app.route("/")
def hello():
    return "Hello World!"

# If this script was run directly from the command line
# Have the server listen on port 80 and report any errors
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
