# AWS Lambda function to perform a loss-less compression of PDF files uploaded to an S3 bucket

from PyPDF2 import PdfReader, PdfWriter
import json
import uuid
import boto3

s3 = boto3.client("s3")
account_id = boto3.client("sts").get_caller_identity().get("Account")

destination_bucket = "compressed-pdf-bucket-" + account_id


def lambda_handler(event, context):
    print(event)
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]
    final_file_name = "compressed-" + key
    print(bucket, key)
    download_path = "/tmp/{}{}".format(uuid.uuid4(), key)
    upload_path = "/tmp/{}{}".format(uuid.uuid4(), key)
    s3.download_file(bucket, key, download_path)
    compress_pdf(download_path, upload_path)
    s3.upload_file(upload_path, destination_bucket, final_file_name)
    print(f"file uploaded: {final_file_name}")


def compress_pdf(download_path, upload_path):
    reader = PdfReader(download_path)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)

    with open(upload_path, "wb") as f:
        writer.write(f)
        if not f.closed:
            f.close()
