# ami-0c8eea98010057bd0

import boto3

# Initialize the EC2 client
ec2_client = boto3.client('ec2', region_name='ap-south-1')  # Change region as needed

# Define parameters for the instance
instance_params = {
    'ImageId': 'ami-01145453a182ea7ea',  # Replace with a valid AMI ID in your region
    'InstanceType': 't3.micro',         # Change instance type as needed
    'KeyName': 'test',           # Replace with your key pair name
    'MinCount': 1,
    'MaxCount': 1,
    'SecurityGroupIds': ['sg-065788f05dfdfdf'],  # Replace with a valid security group ID
    'SubnetId': 'subnet-03094a13bdfdff07'         # Optional: Replace with a valid subnet ID
}

try:
    # Create the EC2 instance
    response = ec2_client.run_instances(**instance_params)

    # Retrieve instance ID
    instance_id = response['Instances'][0]['InstanceId']
    print(f"EC2 instance created with ID: {instance_id}")

except Exception as e:
    print(f"An error occurred: {e}")
