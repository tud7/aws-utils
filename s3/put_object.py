import argparse
import os
import sys
import boto3


def main(filepath, bucket_name=None):

    if not filepath:
        raise RuntimeError("File path cannot be empty")

    if bucket_name is None:
        print("Please provide bucket_name. TODO: list all the available buckets")
        sys.exit(1)

    s3_client = boto3.client('s3')
    filename = os.path.basename(filepath)

    try:
        s3_client.upload_file(filepath, bucket_name, filename)
        
        print("INFO: %s uploaded successfully." %filename)

    except ClientError as e:
        print(e)


if __name__== "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bucket-name', help='bucket name', default=None)
    parser.add_argument('filepath',            help='full path to the file to upload')

    args = parser.parse_args()

    main(args.filepath, args.bucket_name)
