import requests
import json

apiKey = '902f8009375f89ba96ab427769c38f90'
customerList = []
merchantList = []

class Customer:
	accountList = []
	def __init__(self, name, customerID):
		self.__customerID = customerID
		self.nickname = name

	def addAccount(self, cardType, name) :
		url = 'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(self.__customerID, apiKey)

		# Account information
		account = {
			"type": cardType,
			"nickname": name,
			"rewards": 0,
			"balance": 0
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
			self.accountList.append(Account(accountID, name))
		else:
			print("Account creation failed:")
			print(r.status_code)

	def getID(self):
		return self.__customerID

class Account:
	__accountID = 0
	def __init__ (self, accountID, name):
		self.__accountID = accountID
		self.nickname = name
	
	def pushDeposit(self, amount):
		url = 'http://api.nessieisreal.com/accounts/{}/deposits?key={}'.format(self.__accountID, apiKey)

		deposit = {
			"medium": "balance",
			"amount": amount
		}

		# Post to API
		r = requests.post(
			url,
			data = json.dumps(deposit),
			headers = {'content-type':'application/json'}
		)

		# Processes response
		if r.status_code == 201:
			r_dict = r.json()
		else:
			print("Purchase failed:")
			print(r.status_code)

	def pushWithdrawal(self, amount):
		url = 'http://api.nessieisreal.com/accounts/{}/withdrawals?key={}'.format(self.__accountID, apiKey)

		withdrawal = {
			"medium": "balance",
			"amount": amount
		}

		# Post to API
		r = requests.post(
			url,
			data = json.dumps(withdrawal),
			headers = {'content-type':'application/json'}
		)

		# Processes response
		if r.status_code == 201:
			r_dict = r.json()
		else:
			print("Purchase failed:")
			print(r.status_code)

	def pushPurchase(self, merchantID, amount):
		url = 'http://api.nessieisreal.com/accounts/{}/purchases?key={}'.format(self.__accountID, apiKey)

		purchase = {
			"merchant_id": merchantID,
			"medium": "balance",
			"amount": amount
		}

		# Post to API
		r = requests.post(
			url,
			data = json.dumps(purchase),
			headers = {'content-type':'application/json'}
		)

		# Processes response
		if r.status_code == 201:
			r_dict = r.json()
		else:
			print("Purchase failed:")
			print(r.status_code)

class Merchant:
	def __init__(self, merchantID, name):
		self.name = name
		self.__merchantID = merchantID

	def getID(self):
		return self.__merchantID

def createMerchant(name, category):
	url = 'http://api.nessieisreal.com/merchants?key={}'.format(apiKey)

	merchant = {
		"name": name,
		"category": category
	}

	# Posts to API
	r = requests.post(
		url,
		data = json.dumps(merchant),
		headers = {'content-type':'application/json'}
	)
		
	# Processes response
	if r.status_code == 201:
		r_dict = r.json()
		print(r_dict['message'])
		# Gets ID from response & creates object
		merchantID = r_dict['objectCreated']['_id']
		merchantList.append(Merchant(name, fname))
	else:
		print("Merchant creation failed:")
		print(r.status_code)

def createCustomer(fname, lname):
	url = 'http://api.nessieisreal.com/customers?key={}'.format(apiKey)
	fullName = fname + " " + lname

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
		customerList.append(Customer(fullName, customerID))
	else:
		print("Customer creation failed:")
		print(r.status_code)

def deleteData(dataType):
	url = 'http://api.nessieisreal.com/data?type={}&key={}'.format(dataType, apiKey)
	r = requests.delete(url)
	if r.status_code == 204:
		print(dataType + " deleted")
