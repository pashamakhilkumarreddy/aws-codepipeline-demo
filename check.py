import json

def handler(event, context):
  resp = "Hola Mundo!"
  return {
    'statusCode': 200,
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
    },
    'body': json.dumps(resp)
  }