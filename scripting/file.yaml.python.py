import boto3
import os
import json

session = boto3.session.Session()

regions = {}

client = boto3.client('ec2',region_name='us-east-1')
ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
for region in ec2_regions:
    print("executing region " + region)
    vs = []
    ec2_resource = session.resource('ec2', region_name=region)
    for volume in ec2_resource.volumes.filter():
        if volume.state == 'available':
            vs.append(volume.id)
    
    if len(vs) > 0:
        regions[region] = vs
        print("added " + str(len(vs)) +  "volumes for region  " + region)

# writes json to a file
with open('out.json', 'w') as out_file:
     json.dump(regions, out_file)

# writes json to a workflow variable
with open('out/workflow/out.json', 'w') as out_file:
     json.dump(regions, out_file)
