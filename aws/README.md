# AWS Examples

These examples should how you can communicate with AWS using the aws images. There are two examples, one is how to run a ec2 instance and the other is how to upload a file to a s3 bucket. 

These examples require the following namespace secrets to be set:

 - ACCESS_KEY
 - SECRET_ACCESS_KEY

The flow will use these secrets to configure AWS access.

## Run EC2 Instance Flow Example

This flow will create a new t2.small instance on ec2 ap-southeast-2 region. The flow uses the 'awsgo' action which executes the cli command passed in the command input property.

[Start AWS Instance](aws-run-instance.yaml)

## Upload File to S3 Bucket Example

This flow will upload a file to a S3 bucket. The file name and data are set in the input. The input property `fileData` can be a url-encoded base64 string or a standard base64 string.


[Start AWS Instance](aws-s3-upload.yaml)


```json title="Input"
{
  "fileData": "SGVsbG8sIHdvcmxkIQ==",
  "fileName": "message.txt"
}
```