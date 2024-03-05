from ib_insync import IB, Future, MarketOrder
from pprint import pprint
# Create an IB object
ib = IB()

# Connect to the IB Gateway or TWS (replace with your connection details)
ib.connect("127.0.0.1", 7496, clientId=1)

#
fut=Future(symbol="ES",lastTradeDateOrContractMonth="20241220",exchange="CME")

order = MarketOrder("BUY", 1)
trade = ib.placeOrder(fut, order)

print(trade)


# # Disconnect from the IB Gateway or TWS
# ib.disconnect()
import random

# Generate a random integer between 1 and 10000
random_number = random.randint(1, 10000)
print(random_number)