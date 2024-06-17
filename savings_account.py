"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HER
from Account.py import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE

def __init__(self, initial_balance = 0.0, interest_rate = 0.1):
     self.balance = initial_balance
     self.interest_rate = interest_rate
    # Calculate interest earned
     # ADD YOUR CODE HERE
def add_interest(self):
        interest_earned = self.interest * self.interest_rate
        self.balance += interest_earned
        return interest_earned
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
def get_updated_balance_and_interest():
 updated_balance, interest_earned = create_savings_account.get_updated_updated_balance_and_interest()

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
 create_savings_account.set_balance(updated_balance)
 print(f"New Balance (Updated Balance): ${create_savings_account.principal:.2f}")
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
 print(f"interest: {create_savings_account.interest():.2f}")

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
 return create_savings_account.balance