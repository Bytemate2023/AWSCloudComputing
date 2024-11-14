#Move files from one s3 bucket to another s3 bucket

import boto3
from botocore.exceptions import ClientError

def move_files(source_bucket, destination_bucket, aws_access_key_id="", aws_secret_access_key=""):
    """
    Moves all files from one S3 bucket to another by copying them to the destination bucket
    and then deleting them from the source bucket.

    Parameters:
    - source_bucket (str): Name of the source S3 bucket.
    - destination_bucket (str): Name of the destination S3 bucket.
    - aws_access_key_id (str): AWS Access Key ID (optional).
    - aws_secret_access_key (str): AWS Secret Access Key (optional).
    """
    
    # Set up the S3 resource
    s3 = boto3.resource(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    
    # Get source and destination bucket objects
    src_bucket = s3.Bucket(source_bucket)
    dest_bucket = s3.Bucket(destination_bucket)

    try:
        # Iterate over each file in the source bucket
        for obj in src_bucket.objects.all():
            source_key = obj.key
            copy_source = {'Bucket': source_bucket, 'Key': source_key}
            
            # Copy the object to the destination bucket
            dest_bucket.copy(copy_source, source_key)
            print(f"Copied {source_key} to {destination_bucket}")

            # Delete the object from the source bucket
            obj.delete()
            print(f"Deleted {source_key} from {source_bucket}")

    except ClientError as e:
        print(f"Error moving files: {e}")

# Usage example
source_bucket = 'your-source-bucket'
destination_bucket = 'your-destination-bucket'
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY'
aws_secret_access_key = 'YOUR_AWS_SECRET_KEY'

move_files(source_bucket, destination_bucket, aws_access_key_id, aws_secret_access_key)
