import random
from faker import Faker
import pandas as pd

# Initialize Faker with optional locale if needed
fake = Faker()

# Number of nodes and relationships
num_customers = 500_000
num_accounts = 500_000
num_transactions = 1_000_000

# Generating Customers
customers = []
for i in range(num_customers):
    try:
        customers.append({
            'customer_id': i,
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number()
        })
    except Exception as e:
        print(f"Error generating customer {i}: {e}")

# Generating Accounts
accounts = []
for i in range(num_accounts):
    try:
        accounts.append({
            'account_id': i,
            'balance': round(random.uniform(1000, 50000), 2)
        })
    except Exception as e:
        print(f"Error generating account {i}: {e}")

# Generating Transactions
transactions = []
for i in range(num_transactions):
    try:
        transactions.append({
            'transaction_id': i,
            'amount': round(random.uniform(10, 5000), 2),
            'date': fake.date_this_year(),
            'type': random.choice(['debit', 'credit'])
        })
    except Exception as e:
        print(f"Error generating transaction {i}: {e}")

# Saving CSV files to disk in the 'data' folder
pd.DataFrame(customers).to_csv('../data/customers.csv', index=False)
pd.DataFrame(accounts).to_csv('../data/accounts.csv', index=False)
pd.DataFrame(transactions).to_csv('../data/transactions.csv', index=False)

# Creating Relationships (Customer -> Account)
customer_account_rels = []
for i in range(num_accounts):
    try:
        customer_account_rels.append({
            'customer_id': random.randint(0, num_customers-1),
            'account_id': random.randint(0, num_accounts-1)
        })
    except Exception as e:
        print(f"Error generating customer-account relationship {i}: {e}")

# Creating Relationships (Transaction -> Account)
transaction_account_rels = []
for i in range(num_transactions):
    try:
        transaction_account_rels.append({
            'transaction_id': random.randint(0, num_transactions-1),
            'account_id': random.randint(0, num_accounts-1)
        })
    except Exception as e:
        print(f"Error generating transaction-account relationship {i}: {e}")

# Saving Relationship CSV files
pd.DataFrame(customer_account_rels).to_csv('../data/customer_account_rels.csv', index=False)
pd.DataFrame(transaction_account_rels).to_csv('../data/transaction_account_rels.csv', index=False)

print("Data generation completed!")
