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

# Main Code
methods.createCustomer("John", "Doe")
methods.customerList[0].addAccount("Credit Card", "Test Credit")

currentAccount = selectAccount(selectCustomer())
print(currentAccount)

# Clears data
methods.deleteData('Accounts')
methods.deleteData('Customers')
