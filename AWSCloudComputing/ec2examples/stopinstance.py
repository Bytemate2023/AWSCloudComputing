import boto3

# Initialize the EC2 client
ec2_client = boto3.client('ec2', region_name='ap-south-1')  # Replace with your region

def stop_instance(instance_id):
    try:
        print(f"Stopping instance {instance_id}...")
        response = ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} is stopping. Current state: {response['StoppingInstances'][0]['CurrentState']['Name']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'instance-id' with your EC2 instance ID
stop_instance('i-0085c9aa3e9546b36')
