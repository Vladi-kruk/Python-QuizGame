import boto3
from botocore.exceptions import NoCredentialsError

secretFile = open("C://Users/krukv/Desktop/HP/AmazonS3PrivetePublicKey.txt", 'r')
ACCESS_KEY = secretFile.readline().split("\n")[0]
SECRET_KEY = secretFile.readline().split("\n")[0]

projectFilePath = "C://Users/krukv/Desktop/HP/pythonProject/main.py"
bucket = 'quiz-game-s3-bucket'
s3_file = "quiz-main.py"

def upload_to_aws(local_file, bucket, s3_file,ACCESS_KEY,SECRET_KEY):

    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

secretFile.close()
uploaded = upload_to_aws(projectFilePath, bucket, s3_file,ACCESS_KEY,SECRET_KEY)