import boto3

def handler(event, context):
    # Connect to the S3 service
    s3 = boto3.client('s3')

    # Get the source bucket and key from the event
    src_bucket = event['Records'][0]['s3']['bucket']['name']
    src_key = event['Records'][0]['s3']['object']['key']

    # Read the contents of the file
    file_contents = s3.get_object(Bucket=src_bucket, Key=src_key)['Body'].read().decode('utf-8')

    # Process the first 20 characters of the file
    processed_data = file_contents[:20]

    # Store the processed data
    s3.put_object(Bucket=src_bucket, Key=f'processed/{src_key}', Body=processed_data)

    return {
        'statusCode': 200,
        'body': f'File {src_key} was processed and stored as processed/{src_key}'
    }
#the handler function is triggered by an S3 bucket and accepts an event as its input. The handler function uses the AWS S3 API to connect to the S3 service and performs the following operations:

#Retrieves the source bucket and key from the event data.
#Reads the contents of the file using the get_object method.
#Processes the first 20 characters of the file.
#Stores the processed data using the put_object method.
#Returns a response indicating the success of the operation.#