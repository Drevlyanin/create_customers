# create_customers
Processing example of processing client database.

This Python script processes customer data from a CSV file, validates the data, and writes the results to a new CSV file. It checks for missing fields (CustomerID, Name, Email) and invalid email formats (missing @ symbol). The results include the status of each record (Completed or Exception) and any error messages.

Features
Input: Reads customer data from a CSV file (customers.csv).

Validation:

Checks for missing CustomerID, Name, and Email.

Validates the format of the Email field (must contain @).

Output: Writes processed data to a new CSV file (processed_customers.csv) with the following columns:

CustomerID

Name

Email

Phone

Status (Completed or Exception)

Errors (if any)
