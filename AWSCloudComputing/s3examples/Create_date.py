#Create folders based on yyyy/mm/dd

import boto3
from datetime import datetime
from botocore.exceptions import ClientError

def create_date_based_folder(bucket_name):
    """
    Creates a folder structure in an S3 bucket based on the current date (yyyy/mm/dd).

    Parameters:
    - bucket_name (str): The name of the S3 bucket.
    - aws_access_key_id (str): AWS Access Key ID (optional).
    - aws_secret_access_key (str): AWS Secret Access Key (optional).
    """

    # Get the current date and format it as yyyy/mm/dd
    date_folder = datetime.now().strftime("%Y/%m/%d/")

    # Set up the S3 client
    s3_client = boto3.client(
        's3'
    )

    try:
        # Create the date-based folder by uploading an empty object
        s3_client.put_object(Bucket=bucket_name, Key=date_folder)
        print(f"Folder '{date_folder}' created successfully in bucket '{bucket_name}'.")
    except ClientError as e:
        print(f"Error creating folder: {e}")

# Usage example
bucket_name = 'your-s3-bucket-name'


create_date_based_folder(bucket_name)
