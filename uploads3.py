
import json
import boto3

def upload_json_to_s3(data):
    with open('corona-data.json', 'w') as f:
        json.dump(data, f)

    s3 = boto3.resource('s3')
    s3.Bucket("corona-data-bucket-123523145").upload_file("corona-data.json","data/corona-data.json" )