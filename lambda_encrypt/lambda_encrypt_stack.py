from aws_cdk import (
    Stack,
    aws_apigateway as _api,
    aws_lambda as _lambda,
)

from constructs import Construct

from cryptography.fernet import Fernet

key = Fernet.generate_key()

key = str(key, 'utf-8')

class LambdaEncryptStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        layer1 = _lambda.LayerVersion.from_layer_version_arn(self, "cryptography-layer", layer_version_arn="arn:aws:lambda:ap-south-1:770693421928:layer:Klayers-p39-cryptography:5")

        enc_lambda_func = _lambda.Function(
            self, 'lambda_encryption', runtime=_lambda.Runtime.PYTHON_3_9,
            code = _lambda.Code.from_asset('lambda'),
            handler='encryptor.handler',
            environment={
                'encrytionKey': key
            },
            layers=[layer1]
        )

        dec_lambda_func = _lambda.Function(
            self, 'lambda_decryption', runtime=_lambda.Runtime.PYTHON_3_9,
            code = _lambda.Code.from_asset('lambda'),
            handler='decryptor.handler',
            environment={
                'encrytionKey': key
            },
            layers=[layer1]
        )


        api = _api.RestApi(self, 'encryptionApi', rest_api_name='encryptionApi')

        encryptor = api.root.add_resource('encryptor')

        decryptor = api.root.add_resource('decryptor')

        li = _api.LambdaIntegration(enc_lambda_func, proxy=True, integration_responses=[
                _api.IntegrationResponse(
                    status_code="200",  
                )
            ],
        )

        li_dec = _api.LambdaIntegration(dec_lambda_func, proxy=True, integration_responses=[
                _api.IntegrationResponse(
                    status_code="200",  
                )
            ],
        )

        encryptor.add_method("POST", li, method_responses=[
                _api.MethodResponse(
                    status_code="200", 
                )
            ], api_key_required=True
        )

        decryptor.add_method("POST", li_dec, method_responses=[
                _api.MethodResponse(
                    status_code="200", 
                )
            ], api_key_required=True
        )

        plan = api.add_usage_plan("UsagePlan",
            name="Easy",
            throttle=_api.ThrottleSettings(
            rate_limit=10,
            burst_limit=2
            )
        )

        plan.add_api_stage(stage=api.deployment_stage)

        _api_key = api.add_api_key("single-api-key")

        plan.add_api_key(_api_key)

        

        
