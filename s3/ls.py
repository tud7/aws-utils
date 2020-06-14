import os
import json
import argparse
import boto3
import botocore

def main(bucket_name=None, show_bucket_only=False):

    result_dict = {}

    # Initialize Amazon S3 resource
    s3 = boto3.resource('s3')

    if bucket_name is None:
        if not show_bucket_only:
            for bucket in s3.buckets.all():
                result_dict[bucket.name] = []
                for obj in bucket.objects.all():
                    result_dict[bucket.name].append(obj.key)
    else:

        bucket = s3.Bucket(bucket_name) # this does not check if bucket exists or not

        '''
        #test if the bucket exists
        try:
            s3.meta.client.head_bucket(Bucket='bucket_name')
        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = e.response['Error']['Code']
            if error_code == '404':
                raise RuntimeError("Bucket %s does not exist" %bucket_name)
        '''

        result_dict[bucket.name] = []
        for obj in bucket.objects.all():
            result_dict[bucket.name].append(obj.key)

    return json.dumps(result_dict, indent=4)


if __name__== "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bucket-name', help='If bucket name is provided, list all objects under this bucket' \
                                             'Otherwise, list all buckets and all objects')
    parser.add_argument('--show-bucket-only',  help='Specified this flag to only show the list of buckets', \
                                             action='store_true')

    args = parser.parse_args()

    print( main(args.bucket_name, args.show_bucket_only) )
