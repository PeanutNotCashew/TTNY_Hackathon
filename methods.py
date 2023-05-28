import requests
import json

apiKey = '902f8009375f89ba96ab427769c38f90'
customerList = []
merchantList = []

class Customer:
	def __init__(self, name, customerID, accountID):
		self.__customerID = customerID
		self.nickname = name
		self.__accountID = accountID

		# Load budget
		try:
			with open('budget.json', 'r') as file:
				budgets = json.load(file)
		except FileNotFoundError:
			budgets = {}
		self.budgets = budgets

	def postDeposit(self, amount):
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
		if r.status_code != 201:
			print("Deposit failed:")
			print(r.status_code)

	def postPurchase(self, merchantID, amount):
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
			url = 'http://api.nessieisreal.com/merchants/{}?key={}'.format(merchantID, apiKey)

			# Post to API
			r = requests.get(url)
			if r.status_code == 200:
				r_dict = r.json()
				category = r_dict['category']
				if category in self.budgets:
					limit = self.budgets[category]
					if amount > limit:
						print(f'Warning: You are exceeding the budget limit for {category}.')
				else:
					print(f'Warning: No budget limit set for category {category}.')
		else:
			print("Purchase failed:")
			print(r.status_code)

	def getBalance(self):
		url = 'http://api.nessieisreal.com/accounts/{}?key={}'.format(self.__accountID, apiKey)
		# Post to API
		r = requests.get(url)
		# Processes response
		if r.status_code == 200:
			r_dict = r.json()
			print("Balance: " + str(r_dict['balance']))
		else:
			print(r.text)
			print("Get balance failed:")
			print(r.status_code)

	def updateBudget(self, category, limit):
		if category in self.budgets:
			self.budgets[category] = limit
		else:
			newBudget = {category:limit}
			self.budgets.update(newBudget)

	def saveBudget(self):
		with open('budget.json', 'w') as file:
			json.dump(self.budgets, file)

class Merchant:
	def __init__(self, name, merchantID):
		self.nickname = name
		self.__merchantID = merchantID

	def getID(self):
		return self.__merchantID
	
	def getCategory(self):
		url = 'http://api.nessieisreal.com/merchants/{}?key={}'.format(self.__merchantID, apiKey)

		r = requests.get(url)

		# Processes response
		if r.status_code == 201:
			r_dict = r.json()
			print(r_dict['message'])
			# Gets ID from response & creates object
			return r_dict['category']
		else:
			print("Merchant ID retrieval failed:")
			print(r.status_code)

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
		merchantList.append(Merchant(name, merchantID))
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
		accountID = createAccount(customerID)
		if accountID != "failed":
			customerList.append(Customer(fullName, customerID, accountID))
			print("Your customer ID is " + customerID)
			print("Your account ID is " + accountID)
	else:
		print("Customer creation failed:")
		print(r.status_code)

def createAccount(customerID):
	# Create banking account
	url = 'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(customerID, apiKey)
	# Account information
	account = {
		"type": "Checking",
		"nickname": "Checking",
		"rewards": 0,
		"balance": 100
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
		return r_dict['objectCreated']['_id']
	else:
		print("Account creation failed:")
		print(r.status_code)
		return "failed"

def deleteData(dataType):
	url = 'http://api.nessieisreal.com/data?type={}&key={}'.format(dataType, apiKey)
	r = requests.delete(url)
	if r.status_code == 204:
		print(dataType + " deleted")
