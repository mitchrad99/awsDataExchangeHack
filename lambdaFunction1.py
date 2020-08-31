# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
import csv
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('UserDatabase')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
# extract values from the event object we got from the Lambda service and store in a variable
    name = event['ID']
    infected = event['Diagnosed']
    diagnosisdatetime = event['DiagnosisDate']
    symptomsdatetime = event['SymptomsDate']
    symptom1 = event['Symptom1']
    symptom2 = event['Symptom2']
    symptom3 = event['Symptom3']
    symptom4 = event['Symptom4']
    symptom5 = event['Symptom5']
    symptom6 = event['Symptom6']
    symptom7 = event['Symptom7']
    symptom8 = event['Symptom8']
    symptom9 = event['Symptom9']
    contact = event['Contact']
# write name and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'ID': name,
            'Infected':infected,
            'DiagnosisDateTime':diagnosisdatetime,
            'SymptomsDateTime':symptomsdatetime,
            'Symptom1':symptom1,
            'Symptom2':symptom2,
            'Symptom3':symptom3,
            'Symptom4':symptom4,
            'Symptom5':symptom5,
            'Symptom6':symptom6,
            'Symptom7':symptom7,
            'Symptom8':symptom8,
            'Symptom9':symptom9,
            'Contact':contact
            })
            
    key = 'ids.csv'
    bucket = 'aws-data-exchange-mitchrad99'
    s3_resource = boto3.resource('s3')
    s3_object = s3_resource.Object(bucket, key)
    data = s3_object.get()['Body'].read().decode('utf-8').splitlines()

    lines = csv.reader(data)
    value = next(lines)
    for row in lines:
        if row[1] == name:
            value = row
            

# return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda, ' + value[1]),
        'id':value[1],
        'infected':value[2],
        'suspected':value[3],
        'last_infected':value[4],
        'last_suspected':value[5],
        'last_tested':value[6],
        'problem_location_lats':value[7],
        'problem_location_longs':value[8],
        'symptom_score':value[9],
        'lifestyle_score':value[10],
        'total_score':value[11]
        
    }