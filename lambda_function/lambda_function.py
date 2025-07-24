import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # List all EC2 instances
    instances = ec2.describe_instances()
    print("Active EC2 Instances:")
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")

    # List all EBS snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])
    print("\nOwned EBS Snapshots:")
    for snapshot in snapshots['Snapshots']:
        print(f"Snapshot ID: {snapshot['SnapshotId']}, Volume ID: {snapshot['VolumeId']}")

    return {
        'statusCode': 200,
        'body': 'EC2 and EBS snapshot details retrieved successfully.'
    }
