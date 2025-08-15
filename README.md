PYTHON AWS BOTO3 REAL TIME SCENARIOS

Step 1 - Clone this repo to local
Step 2 - Create the AWS account - https://aws.amazon.com/console/
Step 3 - Install Python and Visual Studio on You local Machine
Step 4 - Install AWS CLI on you Machine
Step 5 - Create an IAM user from AWS console and add access key ID to that use, Make sure to save the Access key ID and Access secret somewhere.
Step 6 - From powershell or cmd tape "aws configure" Command with the following input:
AWS Access Key ID [None]: USER_ACCESS_KEY_ID
AWS Secret Access Key [None]: USER_SECRET_ACCESS_KEY
Default region name [None]: YOUR_AWS_REGION
Default output format [None]: json

Step 7 - Install the required Python Modules On your local Machine

pip install boto3

Boto3 is AWS SDK for Python, used to perform various S3 operations

Step 8 - Go to the AWS and create a EC2 instance manually

Step 9 - Go to E2 Folder in github repo and run this command and you can notice the EC2 
instance details displayed in the output

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe Get_Instance_data.py

Step 10 - Go to DynamoDB Folder in github repo and run this command to create a dynamo DB table

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe dynamo_db.py

Step 11 - Upload the data in database in AWS

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe PutData_Db.py

Step 12 - Update the data in database

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe Update_DB.py

Step 13 - Create an S3 bucket

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe S3.py

Step 13 - Upload file to an S3 bucket

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe upload_s3.py
