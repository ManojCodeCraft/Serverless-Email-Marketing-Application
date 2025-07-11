import boto3
import csv


s3_client = boto3.client('s3')
ses_client = boto3.client('ses')

def lambda_handler(event, context):
    
    bucket_name = 'apssdc-email-marketing'

    try:

        csv_file = s3_client.get_object(Bucket=bucket_name, Key='contacts.csv')
        lines = csv_file['Body'].read().decode('utf-8').splitlines()

        template_file = s3_client.get_object(Bucket=bucket_name, Key='email_template.html')
        email_html = template_file['Body'].read().decode('utf-8')

        contacts = csv.DictReader(lines)

        for contact in contacts:
            personalized_email = email_html.replace('{{FirstName}}', contact.get('FirstName', 'Friend'))
            response = ses_client.send_email(
                Source='you@yourdomainname.com',
                Destination={'ToAddresses': [contact['Email']]},
                Message={
                    'Subject': {'Data': 'Your Weekly Tiny Tales Mail!', 'Charset': 'UTF-8'},
                    'Body': {
                        'Html': {'Data': personalized_email, 'Charset': 'UTF-8'}
                    }
                }
            )

            print("Email sent to {contact['Email']}: MessageId: {response['MessageId']}")

    except Exception as e:
        print("An error occurred: {str(e)}")
