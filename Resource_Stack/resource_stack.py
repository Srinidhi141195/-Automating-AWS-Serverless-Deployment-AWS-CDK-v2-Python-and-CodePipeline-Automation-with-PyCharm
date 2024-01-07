from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as function_lambda,
    aws_s3 as s3
)

from constructs import Construct

class ResourceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        queue = sqs.Queue(
            self, "AWSCDKCodePipelineQueue",
            visibility_timeout=Duration.seconds(300),
            queue_name="demonstration-queue"
        )
        function = function_lambda.Function(self, "DemoCDKGITLambda",
                                            function_name="CodePipeline_Lambda",
                                            runtime=function_lambda.Runtime.PYTHON_3_10,
                                            code=function_lambda.Code.from_asset('./lambda_function'),
                                            handler="lambda_function.lambda_handler")

        bucket = s3.Bucket(self, "MyFirstCDKBucket-Srinidhi", versioned = True,
                           bucket_name= "demo-bucket-srinidhi-acharla-cdk",
                           block_public_access=s3.BlockPublicAccess.BLOCK_ALL)
