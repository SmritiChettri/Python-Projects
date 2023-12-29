import random
pass_len = int(input("Enter the length of the password: ")) #set how long your password is going to be
pass_value = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()<>?/[]" #set different characters
rand_choice = random.sample(pass_value, pass_len) # creates a list of random characters
password = "".join(rand_choice) #.join() converts list to a string
print(f"Your random generated password is: {password}")
