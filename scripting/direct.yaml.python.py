import boto3
import os
import json

# This script prints nothing to stdout at all
# At the end we are dumping json out 
# Direktiv will pick it up as JSON response
session = boto3.session.Session()

regions = {}

client = boto3.client('ec2',region_name='us-east-1')
ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
for region in ec2_regions:
    vs = []
    ec2_resource = session.resource('ec2', region_name=region)
    for volume in ec2_resource.volumes.filter():
        if volume.state == 'available':
            vs.append(volume.id)
    
    if len(vs) > 0:
        regions[region] = vs

# print json directly to stdout
json_str = json.dumps(regions)
print(json_str)