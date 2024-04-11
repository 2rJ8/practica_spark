import boto3

# Configure boto3 to use LocalStack endpoint
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',  # dummy access key
    aws_secret_access_key='test',  # dummy secret key
)

# Define the bucket name
bucket_name = 'new-sample-bucket'

# Define the object key and data
object_key = 'example_data.txt'
data = b'Hello, LocalStack S3!'

# Upload data to S3 bucket
s3.put_object(Bucket=bucket_name, Key=object_key, Body=data)

print(f"Data uploaded to s3://{bucket_name}/{object_key}")
