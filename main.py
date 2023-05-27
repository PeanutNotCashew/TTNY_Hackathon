import requests
import json

apiKey = '902f8009375f89ba96ab427769c38f90'
customerList = []

class Customer:
		customerID = 0;
		accounts = [];
	
		def __init__(self, customerID, nick):
				self.customerID = customerID
				self.nickname = nick

		def addAccount(self) :
				url = 'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(self.customerID, apiKey)

				# Account information
				account = {
						"type": "Credit Card",
						"nickname": "Nick",
						"rewards": 0,
						"balance": 0,
				}

				# Post to API
				r = requests.post(
						url,
						data = json.dumps(account),
						headers = {'content-type':'application/json'}
				)

				# Processes response
				if r.status_code == 201:
						r_dict = r.json()
						print(r_dict['message'])
						# Gets ID from response & creates object
						accountID = r_dict['objectCreated']['_id']
						self.accounts.append(accountID)
				else:
						print("Account creation failed:")
						print(r.status_code)

def createCustomer(fname, lname):
	url = 'http://api.nessieisreal.com/customers?key={}'.format(apiKey)

	# Customer information
	address = {
		"street_number":"8000",
		"street_name":"Utopia Pkwy",
		"city":"Jamaica",
		"state":"NY",
		"zip":"11372"
	}
	customer = {
		"first_name":fname,
		"last_name":lname,
		"address":address
	}

	# Posts to API
	r = requests.post(
		url,
		data = json.dumps(customer),
		headers = {'content-type':'application/json'}
	)
	
	# Processes response
	if r.status_code == 201:
		r_dict = r.json()
		print(r_dict['message'])
		# Gets ID from response & creates object
		customerID = r_dict['objectCreated']['_id']
		customerList.append(Customer(customerID, fname))
	else:
		print("Customer creation failed:")
		print(r.status_code)

def deleteData(dataType):
	url = 'http://api.nessieisreal.com/data?type={}&key={}'.format(dataType, apiKey)
	r = requests.delete(url)
	if r.status_code == 204:
		print(dataType + " deleted")

createCustomer("John", "Doe")
customerList[0].addAccount()

# Clears data
deleteData('Accounts')
deleteData('Customers')

