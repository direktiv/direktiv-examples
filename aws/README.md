# AWS Examples

These examples should how you can communicate with AWS using the aws images. There are two examples, one is how to run a ec2 instance and the other is how to upload a file to a s3 bucket. 

**NOTE:** These examples require the following namespace secrets to be set:
 - ACCESS_KEY
 - SECRET_ACCESS_KEY

The workflow will use these secrets to configure aws access.

## Run EC2 Instance Workflow Example
This workflow will create a new t2.small instance on ec2 ap-southeast-2 region. The workflow uses the 'awsgo' action which executes the cli command passed in the command input property.

### Workflow
```yaml
functions:
  - id: ec2
    image: direktiv/awsgo:v4
    type: knative-workflow

states:
  #
  # Start instance on aws ec2
  #
  - id: start-instance
    type: action
    action:
      secrets: ["ACCESS_KEY", "ACCESS_SECRET"]
      function: ec2
      input: 
        "access-key": jq(.secrets.ACCESS_KEY)
        "access-secret": jq(.secrets.ACCESS_SECRET)
        "region": "ap-southeast-2"
        command: ["ec2", "run-instances", "--image-id", "ami-07620139298af599e" ,"--instance-type", "t2.small"]
```

## Upload File to S3 Bucket Example
This workflow will upload a file to a s3 bucket. The file name and data are set in the input. The input property fileData can be a url encoded base64 string, or just a standard base64 string.

### Workflow
```yaml
functions:
  - id: s3
    image: direktiv/amazon-upload:v4
    type: knative-workflow

states:
    #
    # Validate input and extract base64 string
    #
  - id: validate-input
    type: validate
    transition: upload-file
    transform: jq(. + {fileData: .fileData | split("base64,")[-1]})
    schema:
      type: object
      required:
        - fileName
        - fileData
      properties:
        fileName:
          title: Filename
          description: Filename to be set in s3 bucket
          type: string
        fileData:
          title: File
          description: File to upload
          type: string
          format: data-url
  #
  # Upload file on aws ec2
  #
  - id: upload-file
    type: action
    action:
      function: s3
      secrets: ["AWS_ACCESS_KEY", "AWS_SECRET_KEY"]
      input:
        bucket: direktiv
        region: us-east-1
        "upload-name": "jq(.fileName)"
        data: "jq(.fileData)"
        key: "jq(.secrets.AWS_ACCESS_KEY)"
        secret: "jq(.secrets.AWS_SECRET_KEY)"
```

### Input
```json
{
  "fileData": "SGVsbG8sIHdvcmxkIQ==",
  "fileName": "message.txt"
}
```