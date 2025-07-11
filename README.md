# Serverless Email Marketing Application

This project contains an AWS Lambda function that sends personalized HTML emails using Amazon SES and contact data from a CSV file stored in S3.

## Features

- Scheduled email campaigns via Lambda
- HTML template personalization using placeholders
- CSV-based contact management
- Fully serverless and scalable

## Files

- `lambda_function/lambda_function.py`: Main Lambda function
- `lambda_function/contacts.csv`: Example CSV of contacts
- `lambda_function/email_template.html`: HTML template with placeholders (e.g., `{{FirstName}}`)
- `lambda_function/test_event.json`: Sample test event

## Deployment

1. Upload `contacts.csv` and `email_template.html` to your S3 bucket (`apssdc-email-marketing`)
2. Create a Lambda function using `lambda_function.py`
3. Add necessary permissions (S3 read, SES send)
4. Test using `test_event.json`

## Author

Safiya Sulthana
Manoj Kumar
Uday Kumar
