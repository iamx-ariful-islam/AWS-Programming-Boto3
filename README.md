# AWS Programming Boto3

### **Learn about aws and 100+ aws programming using boto3**

[AWS](https://aws.amazon.com/) (Amazon Web Services) is a comprehensive and widely used cloud computing platform provided by Amazon. It offers a variety of cloud services, such as computing power, storage, databases, machine learning, analytics, security, and more. AWS is designed to help individuals, companies, and organizations build, deploy, and scale applications quickly without having to manage physical infrastructure.

AWS Programming refers to using [Amazon Web Services (AWS)](https://en.wikipedia.org/wiki/Amazon_Web_Services) to build and manage applications. It involves writing code that interacts with AWS services to perform tasks like deploying applications, processing data, storing files, and running compute workloads.


## Descriptions
This repository is focused on utilizing the Boto3 library, the official AWS SDK for Python, to interact with various `Amazon Web Services (AWS)` resources. Whether you are looking to automate cloud infrastructure management or integrate AWS services into your applications or learn aws programming, this project demonstrates the powerful capabilities of Boto3 for tasks like managing EC2 instances, S3 buckets, DynamoDB tables, RDS and more.

The primary aim of this repository is to provide a hands-on guide and a collection of Python scripts that will allow developers to effectively use Boto3 to interact with AWS services and streamline cloud management tasks.


## Features
* **EC2 Management:** Launch, stop, and terminate EC2 instances programmatically.
* **S3 Operations:** Upload, download, and manage S3 bucket contents.
* **DynamoDB/RDS Operations:** Perform Create, Read, Update, and Delete operations on DynamoDB/RDS tables.
* **IAM User Management:** Create, delete, and manage AWS IAM users and roles.
* **CloudWatch Metrics:** Access and monitor CloudWatch metrics for various AWS services.
* **Lambda Functions:** Deploy and invoke AWS Lambda functions.
* **CloudFormation:** Automate the creation of AWS resources using CloudFormation stacks.
* **Logs Group:** Create AWS cloudwatch logs group for frontend and backend.
* **Snapshots:** Creating a snapshot from an EBS volume.


## Prerequisites
* **AWS Account:** You'll need an active AWS account. If you don't have one, sign up here.
* **Python:** This project is written in Python 3.x. Ensure Python is installed on your machine.
* **Boto3 Library:** The official AWS SDK for Python.


## Task Requirements & Testing Environment
This repository was developed using the latest operating systems, software, and tools.

* **Operating System :** Windows11, Kali Linux
* **Software :** Python3.12 and Visual Studio Code
---


## Clone the Repository

```bash
git clone https://github.com/iam-ariful-islam/aws-programming-boto3.git
```


## Install it using pip:
The `requirements.txt` file, lists of all the Python libraries that depends on and installs those packages from the file and for better use:

```bash
pip install -r requirements.txt
# sudo pip install -r requirements.txt # linux

# or direct install

pip install boto3
# sudo pip install boto3 # linux
```


### Here are some examples of how to use this repository:
## 1. EC2 Instance Management Example
```python
import boto3

# create an EC2 resource object
ec2 = boto3.resource('ec2')

# launch an EC2 instance
instance = ec2.create_instances(
    ImageId='ami-xxxxxxxxxxxxxxxxx',  # replace with a valid AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
)

print("EC2 instance created with ID:", instance[0].id)
```

## 2. S3 Bucket Operations Example
```python
import boto3

# create an S3 client
s3 = boto3.client('s3')

# create a new S3 bucket
bucket_name = "my-new-bucket-12345"
s3.create_bucket(Bucket=bucket_name)

# upload a file to the bucket
s3.upload_file('local_file.txt', bucket_name, 'uploaded_file.txt')

print(f"File uploaded to {bucket_name}")
```

## 3. DynamoDB Operations Example
```python
import boto3

# create a DynamoDB client
dynamodb = boto3.resource('dynamodb')

# create a new table
table = dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {
            'AttributeName': 'UserId',
            'KeyType': 'HASH'  # partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'UserId',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table created:", table.table_name)
```


## Code Explanation
In this repository, you’ll find several scripts that showcase how to interact with different AWS services using Boto3. Here’s a brief explanation of how the code works:
`Make sure that boto3 is installed and you will need your AWS Access Key ID, Secret Access Key, Region and Output Format.`

**Set up AWS Credentials:** Ensure you have valid AWS credentials set up on your machine via the AWS CLI or by creating an IAM user and configuring credentials manually.<br/>
**Create Resources/Clients:** Use `boto3.resource('service_name')` to create resource objects for high-level service interactions (e.g., EC2, S3, DynamoDB, RDS) or `boto3.client('service_name')` for low-level service clients.<br/>
**Perform Operations:** Perform actions like launching instances, uploading files or creating tables using the respective methods provided by the resources or clients.<br/>
**Error Handling:** Implement error handling using Python’s try-except blocks to handle service errors like missing credentials, permission issues or service limits.<br/>


## Acknowledgments
`Boto3` is the AWS SDK for Python that allows you to interact with AWS services.
`Amazon Web Services (AWS)` for providing a suite of powerful cloud services.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

* Fork the repository.
* Create a new branch (git checkout -b feature-name).
* Commit your changes (git commit -am 'Add new feature').
* Push to your branch (git push origin feature-name).
* Create a new Pull Request.

Please make sure to update tests as appropriate.


## For more or connect with me
<p align='center'>
  <a href="https://github.com/iam-ariful-islam"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://twitter.com/am_ariful_islam"><img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://bd.linkedin.com/in/im-ariful-islam"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.facebook.com/jonakisoft.net/"><img src="https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
</p>


## License
This repository is licensed under the [MIT](https://choosealicense.com/licenses/mit/)