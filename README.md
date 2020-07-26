# banking-system

## Database (models + relations):

### Client:

National ID (primary key, 14 characters, numbers only),<br>
Name,<br>
Phone number

### Account:

ID,<br>
Balance,<br>
Client National ID

## Functionality:

### Accounts:

Creation,<br>
Deposit (update),<br>
Withdraw (update),<br>
Transfer between accounts (2 updates),<br>
Delete

### Clients:

Creation,<br>
Delete (2 deletions -> client + account),<br>
Display list of accounts
