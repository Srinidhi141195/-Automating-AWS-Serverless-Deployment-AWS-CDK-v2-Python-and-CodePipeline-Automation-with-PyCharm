#!/usr/bin/env python3
import os
from aws_cdk import App, Environment, Tags
from mysampleproject.mysampleproject_stack import MysampleprojectStack

app = App()
MysampleprojectStack(app, "MysampleprojectStack",
    env=Environment(account='545942567149', region='eu-central-1'),
    stack_name='github-Codepipeline-Stack'
)

Tags.of(app).add(key='feature', value='resource-stack')
Tags.of(app).add(key='contact', value='sacharla@usf.edu')
Tags.of(app).add(key='feature', value='Solution_Architect')
app.synth()

