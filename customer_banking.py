
# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
# from cd_account import create_cd_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance =  input("Enter your starting Savings Balance: ")
    savings_interest = input("Set your expected interest rate: ")
    savings_maturity = input("Enter the number of months: ")
    print(savings_balance)



    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print(updated_savings_balance)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Updated savings balance: {savings_balance}, Interest earned: {interest_earned}")
    
    cd_balance = input("Enter your starting CD Balance: ")
    cd_interest = input("Set your expected interest rate: ")
    cd_maturity = input("Enter the number of months: ")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Updated CD balance: {cd_balance}, Interest earned: {interest_earned}")
if __name__ == "__main__":
    # Call the main function.
    main()
