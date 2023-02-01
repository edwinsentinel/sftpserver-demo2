import boto3

def handler(event, context):
    # Connect to the S3 service
    s3 = boto3.client('s3')
    
    # Get the source and destination buckets and keys from the event
    src_bucket = event['Records'][0]['s3']['bucket']['name']
    src_key = event['Records'][0]['s3']['object']['key']
    dest_bucket = "destination-bucket"
    dest_key = src_key

    # Copy the file from the source bucket to the destination bucket
    copy_source = {'Bucket': src_bucket, 'Key': src_key}
    s3.copy_object(Bucket=dest_bucket, CopySource=copy_source, Key=dest_key)

    # Delete the file from the source bucket
    s3.delete_object(Bucket=src_bucket, Key=src_key)

    return {
        'statusCode': 200,
        'body': f'File {src_key} was moved from {src_bucket} to {dest_bucket}'
    }

    #the handler function is triggered by an S3 bucket and accepts an event as its input. The handler function uses the AWS S3 API to connect to the S3 service and performs the following operations:

#Retrieves the source and destination buckets and keys from the event data.
#Copies the file from the source bucket to the destination bucket using the copy_object method.
#Deletes the file from the source bucket using the delete_object method.
#Returns a response indicating the success of the operation.
