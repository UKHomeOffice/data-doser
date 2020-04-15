#!/usr/bin/env python3
"""
Template functions to generate test data.
"""

__author__ = "David Morris"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
from logzero import logger
import time
import xtemplate
import xs3
import xscarymaths


def do_a_chunk(args, chunk_number, bag_o_random, values):
    logger.debug(f"""doing chunk: {chunk_number}""")
    file_number = 0
    for random_time in bag_o_random:
        if args.mode == 'random_delay':
            logger.debug(f"""Sleeping for {random_time}""")
            time.sleep(random_time)
        file_number += 1
        target_filename = f"""{args.prefix}-{chunk_number}-{file_number}"""
        t = xtemplate.get_template_from_file(args.template_file)
        new_record = xtemplate.process_template(t, values)
        if args.debug:
            print(new_record)
        else:
            xs3.push_to_s3(args.aws_profile, args.bucket, args.subfolder, args.kmskey, new_record, target_filename)
        xtemplate.update_values(values)
        logger.debug(f"""completed file number: {target_filename}""")
    logger.debug(f"""completed chunk: {chunk_number}""")
    return values


def main(args):
    """ Main entry point of the app """
    duration = int(args.duration)
    chunks = int(args.chunks)
    number_of_files = int(args.numfiles)
    values = xtemplate.get_initial_values(args.startindex)
    for chunk in range(chunks):
        c = xscarymaths.random_restricted_composition(duration, number_of_files, 1, duration)
        bag_o_random = c
        do_a_chunk(args, chunk, bag_o_random, values)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--duration", action="store", dest="duration", default=5)
    parser.add_argument("-c", "--chunks", action="store", dest="chunks", default=2)
    parser.add_argument("-f", "--numfiles", action="store", dest="numfiles", default=2)
    parser.add_argument("-i", "--startindex", action="store", dest="startindex", default=1)
    parser.add_argument("-t", "--template", action="store", dest="template_file", default='templates/template1.txt')
    parser.add_argument("-b", "--bucket", action="store", dest="bucket", default='cto-aftc-sc')
    parser.add_argument("-s", "--subfolder", action="store", dest="subfolder", default='gw/opt/queue/pre_emails/')
    parser.add_argument("-m", "--mode", action="store", dest="mode", default='random_delay')
    parser.add_argument("-p", "--prefix", action="store", dest="prefix", default='msg')
    parser.add_argument("-k", "--kmskey", action="store", dest="kmskey", required=True)
    parser.add_argument("--debug", action="store_true", help='Output message to sysout rather than s3')
    parser.add_argument("--aws-profile", action="store", dest="aws_profile", default="default")
    args = parser.parse_args()
    main(args)
