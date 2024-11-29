# Delete s3 bucket and folders inside
import boto3
from botocore.exceptions import ClientError

def delete_bucket(bucket_name):
    """
    Deletes an S3 bucket along with all its contents.

    Parameters:
    - bucket_name (str): The name of the S3 bucket to delete.
    - aws_access_key_id (str): AWS Access Key ID (optional).
    - aws_secret_access_key (str): AWS Secret Access Key (optional).
    """
    # Set up the S3 resource
    s3 = boto3.resource(
        's3'
    )
    
    try:
        # Get the bucket
        bucket = s3.Bucket(bucket_name)

        # Delete all objects in the bucket
        bucket.objects.all().delete()
        print(f"All objects in bucket '{bucket_name}' have been deleted.")
        
        # Delete the bucket itself
        bucket.delete()
        print(f"Bucket '{bucket_name}' has been deleted successfully.")
        
    except ClientError as e:
        print(f"Error deleting bucket or its contents: {e}")

# Usage example
bucket_name = 'your-s3-bucket-name'


delete_bucket(bucket_name)
