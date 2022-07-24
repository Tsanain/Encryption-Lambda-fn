from cryptography.fernet import Fernet
import json

encryptionKey = "key"
encryptedData = b"data here"
cryptor = Fernet(encryptionKey)
decryptedData = cryptor.decrypt(encryptedData)
decryptedData.decode('utf-8')
decryptedData = json.loads(decryptedData)
decryptedData = json.dumps(decryptedData, indent=2)  

print(decryptedData)
