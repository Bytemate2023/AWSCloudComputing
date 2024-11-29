import boto3

def delete_all_buckets():
    s3 = boto3.resource('s3')
    client = boto3.client('s3')

    for bucket in s3.buckets.all():
        print(f"Deleting contents of bucket: {bucket.name}")
        bucket.objects.all().delete()
        bucket.object_versions.all().delete()

        print(f"Deleting bucket: {bucket.name}")
        client.delete_bucket(Bucket=bucket.name)

    print("All buckets deleted!")

# Run the script
delete_all_buckets()
