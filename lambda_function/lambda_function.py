import json

def lambda_handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statuscode':200,
        'headers':{
            'Content-Type': 'text/plain'
        },
        'body': 'Hello from lambda created by GitHub'

    }