# Encryption-Lambda-fn
Encryption using AWS Api gateway and lambda function using cdk python. Cryptography library is used for encryption. Encryption key is stored in env variables of lambda function. Imported a layer for cryptography library from <a href = "https://api.klayers.cloud//api/v2/p3.9/layers/latest/ap-south-1/json">here</a>

## Requirements

1. AWS account and access key 
2. `aws cdk`, configured with access key
3. `Cryptography` python library
4. <a href="https://www.postman.com/">Postman</a>

## Installation and working

1. Install aws cdk, configure aws account using access key.
2. Create a project using `cdk init`, paste the "lambda" and "lambda_encrypt" folder from this repository.
3. Run `cdk deploy`.
4. Copy the api gateway link into postman under `GET` method.
5. Get Api key from api gateway console and paste it in header with `x-api-key` as key and api key value as value.
6. Enter string parameters to be encrypted and run the link

   ### Output
   
   <img src="![image](https://user-images.githubusercontent.com/89830533/177985463-d92819ce-90b7-44d2-bdd1-2d6dd905a937.png)" height = 70px width = 200px>
