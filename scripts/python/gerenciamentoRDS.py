# -*- coding: utf-8 -*-
#!pip install boto3
#####################################################################################################################################
import psycopg2 as psy
conn = psy.connect(host="0.0.0.0:8080",database="postgres",user="postgres",password="postgres")
conn.autocommit = True
cur = conn.cursor()
result = cur.execute("create database inventario;")
conn.close()
#####################################################################################################################################
import psycopg2 as psy
conn = psy.connect(host="0.0.0.0:8080",database="inventario",user="postgres",password="postgres")
conn.autocommit = True
cur = conn.cursor()
result = cur.execute("create table arquivos (idarquivo int, nomearquivo varchar(256));")
conn.close()
#####################################################################################################################################
import boto3
import io
import psycopg2 as psy

s3 = boto3.resource(
    service_name = "s3",
    region_name = "sa-east-1",
    aws_access_key_id = "AAAAAAAAAAAAAAA",
    aws_secret_access_key = "BBBBBBBBBBBBBBBBBBBB"
)
bucket="engenheirodedadosimagens01"
prefix="imagens/"
id = 0
#####################################################################################################################################
conn = psy.connect(host="0.0.0.0:8080",database="inventario",user="postgres",password="postgres")
conn.autocommit = True
cur = conn.cursor()

for objectS3 in s3.Bucket(bucket).objects.filter(Prefix=prefix):
  if objectS3.key.endswith("jpg") or objectS3.key.endswith("JPG"):
    filename = objectS3.key.split("/")[1]
    id += 1
    cur.execute("insert into arquivos (idarquivo,nomearquivo) values ("+str(id)+",'"+filename+"')")
conn.close()
#####################################################################################################################################
import psycopg2 as psy
conn = psy.connect(host="",database="inventario",user="postgres",password="postgres")
conn.autocommit = True
cur = conn.cursor()
result = cur.execute("select * from arquivos")
for i in cur.fetchall():
  print(i)
conn.close()