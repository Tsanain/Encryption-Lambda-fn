from cryptography.fernet import Fernet
import json

encryptionKey = "epPGev7qqJg1yQlY0zTOrg-py3aUX3SslJOXAbNJ8t8="

encryptedData = b"gAAAAABi3UXkTQ29lNeO7WYR2B5dYMgSJtVTkPFznfhJDOjDLSIMY6w3GnYmnHtSBXQKBimqoWd7Oat5UGn7Q9Ihi-kSLpoxTRRU87CLAmnKvW4Q72N9J2maUGbMQZDp1PYLng-vBrs5ugJKIGqk-6oaEDFQax_h5_fMIB3qHJyeYH-8XjPM1es="

cryptor = Fernet(encryptionKey)

decryptedData = cryptor.decrypt(encryptedData)
decryptedData = json.loads(decryptedData)

print(decryptedData)
