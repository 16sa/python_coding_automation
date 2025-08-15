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

Step 14 - Upload file to an S3 bucket

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe upload_s3.py

=================================

Real time Python Automations

Step 1 - Go to Python_automation folder in github and run the Compare_list.py

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe Compare_list.py

Step 2 - Install the required Python Modules

pip install requests

requests is a library for making HTTP requests in a much simpler and more intuitive way than Python's built-in modules. It's widely used for tasks like interacting with web APIs and downloading web content.

Step 3 - Go to Python_automation folder in github and run the Endpoint_Hit.py

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe Endpoint_Hit.py

Step 4 - Go to Python_automation folder in github and run the List_with_sort.py

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe List_with_sort.py

Step 5 - Run the TEXT TO SPEECH CONVERTER python script

***Install the libraries first in the local:

pip install PyPDF2
pip install pyttsx3

PyPDF2 is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files

pyttsx3 is a text-to-speech conversion library in Python

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe SPEECH.py

The above script will read the dummypdf.pdf which is there in folder

Step 6 - Run the OTP / PASSWORD Generator python script

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe OTP_VERIFICATION.py

*** Install the libraries first in the local:

Pyperclip is a cross-platform Python module for copy and paste clipboard functions

pip install pyperclip 

curl https://files.pythonhosted.org/packages/a7/2c/4c64579f847bd5d539803c8b909e54ba087a79d01bb3aba433a95879a6c5/pyperclip-1.8.2.tar.gz > pyperclip.tar.gz

tar -xzvf pyperclip.tar.gz

cd pyperclip-1.8.2

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe -m pip install setuptools

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe setup.py install

/c/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe PASSWORD_GENERATOR.py








