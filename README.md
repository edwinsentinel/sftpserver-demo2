# sftpserver-demo2
This is the second attempt to demo1 above but using a microservice approach. I created the lambda function using kotlin and the services using python.

A microservice architecture to manage incoming text files would look like the following:

Moving Service: This service would be responsible for moving the files from the incoming folder to a different location for processing. This can be achieved using an AWS Lambda function triggered by an AWS S3 bucket, where the incoming text files are stored. The Lambda function can use the AWS S3 API to move the files from the incoming folder to another S3 bucket, which acts as a staging area for processing.

Processing Service: This service would be responsible for processing the text files. This can also be achieved using an AWS Lambda function triggered by the S3 bucket where the moving service places the files for processing. The Lambda function can process the text files, for example, by reading the first 20 characters and storing it in an AWS DynamoDB table.

This architecture can be implemented using Terraform by defining two AWS Lambda functions and two AWS S3 buckets, along with necessary triggers and IAM roles.



Next try the two demos on azure
