# Banking System CLI

A command-line Banking Management System developed using Python and SQL. This project provides a simple simulation of core banking operations such as account creation, user authentication, deposits, withdrawals, balance inquiries, and transaction management through a terminal-based interface.

## Features

- Create and manage bank accounts
- Secure user authentication
- Deposit and withdraw funds
- Check account balance
- View transaction history
- SQL-based data storage
- Input validation and error handling
- Modular and maintainable code structure

## Technologies Used

- Python
- SQL (MySQL/SQLite)
- Object-Oriented Programming
- Command Line Interface (CLI)

## Project Structure

```text
banking-system/
│
├── main.py               # Application entry point
├── database.py           # Database connection and operations
├── account.py            # Account-related functionality
├── transaction.py        # Transaction processing
├── operation-auth.py     # User authentication logic
├── logger.py             # Logging and transaction records
├── utils.py              # Utility/helper functions
├── schema.sql            # Database schema
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd banking-system
```

2. Create and configure the database using the provided `schema.sql` file.

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python main.py
```

## Database

The system uses a relational database to store:

- Account information
- User credentials
- Account balances
- Transaction records

The database schema is defined in `schema.sql`.

## Core Functionalities

- Account Creation
- User Login and Authentication
- Deposit Funds
- Withdraw Funds
- Balance Inquiry
- Transaction Tracking

## Learning Objectives

This project was developed to gain practical experience with:

- Python application development
- Database connectivity
- SQL queries and data management
- Authentication workflows
- Modular software architecture
- Error handling and validation techniques

## Future Enhancements

- Password hashing and encryption
- Fund transfer between accounts
- Administrative dashboard
- Graphical User Interface (GUI)
- Interest calculation features
- Email or OTP verification