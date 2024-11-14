# download files from s3 to local machine
import boto3
import os

def download_files(bucket_name, s3_folder, local_dir, aws_access_key_id="", aws_secret_access_key=""):
    """
    Downloads all files from an S3 bucket folder to a local directory.

    Parameters:
    - bucket_name (str): The name of the S3 bucket.
    - s3_folder (str): Folder in the S3 bucket to download files from.
    - local_dir (str): Local directory to download the files to.
    - aws_access_key_id (str): AWS Access Key ID (optional).
    - aws_secret_access_key (str): AWS Secret Access Key (optional).
    """

    # Set up the S3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Ensure local directory exists
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # List all objects in the specified S3 folder
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=s3_folder)
    if 'Contents' in response:
        for obj in response['Contents']:
            # Define the local file path
            s3_key = obj['Key']
            local_file_path = os.path.join(local_dir, os.path.relpath(s3_key, s3_folder))

            # Ensure the local directory for the file exists
            local_file_dir = os.path.dirname(local_file_path)
            if not os.path.exists(local_file_dir):
                os.makedirs(local_file_dir)

            # Download the file
            try:
                s3_client.download_file(bucket_name, s3_key, local_file_path)
                print(f"Downloaded {s3_key} to {local_file_path}")
            except Exception as e:
                print(f"Error downloading {s3_key}: {e}")
    else:
        print("No files found in the specified S3 folder.")

# Usage example
bucket_name = 'your-s3-bucket-name'
s3_folder = 'your/s3/folder'  # Folder in the S3 bucket
local_directory = 'path/to/local/directory'
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY'
aws_secret_access_key = 'YOUR_AWS_SECRET_KEY'

download_files(bucket_name, s3_folder, local_directory, aws_access_key_id, aws_secret_access_key)
