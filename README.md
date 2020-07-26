# banking-system

## Database (models + relations):

### Client:

National ID (primary key, 14 characters, numbers only),<br>
Name,
Phone number

### Account:

ID,
Balance,
Client National ID

## Functionality:

### Accounts:

Creation,
Deposit (update),
Withdraw (update),
Transfer between accounts (2 updates),
Delete

### Clients:

Creation,
Delete (2 deletions -> client + account),
Display list of accounts
