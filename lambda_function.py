import boto3
import csv
import re

# Initialize the boto3 client
s3_client = boto3.client('s3')
ses_client = boto3.client('ses')

def is_valid_email(email):
    """Check if the given email address is valid."""
    email_regex = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def lambda_handler(event, context):
    # Specify the S3 bucket name
    bucket_name = 'temail-marketing' # Replace with your bucket name

    try:
        # Retrieve the CSV file from S3
        csv_file = s3_client.get_object(Bucket=bucket_name, Key='contacts.csv')
        lines = csv_file['Body'].read().decode('utf-8').splitlines()
        
        # Retrieve the HTML email template from S3
        email_template = s3_client.get_object(Bucket=bucket_name, Key='email_template.html')
        email_html = email_template['Body'].read().decode('utf-8')
        
        # Parse the CSV file
        contacts = csv.DictReader(lines)
        
        for contact in contacts:
            # Strip leading and trailing spaces from keys
            contact = {key.strip(): value for key, value in contact.items()}
            print("Current Contact:", contact)
            try:
                email_address = contact.get('Email', '').strip() # Remove leading/trailing whitespace
                if not email_address:
                    raise ValueError("Email address is empty or missing")
                if not is_valid_email(email_address):
                    raise ValueError(f"Invalid email address: {email_address}")
                
                personalized_email = email_html.replace('{{FirstName}}', contact['FirstName'])
                response = ses_client.send_email(
                    Source='Manasapothakamuru@csu.fullerton.edu', # Replace with your verified "From" address
                    Destination={'ToAddresses': [email_address]},
                    Message={
                        'Subject': {'Data': 'Your Weekly Tiny Tales Mail!', 'Charset': 'UTF-8'},
                        'Body': {'Html': {'Data': personalized_email, 'Charset': 'UTF-8'}}
                    }
                )
                print(f"Email sent to {email_address}: Response {response}")
            except ValueError as ve:
                print(f"An error occurred: {ve}")
            except Exception as e:
                print(f"An error occurred: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()