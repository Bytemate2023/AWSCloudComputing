# upload files from local directory

import boto3
import os

def upload_files(directory_path, bucket_name, s3_folder):
    """
    Uploads all files from a local directory to an S3 bucket using provided AWS credentials.

    Parameters:
    - directory_path (str): Local directory path containing files to upload.
    - bucket_name (str): Target S3 bucket name.
    - s3_folder (str): Folder in the S3 bucket to upload the files to (optional).
    - aws_access_key_id (str): AWS Access Key ID.
    - aws_secret_access_key (str): AWS Secret Access Key.
    """

    # Set up the S3 client with the provided credentials
    s3_client = boto3.client(
        's3'
    )
    print("s3",directory_path)
    # List all files in the specified directory
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            # Construct the full file path
            file_path = os.path.join(root, file_name)
            print("filepath",file_path)
            
            # Define the S3 key (file path in the S3 bucket)
            s3_key = os.path.join(s3_folder, os.path.relpath(file_path, directory_path)).replace("\\",'/')
            print("s3_key", s3_key)

            try:
                # Upload the file to S3
                s3_client.upload_file(file_path, bucket_name, s3_key)
                print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
            except Exception as e:
                print(f"Error uploading {file_path}: {e}")

# Usage example
local_directory = r'C:\Users\THISPC\Desktop\project1'
bucket_name = 'rr-user-401'
s3_folder = 'folder2'  # Optional

print("working")
upload_files(local_directory, bucket_name, s3_folder)
