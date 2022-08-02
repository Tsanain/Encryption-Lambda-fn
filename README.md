# Encryption-Lambda-fn
Encrypting and decrypting the body data of POST request using `AWS Api gateway` and `lambda function` deployed via `aws cdk` python. `Cryptography` library is used for encryption. Encryption key is stored in env variables of lambda function. Imported a layer for cryptography library from <a href = "https://api.klayers.cloud//api/v2/p3.9/layers/latest/ap-south-1/json">here</a>.

## Requirements

1. AWS account and access key 
2. `aws cdk`, configured with access key
3. `Cryptography` python library
4. <a href="https://www.postman.com/">Postman</a>

## Installation and working

1. Install aws cdk, configure aws account using access key.
2. Create a project using `cdk init`, paste the "lambda" and "lambda_encrypt" folder from this repository, change the app.py file accordingly.
3. Run `cdk deploy`.
4. Copy the api gateway link into postman under `POST` method.
5. Append "/encryptor/" for encryption or "/decryptor/" for decrytion at the end of api link.
6. Get Api key from api gateway console and paste it in header with `x-api-key` as key and api key value as value.
7. Enter data in json format under raw in body for encryption or in text format for decryption and send the request.
8. Decryption request will not work without encrypting the data.

   ### Output
   Encryption:
   ![image](https://user-images.githubusercontent.com/89830533/182309261-1210496a-7617-4b38-9b05-e27da8c6089f.png)
   Decryption:
   ![image](https://user-images.githubusercontent.com/89830533/182309566-18bbea80-c1eb-495f-b793-4640b727e11e.png)


