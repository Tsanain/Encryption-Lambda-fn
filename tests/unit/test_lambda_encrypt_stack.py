import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_encrypt.lambda_encrypt_stack import LambdaEncryptStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_encrypt/lambda_encrypt_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaEncryptStack(app, "lambda-encrypt")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
