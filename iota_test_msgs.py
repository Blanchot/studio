# iota_test_msgs.py
# using pyota to read messages
# https://iota.stackexchange.com/questions/1708/how-to-find-all-the-messages-of-the-txs-of-an-address/1788

# Imports the PyOTA library
from iota import Iota
from iota import Address, Transaction
from iota.commands.extended.utils import find_transaction_objects
from iota.adapter import HttpAdapter #trying this 

api = Iota(HttpAdapter('https://field.carriota.com:443'))

'''
help(find_transaction_ojbects)
find_transaction_objects(adapter, **kwargs)
    Finds transactions matching the specified criteria, fetches the
    corresponding trytes and converts them into Transaction objects.  
'''
'''
iotaNode = "https://field.carriota.com:443"
# Create an IOTA object
# api = Iota(iotaNode, "")
api = Iota(iotaNode)
# Thalia Receive address:
#address = [Address(b'RNSVVCTUYTCMZVTUAOUZUZSXKE9XZGUNAG9XNDLEKXFUDE9MSLAEQIJRFIFUCRFIZFCZNZAYFDJFQFELZMFOWWJNTD')]
'''

# Thalia Receive address
list_add = [Address(b'RNSVVCTUYTCMZVTUAOUZUZSXKE9XZGUNAG9XNDLEKXFUDE9MSLAEQIJRFIFUCRFIZFCZNZAYFDJFQFELZMFOWWJNTD')]

'''
A: There's a utility function called find_transaction_objects (that will be added to the main API soon) that may be useful here. It does the same thing as find_transactions, except it then converts the trytes that the IRI sends back into proper iota.transaction.base.Transaction objects. Once you have Transaction objects, you can access each one's signature_message_fragment (which is an iota.types.TryteString object) and decode it:
'''

# transactions = api.find_transaction_objects(addresses=list_add)
transactions = find_transaction_objects(api, addresses=list_add)

for transaction in transactions:
  # Ignore input transactions; these have cryptographic signatures,
  # not human-readable messages.
  if transaction.value < 0:
    continue
  #print(f'Message from {transaction.hash}:')
  print('Message from: ',transaction.hash)
  message = transaction.signature_message_fragment
  if message is None:
    print('(None)')
  else:
    print(message.decode())


