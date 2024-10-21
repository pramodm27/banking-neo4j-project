// Load Customers
LOAD CSV WITH HEADERS FROM 'file:///customers.csv' AS row
CREATE (:Customer {id: row.customer_id, name: row.name, email: row.email, phone: row.phone});

// Load Accounts
LOAD CSV WITH HEADERS FROM 'file:///accounts.csv' AS row
CREATE (:Account {id: row.account_id, balance: row.balance});

// Load Transactions
LOAD CSV WITH HEADERS FROM 'file:///transactions.csv' AS row
CREATE (:Transaction {id: row.transaction_id, amount: row.amount, date: row.date, type: row.type});

// Load Customer-Account Relationships
LOAD CSV WITH HEADERS FROM 'file:///customer_account_rels.csv' AS row
MATCH (c:Customer {id: row.customer_id}), (a:Account {id: row.account_id})
CREATE (c)-[:OWNS]->(a);

// Load Transaction-Account Relationships
LOAD CSV WITH HEADERS FROM 'file:///transaction_account_rels.csv' AS row
MATCH (t:Transaction {id: row.transaction_id}), (a:Account {id: row.account_id})
CREATE (t)-[:FROM]->(a);
