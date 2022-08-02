from cryptography.fernet import Fernet
import json
import os

def handler(event, context):
    
    text = event['body']
    text = bytes(text, 'utf-8')

    encryptionKey = os.environ['encrytionKey']

    cryptor = Fernet(encryptionKey)
    
    decryptedData = cryptor.decrypt(text)
    decryptedData = json.loads(decryptedData)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': decryptedData
    }
