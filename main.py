import requests
import json

apiKey = '902f8009375f89ba96ab427769c38f90'

def createCustomer():
	url = 'http://api.nessieisreal.com/customers?key={}'.format(apiKey)
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
	response = requests.post(
		url,
		data = json.dumps(customer),
		headers = {'content-type':'application/json'}
	)
	
	if response.status_code == 201:
		print('account created')
		print(response)

def getCustomers():
  url = 'http://api.nessieisreal.com/enterprise/customers?key={}'.format(apiKey)

  response = requests.post(url)
  if response.status_code == 201:
	  print('got customers')
  else:
	  print('got customers fail')
  print(response)

createCustomer()
getCustomers()