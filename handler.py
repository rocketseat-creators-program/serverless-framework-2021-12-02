import json
import boto3

def lambdafunction(event, context):
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=bucket,Key=key)
    total_sum, row_count = 0, 0
    for line in obj['Body'].iter_lines(chunk_size=1024, keepsends=False):
        total_sum += int(line(0))
        row_count += 1
    print(f"Linhas {row_count} Total de colunas {total_sum}")



