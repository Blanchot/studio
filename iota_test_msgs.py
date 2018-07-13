# iota_test_msgs.py
# using pyota to read messages
# https://iota.stackexchange.com/questions/1708/how-to-find-all-the-messages-of-the-txs-of-an-address/1788

# Imports the PyOTA library
from iota import Iota
from iota import Address
from iota.commands.extended.utils import find_transaction_objects

# Thalia Receive address
list_add = [Address('RNSVVCTUYTCMZVTUAOUZUZSXKE9XZGUNAG9XNDLEKXFUDE9MSLAEQIJRFIFUCRFIZFCZNZAYFDJFQFELZMFOWWJNTD')]

'''
A: There's a utility function called find_transaction_objects (that will be added to the main API soon) that may be useful here. It does the same thing as find_transactions, except it then converts the trytes that the IRI sends back into proper iota.transaction.base.Transaction objects. Once you have Transaction objects, you can access each one's signature_message_fragment (which is an iota.types.TryteString object) and decode it:
'''

transactions = find_transaction_objects(addresses=list_add)

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


