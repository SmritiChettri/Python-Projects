# let's create a program that can retrieve the username and the domain name of the 

email = input("Enter your email: ").strip() # strip() removes any unwanted space on both sides of string
index = email.index("@")
username = email[:index]
domain = email[index+1:]
print(f"Email: {email}")
print(f"Your username is {username}")
print(f"Your domain is: {domain}")