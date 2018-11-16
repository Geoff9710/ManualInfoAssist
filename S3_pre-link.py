# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 12:08:36 2018

@author: AkSangwan
"""
import boto3
#import requests


# Code to generate a pre-signed url
s3 = boto3.client(
    's3', verify= False,
    region_name='eu-west-2'
)

signed_url = s3.generate_presigned_url( ClientMethod='get_object', Params={'Bucket': 's3-ukscni', 'Key': '2018-07-23T171350.530624ReportTESCOPLC.pdf'}, ExpiresIn = 86400)

#response = requests.get(signed_url, verify = False)
#print(response)
print(signed_url)

