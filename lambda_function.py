import json 
import boto3 
glueClient - boto3.client('glue') 
def lamnda_handler(event,context): 
    glueClient.start_job_run(Jobname="your jobname") 
    return "Job Started"