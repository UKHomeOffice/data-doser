#!/usr/bin/env python3
"""
Template functions to generate test data.
"""

import boto3
from botocore.config import Config
from logzero import logger

__author__ = "David Morris"
__version__ = "0.1.0"
__license__ = "MIT"


def push_to_s3(bucket, subfolder, kms_key, source_file, target_file):
    boto3.Session(profile_name='default')
    s3_client = boto3.resource('s3', config=Config(signature_version='s3v4'))
    logger.debug(f"""s3 details: {bucket}, {subfolder}, {type(source_file)}""")
    target_object = s3_client.Object(bucket, subfolder + target_file)
    target_object.put(Body=source_file, ServerSideEncryption="aws:kms", SSEKMSKeyId=kms_key)






