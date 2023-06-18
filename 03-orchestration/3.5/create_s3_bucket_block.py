from time import sleep
from prefect_aws import S3Bucket, AwsCredentials
import os


def create_aws_creds_block():
    my_aws_creds_obj = AwsCredentials(
        aws_access_key_id=os.environ["aws_access_key_id"], aws_secret_access_key=os.environ["aws_secret_access_key"]
    )
    my_aws_creds_obj.save(name="my-aws-creds", overwrite=True)


def create_s3_bucket_block():
    aws_creds = AwsCredentials.load("my-aws-creds")
    my_s3_bucket_obj = S3Bucket(
        bucket_name="zoomcamp", credentials=aws_creds
    )
    my_s3_bucket_obj.save(name="zoomcampuser", overwrite=True)


if __name__ == "__main__":
    create_aws_creds_block()
    sleep(5)
    create_s3_bucket_block()
