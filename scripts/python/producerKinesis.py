# -*- coding: utf-8 -*-
#!pip install boto3

import boto3
import json

awsService = boto3.client(
    "kinesis",
    aws_access_key_id = "AAAAAAAAAAAA",
    aws_secret_access_key = "BBBBBBBBBBBB",
    region_name = "us-west-2"
    )
registro = {"idvendedor":"998","nome":"Maria"}
result = awsService.put_record(
    StreamName = "stream1",
    Data = json.dumps(registro),
    PartitionKey = "02"
)
print(result)