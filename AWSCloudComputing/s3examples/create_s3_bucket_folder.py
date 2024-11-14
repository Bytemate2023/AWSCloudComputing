# Create s3 bucket and folder inside using python script
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None, aws_access_key_id="", aws_secret_access_key=""):
    """
    Creates an S3 bucket in a specified region.

    Parameters:
    - bucket_name (str): The name of the S3 bucket to create.
    - region (str): AWS region where the bucket will be created (optional).
    - aws_access_key_id (str): AWS Access Key ID (optional).
    - aws_secret_access_key (str): AWS Secret Access Key (optional).
    """
    # Set up the S3 client
    s3_client = boto3.client(
        's3',
        region_name=region,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        # Create bucket
        if region is None:
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket '{bucket_name}' created successfully.")
    except ClientError as e:
        print(f"Error creating bucket: {e}")

def create_folder(bucket_name, folder_name, aws_access_key_id="", aws_secret_access_key=""):
    """
    Creates a folder in an S3 bucket by uploading an empty object with the folder name.

    Parameters:
    - bucket_name (str): The name of the S3 bucket.
    - folder_name (str): Name of the folder to create within the bucket (use 'folder_name/' format).
    - aws_access_key_id (str): AWS Access Key ID (optional).
    - aws_secret_access_key (str): AWS Secret Access Key (optional).
    """
    # Set up the S3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        # Create a "folder" by uploading an empty object with the folder name as the key
        s3_client.put_object(Bucket=bucket_name, Key=(folder_name + '/'))
        print(f"Folder '{folder_name}' created successfully in bucket '{bucket_name}'.")
    except ClientError as e:
        print(f"Error creating folder: {e}")

# Usage example
bucket_name = 'your-new-s3-bucket-name'
folder_name = 'your-folder-name'
region = 'us-west-1'  # Specify your desired AWS region
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY'
aws_secret_access_key = 'YOUR_AWS_SECRET_KEY'

# Create the bucket
create_bucket(bucket_name, region, aws_access_key_id, aws_secret_access_key)

# Create the folder inside the bucket
create_folder(bucket_name, folder_name, aws_access_key_id, aws_secret_access_key)
