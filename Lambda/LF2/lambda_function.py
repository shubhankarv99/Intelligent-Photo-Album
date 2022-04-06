import json
import logging
import boto3
import requests
from pprint import pprint

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    # TODO implement
    
    # logger.debug(event)
    
    # bucket_name = event['Records'][0]['s3']['bucket']['name']
    # image_name = event['Records'][0]['s3']['object']['key']
    # logger.debug(f"Bucket: {bucket_name}  Image: {image_name}")
    
    # client_rec =boto3.client('rekognition', region_name = 'us-east-1')
    # response_res = client_rec.detect_labels(Image={'S3Object':{'Bucket':bucket_name,'Name':image_name}},
    #     MaxLabels=10)
    # logger.debug(response_res)
    
    # client_s3 = boto3.client('s3')
    # response_s3 = client_s3.head_object(Bucket="cc-b2", Key="landscape_resized.jpg")
    # logger.debug(response_s3)
    
    # try:
    #     meta_labels = response_s3['Metadata']['x-amzmeta-customLabels']
    # except KeyError:
    #     meta_labels = []

    # labels = [label['Name'] for label in response_res['Labels']] + meta_labels
    
    # a1 = {}
    # a1["objectKey"] = image_name
    # a1["bucket"] = bucket_name
    # a1["createdTimestamp"] = str(datetime.now())
    # a1["labels"] = labels
    # logger.debug(a1)

    # This is from codebuild 2
    logger.debug(event)
    logger.debug(context)
    
    
    
    host = 'https://search-cc-photos-qco2o44jvnbkzdh5q6cycer6l4.us-east-1.es.amazonaws.com'
    master_user = "test"
    master_password = "Test@1234"
    
    text = "Hello"
    
    client_lex = boto3.client('lex-runtime')
    response = client_lex.post_text(
        botName='SearchPhotos',
        botAlias ='$LATEST',
        userId="Aniket",
        inputText=text
        )
    logger.debug(response)
        
    if response['dialogState'] == "ElicitIntent" or response['dialogState'] == 'ElicitSlot':
        return {
            'statusCode': 200,
            'message': json.dumps(response['message'])
            
        }
    
    labels = [val for val in response['slots'].values() if val is not None]
    logger.debug(labels)
    
    
    query_labels = ','.join(labels)
    url = host + '/_search?q=labels:{}&size=1000'.format(query_labels)
    r = requests.get(url, auth=(master_user, master_password)) 
    data = json.loads(r.text)
    logger.debug(data)
    
    image_names = []
    for doc in data['hits']['hits']:
        image_names.append(doc['_source']['objectKey'])
    
    # s3 = boto3.resource('s3')
    # obj = s3.Object(bucket, key)
    print(image_names)
    

    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
