# flask_with_template tutorial
# from: http://mattrichardson.com/Raspberry-Pi-Flask/
# Flask uses a template engine called Jinja2 so that you can use separate HTML files
# with placeholders for spots where you want dynamic data to be inserted.

# Import the PyOTA library
# from iota import Iota
# from iota import Address

# Import the flask main module and the render_template
from flask import Flask, render_template
import datetime
import requests, json

URL = 'https://min-api.cryptocompare.com/data/price?fsym=IOT&tsyms=EUR'
app = Flask(__name__)

# URL to IOTA fullnode used when checking balance
# iotaNode = "https://field.carriota.com:443"
# Create an IOTA object
# api = Iota(iotaNode, "")
# Thalia Receive address:
# address = [Address(b'RNSVVCTUYTCMZVTUAOUZUZSXKE9XZGUNAG9XNDLEKXFUDE9MSLAEQIJRFIFUCRFIZFCZNZAYFDJFQFELZMFOWWJNTD')]

# get BTC market volume using the Cryptocompare 5 MINUTE API
def get_iota_price():
  try:
    r = requests.get(URL)
    iota_price = json.loads(r.text)
    return iota_price
  except requests.ConnectionError:
    print("Error querying Cryptocompare API")


'''
# Function for checking address balance on the IOTA tangle. 
def checkbalance():
  #print("Checking balance")
  gb_result = api.get_balances(address)
  balance = gb_result['balances']
  #print('Balance is: ',balance[0])
  bal_text = 'Balance: ' + str(balance[0])
  return bal_text
'''


@app.route("/")
def hello():
  iota_price = get_iota_price()
  print(iota_price)
  now = datetime.datetime.now()
  timeString = now.strftime("%Y-%m-%d %H:%M")
  
  # Create a dictionary of variables (a set of keys, such as title that are associated with values, 
  # such as HELLO!) to pass into the template
  templateData = {
    'title' : 'THALIA',
    'time': timeString,
    'price': iota_price
    }
  # Return the main.html template to the web browser using the variables in the templateData dictionary
  return render_template('main.html', **templateData)



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)

'''
def run():
  app.run(host='0.0.0.0', port=80, debug=True)

'''
