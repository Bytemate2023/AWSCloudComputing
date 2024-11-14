# Archive old buckets
import boto3
from datetime import datetime, timedelta
from botocore.exceptions import ClientError

def archive_old_buckets(archive_bucket_name, days_old=365, aws_access_key_id="", aws_secret_access_key=""):
    """
    Archives old S3 buckets by moving their contents to a designated archive bucket
    and then deleting the old buckets.

    Parameters:
    - archive_bucket_name (str): Name of the archive S3 bucket.
    - days_old (int): Number of days to consider a bucket "old".
    - aws_access_key_id (str): AWS Access Key ID (optional).
    - aws_secret_access_key (str): AWS Secret Access Key (optional).
    """
    
    # Initialize the S3 resource
    s3 = boto3.resource(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Calculate the threshold date for old buckets
    threshold_date = datetime.now() - timedelta(days=days_old)

    try:
        # List all S3 buckets
        for bucket in s3.buckets.all():
            # Check bucket creation date
            bucket_creation_date = bucket.creation_date
            if bucket_creation_date < threshold_date:
                print(f"Archiving bucket: {bucket.name} (Created on {bucket_creation_date})")

                # Move all objects to the archive bucket
                for obj in bucket.objects.all():
                    archive_key = f"{bucket.name}/{obj.key}"  # Preserve original bucket structure in archive
                    copy_source = {'Bucket': bucket.name, 'Key': obj.key}
                    s3.Bucket(archive_bucket_name).copy(copy_source, archive_key)
                    print(f"Copied {obj.key} to {archive_bucket_name}/{archive_key}")

                # Delete all objects in the old bucket
                bucket.objects.all().delete()
                print(f"All objects in bucket '{bucket.name}' have been deleted.")

                # Delete the old bucket
                bucket.delete()
                print(f"Bucket '{bucket.name}' has been deleted.")
            else:
                print(f"Bucket '{bucket.name}' is not older than {days_old} days; skipping.")

    except ClientError as e:
        print(f"Error archiving buckets: {e}")

# Usage example
archive_bucket_name = 'your-archive-bucket'
days_old = 365  # Archive buckets older than 1 year
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY'
aws_secret_access_key = 'YOUR_AWS_SECRET_KEY'

archive_old_buckets(archive_bucket_name, days_old, aws_access_key_id, aws_secret_access_key)
