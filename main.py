import methods
import setup
import sys

def selectCustomer():
	j = 1
	for i in methods.customerList:
		print(str(j) + ". " + i.nickname)
		j += 1

	j = int(input("Input number of user: "))

	return methods.customerList[j - 1]

def selectMerchant():
	j = 1
	for i in methods.merchantList:
		print(str(j) + ". " + i.nickname)
		j += 1

	j = int(input("Input number of merchant: "))

	return methods.merchantList[j - 1]

def accountActions(customer):
	print("1. Make a purchase\n2. Make a deposit\n3. Check account information\n4. Create budget\n5. Quit")
	i = int(input("Input number of action: "))

	if i == 1:
		merchant = selectMerchant()
		amount = int(input("Amount Spent: "))
		customer.postPurchase(merchant.getID(), amount)
	elif i == 2:
		amount = int(input("Amount Depositing: "))
		customer.postDeposit(amount)
	elif i == 3:
		customer.getBalance()
	elif i == 4:
		category = input("Category: ")
		limit = int(input("Limit: "))
		customer.updateBudget(category, limit)
	elif i == 5:
		# Save budgeting data
		customer.saveBudget()
		# Clear data
		dataTypes = ['Accounts', 'Bills', 'Customers', 'Deposits', 'Loans', 'Purchases', 'Transfers', 'Withdrawals']
		for i in dataTypes:
			methods.deleteData(i)
		# Delete data
		sys.exit()

	accountActions(customer)

# Main Code
customer = selectCustomer()
accountActions(customer)
