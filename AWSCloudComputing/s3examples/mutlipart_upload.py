import boto3
import math
import os
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError

def multipart_upload(bucket_name, file_path, object_name=None):
    """
    Uploads a large file to an S3 bucket using multipart upload.

    Parameters:
    - bucket_name (str): Name of the S3 bucket.
    - file_path (str): Path to the local file to be uploaded.
    - object_name (str): S3 object name (optional). If not specified, file_path will be used.
    - aws_access_key_id (str): AWS Access Key ID (optional).
    - aws_secret_access_key (str): AWS Secret Access Key (optional).
    """

    # Set up the S3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # If no object name is specified, use the file name
    if object_name is None:
        object_name = os.path.basename(file_path)

    # Configure the transfer for multipart upload
    config = TransferConfig(multipart_threshold=1024*25, multipart_chunksize=1024*25, use_threads=True)

    try:
        # Start multipart upload
        print(f"Starting multipart upload for {file_path} to bucket '{bucket_name}' as '{object_name}'...")
        s3_client.upload_file(
            Filename=file_path,
            Bucket=bucket_name,
            Key=object_name,
            Config=config
        )
        print(f"Multipart upload completed successfully.")
    except ClientError as e:
        print(f"Error during multipart upload: {e}")

# Usage example
bucket_name = 'your-s3-bucket-name'
file_path = 'path/to/your/large/video.mp4'
object_name = 'uploaded/video.mp4'  # Optional, specify the S3 key if different from file name


multipart_upload(bucket_name, file_path, object_name)
