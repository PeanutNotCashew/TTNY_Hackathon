import methods

def selectCustomer():
	j = 1
	for i in methods.customerList:
		print(str(j) + ". " + i.nickname)
		j += 1

	j = int(input("Input number of user: "))

	return methods.customerList[j - 1]

def selectAccount(user):
	i = 1
	for j in user.accountList:
		print(str(i) + ". " + j.nickname)
		i += 1

	j = int(input("Input number of account: "))

	return user.accountList[j - 1]

def selectMerchant()
	j = 1
	for i in methods.merchantList:
		print(str(j) + ". " + i.nickname)
		j += 1

	j = int(input("Input number of merchant: "))

	return methods.merchantList[j - 1]

def accountActions(account):
	print("1. Make a purchase\n2. Make a deposit\n3. Make a withdrawal")
	i = int(input("Input number of action: "))

	if i == 1:
		merchant = selectMerchant()
		amount = int(input("Amount Spent: "))
		account.pushPurchase(merchant.getID(), amount)
	elif i == 2:
		amount = int(input("Amount Depositing: "))
		account.pushDeposit(amount)
	elif i == 3:
		amount = int(input("Amount withdrawing: "))
		account.pushWithdrawal(amount)

# Main Code
methods.createCustomer("John", "Doe")
methods.customerList[0].addAccount("Credit Card", "Test Credit")
methods.createMerchant("H&M", "Clothing")

currentUser = selectCustomer()
currentAccount = selectAccount(currentUser)
accountActions(currentAccount)
print(currentAccount)

# Clears data
methods.deleteData('Accounts')
methods.deleteData('Customers')
