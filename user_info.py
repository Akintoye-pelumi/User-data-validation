import random
import string 

def user_details():
	firstname = input("Enter your firstname: ")
	lastname = input("Enter your lastname: ")
	useremail = input("Enter your email address: ")

	details = {'firstname': firstname,'lastname': lastname,'email': useremail,}

	return details


def gen_password(user_details):
	letters = string.ascii_lowercase
	length = 5
	random_password = ''.join(random.choice(letters) for i in range(length))
	password = str(details["firstname"][0:2] + details["lastname"][-2:] + random_password)

	return password

status = True
container = {}

while status:

	details = user_details()
	password = gen_password(details)
	print ("your password is: " +str(password))

	password_like = input(str("Do you like the generated password? if yes, enter Yes, if no, enter No and enter your preferred password "))

	password_loop = True

	while password_loop:
		if password_like == "Yes":
			details.append(password)

			container.append(details)

			password_loop = False

		else:
			user_password = input(str("Enter your preferred password, it must be at least 7 characters "))

			pass_lenght = True

			while pass_lenght:
				if len(user_password) >= 7:
					details.append(user_password)
					container.append(details)

					pass_lenght = False
					password_loop = False
				else:
					print ("Your password is less than 7")
					user_password = inpu(str("Enter a password equal or longer than 7"))

	new_user = input(str("Will you like to input new user details? "))
	if (new_user == "no"):
		status = False
		for items in container:
			print(items)

	else:
		status = True


		



				


		







