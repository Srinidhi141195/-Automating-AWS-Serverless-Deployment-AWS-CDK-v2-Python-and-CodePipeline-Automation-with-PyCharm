from aws_cdk import (
    #Duration,
    Stack,
    Stage,
    Environment,
    pipelines,
    aws_codepipeline as codepipeline
)
from constructs import Construct
from Resource_Stack.resource_stack import ResourceStack

class DeploymentState(Stage):
    def __init__(self, scope: Construct, id: str, env: Environment, **kwargs) -> None:
        super().__init__(scope, id, env=env , **kwargs)
        ResourceStack(self, 'ResourceStack', env=env, stack_name ="resource-stack-deployment")



class MysampleprojectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        git_input = pipelines.CodePipelineSource.connection(
            repo_string="Srinidhi141195/mysampleproject",
            branch="main",
            connection_arn="arn:aws:codestar-connections:eu-central-1:545942567149:connection/eefa482c-920b-494c-983d-37ec8a2b007b"
        )

        code_pipeline = codepipeline.Pipeline(
            self, "Pipeline",
            pipeline_name ="new-pipeline",
            cross_account_keys=False
        )



        synth_step =pipelines.ShellStep(
            id ="Synth",
            install_commands=[
                'pip install -r requirements.txt'
            ],
            commands=[
                'npx cdk synth'
            ],
            input=git_input
        )



        pipeline = pipelines.CodePipeline(

            self, 'CodePipeline',
            self_mutation=True,
            code_pipeline=code_pipeline,
            synth=synth_step
        )


        deployment_wave = pipeline.add_wave("DeploymentWave")

        deployment_wave.add_stage(DeploymentState(
            self, 'DeploymentStage',
            env=(Environment(account='545942567149', region='eu-central-1'))
        ))



        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "MysampleprojectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
