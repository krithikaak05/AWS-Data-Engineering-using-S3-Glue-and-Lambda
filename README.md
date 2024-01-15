# Data Engineering Project: Sales Data Transformation on AWS

This repository demonstrates an end-to-end data engineering workflow that involves cleaning and filtering sales data within the AWS cloud environment.

## Project Overview

This project showcases the following key steps:

Data Acquisition from Kaggle and Upload to S3
Data Cataloging with Glue Crawler
Data Filtering with Lambda Function
Clean Data Storage in S3
Local Download for Further Analysis

## Key Technologies and Services

AWS S3
AWS Glue
AWS Lambda
IAM

## Project Highlights

Demonstrates proficiency in data engineering tasks on AWS.
Employs serverless architecture for efficient data processing.
Implements robust data filtering based on specific requirements.
Facilitates both cloud-based and local-based data analysis.
## Project Structure

This repository includes:

README.md (this file)
lambda_function.py (Python code for the Lambda function)
sample_data.csv (a sample of the original sales data)
clean_data.csv (the filtered and clean sales data)

## Setup Instructions

Prerequisites:
An AWS account with necessary permissions.
Basic familiarity with AWS S3, Glue, Lambda, and IAM services.

1.Create S3 buckets:
   Create two S3 buckets: one for the raw data (raw-data-bucket) and one for the clean data (clean-data-bucket).
   
2.Upload data to S3:
   Upload the sample sales data to the raw-data-bucket.

3.Create Glue crawler:
  Create a Glue crawler to catalog the data in the raw-data-bucket.

4.Create Glue ETL job:
  Create a Glue ETL job using the glue_etl_job.py script.

5.Create Lambda function:
  Create a Lambda function using the lambda_function.py code. I have used a boto script :

  import json
  import boto3
  glueClient - boto3.client('glue')
  def lamnda_handler(event,context):
    glueClient.start_job_run(Jobname="your jobname")
    return "Job Started"

6.Configure IAM permissions:
  Ensure appropriate IAM permissions are in place for the Glue job and Lambda function to access S3 buckets.

![Architecture](images/aws_arch.png)

## Running the Project

Trigger the Glue ETL job.
The job will execute the Lambda function to filter the data.
The filtered data will be stored in the clean-data-bucket.
Download the clean data from S3 for further analysis.
