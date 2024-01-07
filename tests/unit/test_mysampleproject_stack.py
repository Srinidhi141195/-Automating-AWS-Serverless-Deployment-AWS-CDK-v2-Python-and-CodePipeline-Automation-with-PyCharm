import aws_cdk as core
import aws_cdk.assertions as assertions

from mysampleproject.mysampleproject_stack import MysampleprojectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in mysampleproject/mysampleproject_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MysampleprojectStack(app, "mysampleproject")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
