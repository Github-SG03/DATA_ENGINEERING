import boto3

def extract_from_s3(bucket_name, file_key, download_path):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, file_key, download_path)
    print(f"File {file_key} downloaded to {download_path}")