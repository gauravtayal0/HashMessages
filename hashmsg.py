import hashlib
import sys
import base64
import argparse


parser = argparse.ArgumentParser(description='parse arguments')
parser.add_argument('msg', type=str,
                    help='message to be hashed')
parser.add_argument('algo', type=str,
                    help='algorithm to be choosed from md5, sha1, sha224, sha256, sha384, sha512')

args = parser.parse_args()

algo_type = args.algo
msg = args.msg

if(algo_type == 'md5'):
	hashmsg = hashlib.md5((msg)).hexdigest()
if(algo_type == 'sha1'):
	hashmsg = hashlib.sha1((msg)).hexdigest()
if(algo_type == 'sha224'):
	hashmsg = hashlib.sha224((msg)).hexdigest()
if(algo_type == 'sha256'):
	hashmsg = hashlib.sha256((msg)).hexdigest()
if(algo_type == 'sha384'):
	hashmsg = hashlib.sha384((msg)).hexdigest()
if(algo_type == 'sha512'):
	hashmsg = hashlib.sha512((msg)).hexdigest()

print hashmsg
