import json

import requests

def main(event, context):
    r = requests.get('https://consumer-ow-api.deliveroo.com/orderapp/v2/restaurants?geohash=u09tvqmq806q')

    body = r.json()

    del body['links']

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

