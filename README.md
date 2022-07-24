# Encryption-Lambda-fn
Encrypting body data of POST request using `AWS Api gateway` and `lambda function` deployed via `aws cdk` python. `Cryptography` library is used for encryption. Encryption key is stored in env variables of lambda function. Imported a layer for cryptography library from <a href = "https://api.klayers.cloud//api/v2/p3.9/layers/latest/ap-south-1/json">here</a>.

## Requirements

1. AWS account and access key 
2. `aws cdk`, configured with access key
3. `Cryptography` python library
4. <a href="https://www.postman.com/">Postman</a>

## Installation and working

1. Install aws cdk, configure aws account using access key.
2. Create a project using `cdk init`, paste the "lambda" and "lambda_encrypt" folder from this repository.
3. Run `cdk deploy`.
4. Copy the api gateway link into postman under `POST` method.
5. Get Api key from api gateway console and paste it in header with `x-api-key` as key and api key value as value.
6. Enter data in json format under raw in body and send the request.

   ### Output
   
   ![image](https://user-images.githubusercontent.com/89830533/180649290-3f7063b0-71b5-4ee1-9777-1ab602e463ae.png)
