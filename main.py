import requests
import json

apiKey = '902f8009375f89ba96ab427769c38f90'
customers = []

class Customer:
    customerID = 0;
    accounts = [];

    def __init__(self, customerID):
        self.customerID = customerID

    def addAccount() :
        url = 'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(customerID, apiKey)

        # Account information
        account = {
            "type": "Credit Card",
            "nickname": "",
            "rewards": 0,
            "balance": 0,
            "account_number": "string"
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
            accounts.append(accountID)
        else:
            print(Account creation failed:)
            print(r.status_code)

def createCustomer():
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
		"first_name":"John",
		"last_name":"Doe",
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
		customers.append(Customer(customerID))
    else:
        print(Account creation failed:)
        print(r.status_code)

createCustomer()