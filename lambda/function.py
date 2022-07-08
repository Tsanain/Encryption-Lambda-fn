import json
import os
from cryptography.fernet import Fernet


def handler(event, context):
    text = event['queryStringParameters']
    text = json.dumps(text, indent=2).encode('utf-8')
    
    encryptionKey = os.environ['encrytionKey']

    cryptor = Fernet(encryptionKey)
    encryptedData = cryptor.encrypt(text)
    output = {}
    output['Encrypted data'] = str(encryptedData, 'utf-8')

    decryptedData = cryptor.decrypt(encryptedData)
    decryptedData.decode('utf-8')
    decryptedData = json.loads(decryptedData)
    decryptedData = json.dumps(decryptedData, indent=2)    

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(output) #  + decryptedData
    }

