import boto3

# AWS CREDS
aws_access_key_id = ''
aws_secret_access_key = ''

# SNAPSHOT
snapshot_filename = ''
snapshot_bucket = ''
snapshot_key = ''

# DUMP
dump_filename = ''
dump_bucket = ''
dump_key = ''

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)
s3 = session.resource('s3')
# Filename - File to upload
# Bucket - Bucket to upload to (the top level directory under AWS S3)
# Key - S3 object name (can contain subdirectories). If not specified then file_name is used
s3.meta.client.download_file(Filename=snapshot_filename, Bucket=snapshot_bucket, Key=snapshot_key)
s3.meta.client.download_file(Filename=dump_filename, Bucket=dump_bucket, Key=dump_key)
print("download finished")
