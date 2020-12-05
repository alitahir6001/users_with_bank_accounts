# So if i understand this assignment correctly, we're basically combining the two differnet classes we've created so far (User Class and BankAccount Class) into one file, so that they can associate with each other.

class User:
    def __init__(self, name, email_address): # now our method has 2 parameters/aka arguments!
        self.name = name			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        # self.account_balance = 0
        # self.bank_account = bank_account
        
        
# the account balance is set to $0, so no need for a third parameter

# adding the deposit method
    
    # def make_deposit(self, amount):	# takes an argument that is the amount of the withdrawl
    #     self.account_balance += amount	# the specific user's account decreases by the amount of the value received
    #     return self # each function needs to be paired with a return statement
    
    # def make_withdrawl(self, amount): # made a separate method to increase by the amount
    #     self.account_balance -= amount
    #     return self

    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self


class BankAccount:
    def __init__(self, user, int_rate, balance): # don't forget to add some default values for these parameters!
        self.user = user
        self.int_rate = int_rate
        self.balance = balance 
        
    def deposit(self, amount):
        self.balance += amount 
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"{self.user.name} ${str(self.balance)}")
        # self.User. = name
        return self

    def yield_interest(self):
        # self.balance *=self.int_rate 
        self.balance = self.balance*self.int_rate + self.balance
        return self


# And now, to practice messing around with users and their bank accounts

# guidosbankAccount = BankAccount(0.050, 500)

# guidosbankAccount = 10
# guido = User("Guido van Rossum", "guido@python.com", BankAccount(0.050, 500))




guido_bank_account = BankAccount(
        User(name="Guido van Rossum", email_address="guido@python.com"), 
        0.050, 
        500
    )


monty_bank_account = BankAccount(
        User(name="Monty Python", email_address="monty@python.com"), 
        0.025, 
        1000
    )

ali_bank_account = BankAccount(
        User(name="Ali Tahir", email_address="alitahir6001@gmail.com"), 
        0.125, 
        2000
    )

# my_stupid_variable_that_sucks = "ali is cool"
# output = upper(my_stupid_variable_that_sucks)
# -> 
# output = upper("ali is cool")

# x = y
# z = x
# ->
# z = y



# monty = User("Monty Python", "monty@python.com", BankAccount(0.025, 1000))
# ali = User("Ali Tahir", "alitahir6001@gmail.com", BankAccount(0.125, 2000)) # tried chaining together both the User and their associated Bank Account information.



guido_bank_account.deposit(50).deposit(100).deposit(200).withdraw(25).yield_interest().display_account_info()

monty_bank_account.deposit(50).deposit(100).deposit(200).withdraw(25).yield_interest().display_account_info()

ali_bank_account.deposit(50).deposit(100).deposit(200).withdraw(25).yield_interest().display_account_info()



# guido_bank_account.deposit(50)
# guido_bank_account.deposit(100).deposit(200)
# guido_bank_account.withdraw(25)
# guido_bank_account.yield_interest()
# guido_bank_account.display_account_info(name = "Guido")





# print(guido.display_user_balance)



# What I want to do: Create a user that has an account, with a starting balance and an interest rate 
    # Then I want to make some deposits, some withdrawls, and display the updated balance with the yielded interest rate.

# What I've tried: 
    # In order to associate the two classes i've created, I tried "chaining" the Users and BankAccount classes together (line 49-51) to try and get what i want, but getting an AttributeError instead
    # Next I tried putting each class between brackets [], and separating with a comma (guido = User(["guido van Rossum", "guido@python.com"], [BankAccount(0.050, 500]) 