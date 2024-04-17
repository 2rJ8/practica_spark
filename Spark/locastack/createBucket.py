import boto3

# Create an S3 client instance
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',  # LocalStack endpoint URL
    aws_access_key_id='test',  # dummy access key (LocalStack default)
    aws_secret_access_key='test',  # dummy secret key (LocalStack default)
)

# Define the bucket name
buckets=['entrada','procesado','junto']
# Create the bucket
for bucket_name in buckets:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")



# awslocal s3api list-buckets
# awslocal s3api list-objects --bucket sample-bucket