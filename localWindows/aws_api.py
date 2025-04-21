import boto3
from mypy_boto3_ec2.client import EC2Client

ec2 = boto3.client('ec2', region_name='us-east-1')
instanceInfo = ec2.describe_instances()
infoList = []
for traverse in instanceInfo.get('Reservations', []): 
    for i in traverse.get('Instances', [] ):
        instanceId = i['InstanceId']
        instanceType = i['InstanceType']
        instanceTag = i['Tags']
        
        infoList.append(instanceId)
        infoList.append(instanceType)
        infoList.append(instanceTag)

    # print ('***********************************************')
    ## print(traverse["Instances"][0]['InstanceId']['Tags']) #Just kept filtering.. we wanted items in Instances.. then go inside the list of instances.... then value of InstanceId

print (infoList)