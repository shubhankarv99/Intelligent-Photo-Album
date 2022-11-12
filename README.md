# Intelligent Photo Album
Implemented a photo album web application, that can be searched using natural language
through both text and voice

### Services/ Technologies:
- AWS S3
- AWS API Gateway
- Swagger
- AWS Lambda
- AWS Lex
- AWS Rekognition
- DynamoDB
- AWS Opensearch/ElasticSearch
- AWS Cloudwatch
- AWS CodePipeline
- AWS CloudFormation

### Architecture:

<p align="center">
  <img src="Architecture.PNG" width="600" title="Architecture">
</p>


### Instructions to use
- Generate Github personal access token by giving access to everything.
  - [Generating access personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- Fork this repository on your account   
- Change the parameters of stack_1.yaml to appropriate values
  - Can be done by changing default value or can be changed in aws.(AWS asks you these parameter before deploying cloudformation)
- Run stack_1.yaml in AWS cloudformation
- Once that is successfully created, run the python code "update_api_gateway.py"
  - boto3 credential should be setup and required packages must be installed
- After the code runs without any error, change parameters in stack_2.yaml
  - codebucket value(stack2) = artifactname value(stack1)
  - lf2name value(stack2) = lf2name value(stack1)
- Run stack_2.yaml in AWScloudformation
- After succesfully implementing all, your system is live.
- Download the javasript sdk from api gateway and replace the one in website_v2.
- Change bucket name in index.js(line 112) to ccbucketname value(stack1)
- Test the website locally. 
- If it works push the changes to remote repository and the changes will be automatically reflected in hosted website inside S3 bucket.

