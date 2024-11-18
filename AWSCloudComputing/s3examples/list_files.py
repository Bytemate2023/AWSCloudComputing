import boto3

def list_files(bucket_name, s3_folder):
    """
    Lists all files in a specified S3 bucket folder.

    Parameters:
    - bucket_name (str): The name of the S3 bucket.
    - s3_folder (str): Folder in the S3 bucket to list files from.
    - aws_access_key_id (str): AWS Access Key ID (optional).
    - aws_secret_access_key (str): AWS Secret Access Key (optional).

    Returns:
    - list: A list of file keys in the specified S3 folder.
    """

    # Set up the S3 client
    s3_client = boto3.client(
        's3'
       
    )

    # List all objects in the specified S3 folder
    file_keys = []
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=s3_folder)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            file_keys.append(obj['Key'])
            print(obj['Key'])  # Print each file key
    else:
        print("No files found in the specified S3 folder.")

    return file_keys

# Usage example
bucket_name = 'your-s3-bucket-name'
s3_folder = 'your/s3/folder/'  # Folder in the S3 bucket


file_keys = list_files(bucket_name, s3_folder)
