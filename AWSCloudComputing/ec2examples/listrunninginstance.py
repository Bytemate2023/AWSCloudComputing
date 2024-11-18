import boto3
def list_running_instances():
    ec2_client = boto3.client('ec2', region_name='ap-south-1')  # Replace with your region
    try:
        response = ec2_client.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
    except Exception as e:
        print(f"An error occurred: {e}")

list_running_instances()
