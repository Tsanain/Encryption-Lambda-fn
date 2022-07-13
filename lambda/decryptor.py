from cryptography.fernet import Fernet
import json

encryptionKey = "Iqo3RICZYMSZoqik9hfuoT2bb_J-XaY3ApDnalEv0WE="

encryptedData = b"gAAAAABizmTSX_JDjzyfRUfklEWlg3DdiadgpxR2UH9FtIPcxLCSwdmA6R-k6wij4NzEJEpB1-j7pR5Bq3bq1BWArwVNqGAB9RWuwBWUP-6O0fk5-O_6IPFiD6fHv3ivlUoSLPW-PXbG-uWfAS8vAGDise7gPYwhbqsuN_Zx0nSdCSm_i_utoLz-SkjiKAxkUF8-_Jvjc9DNaSWJmtmj3AWr-DHiOhD5uVPv2emhNkXeV3YYYOJg40OhQId7gSmwSjwRt4r2ksPI7NW-jLLUIzXJoyLsjoa8Q0x97kaT0YCDNyQR5FRWT0dq7VBL25sazbhDoCi0ZLPrlcJb5qig8rKItdFjTt0nKQ=="

cryptor = Fernet(encryptionKey)
decryptedData = cryptor.decrypt(encryptedData)
decryptedData.decode('utf-8')
decryptedData = json.loads(decryptedData)
decryptedData = json.dumps(decryptedData, indent=2)  

print(decryptedData)
