import json
import boto3

def lambdafunction(event, context):
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket="",Key="")
    total_sum, row_count = 0, 0
    for line in obj['Body'].iter_lines(chunk_size=1024, keepsends=False):
        total_sum += int(line(0))
        row_count += 1
    print(f"Linhas {row_count} Total de colunas {total_sum}")



