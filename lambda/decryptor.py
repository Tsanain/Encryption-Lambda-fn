from cryptography.fernet import Fernet
import json

encryptionKey = "key here"

encryptedData = b"data here"

cryptor = Fernet(encryptionKey)

decryptedData = cryptor.decrypt(encryptedData)

decryptedData = json.loads(decryptedData)

print(decryptedData)
