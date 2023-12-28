from ib_insync import IB, Future, MarketOrder
from pprint import pprint
# Create an IB object
ib = IB()

# Connect to the IB Gateway or TWS (replace with your connection details)
ib.connect("127.0.0.1", 7496, clientId=1)

# Define the contract for E-mini S&P 500 futures (ES)
# es_contract = Future("ES","SMART")
# print(es_contract)

# # Qualify the contract to get all available contracts for the symbol
# contracts = ib.qualifyContracts(es_contract)
fut=Future(symbol="ES",lastTradeDateOrContractMonth="20241220",exchange="CME")

order = MarketOrder("BUY", 1)
trade = ib.placeOrder(fut, order)
# ib.waitFill(trade)

# Print the trade details
print(trade)
# pprint(contracts)
# pprint(list(contracts))

# pprint(contracts[0])
# contract=Future(symbol="ES",)
# # Display the details for each contract
# for contract in contracts:
#     print(contract)

# # Disconnect from the IB Gateway or TWS
# ib.disconnect()
