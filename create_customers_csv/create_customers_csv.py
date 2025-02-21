import csv

def validate_customer(customer):
    errors = []
    
    if not customer['CustomerID']:
        errors.append("Missing CustomerID")
    if not customer['Name']:
        errors.append("Missing Name")
    if not customer['Email']:
        errors.append("Missing Email")
    
    if '@' not in customer['Email']:
        errors.append("Invalid Email Format")
    
    return errors

with open('customers.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    with open('processed_customers.csv', mode='w', newline='', encoding='utf-8') as output_file:
        fieldnames = ['CustomerID', 'Name', 'Email', 'Phone', 'Status', 'Errors']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            errors = validate_customer(row)
            
            if errors:
                writer.writerow({
                    'CustomerID': row['CustomerID'],
                    'Name': row['Name'],
                    'Email': row['Email'],
                    'Phone': row['Phone'],
                    'Status': 'Exception',
                    'Errors': '; '.join(errors)
                })
            else:
                writer.writerow({
                    'CustomerID': row['CustomerID'],
                    'Name': row['Name'],
                    'Email': row['Email'],
                    'Phone': row['Phone'],
                    'Status': 'Completed',
                    'Errors': ''
                })

print("Data processing is complete. The results are written in processed_customers.csv.")