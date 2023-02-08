# -*- coding: utf-8 -*-
#!pip install boto3

import boto3

awsService = boto3.client(
    "kinesis",
    aws_access_key_id = "AAAAAAAAAAAAAAAAAAAAA",
    aws_secret_access_key = "BBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    region_name = "us-west-2"
    )
shard = awsService.get_shard_iterator (
    StreamName = "stream1",
    ShardId = "shardId-000000000002",
    ShardIteratorType = "LATEST"
)["ShardIterator"]

while shard is not None:
  result = awsService.get_records(ShardIterator = shard)
  registros = result["Records"]
  shard = result["NextShardIterator"]
  for registro in registros:
    print(registro["SequenceNumber"])
    print(registro["ApproximateArrivalTimestamp"])
    print(registro["PartitionKey"])
    print(registro["Data"])