# AutumnCapasso
# UMGC
# Homework 1

# import statments
import sys
import datetime
import logging
import boto3
from botocore.exceptions import ClientError


# main menu starts
def main():
    menu()


# start of menu
def menu():
    x = datetime.datetime.now()
    selection = 0

    while selection < 5:
        print("Welcome to the secure programming in s3 program")
        print("Press 1 to create an S3 bucket named autumncapasso-555555")
        print("Press 2 to put an object in the bucket")
        print("Press 3 to delete an object in the bucket")
        print("Press 4 Copies and object from one bucket to another")
        print("Press 5 Download an exsiting object for a bucket")
        print("Press 6 to exit")

        # Program takes in input
        print("Enter selection: ")
        selection = int(input())

        # conditional section that determins the menu choice
        if selection == 1:
            print(create_bucket())
            #end_program()

        if selection == 2:
            print(create_object())
            #end_program()

        if selection == 3:
            print(delete_object())
            #end_program()

        if selection == 4:
            print(copy())
            #end_program()

        if selection == 5:
            print(download_object())
            #end_program()

        if selection == 6:
            print("you haev exited the program")
            print(x)
            #end_program()

        else:

            print("\r\n###############################6###############\r\n"
                  " * You have entered an invalid selection * "
                  " \r\n##############################################\r\n ")


# Exit Function
def end_program():
    sys.exit()


# Create bucket function
def create_bucket(bucket_name='autumncapasso-555555', region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

  
# Create an object in previously created s3 bucket 
def create_object():
    session = boto3.session.Session()
    s3 = session.resource('s3')
    object = s3.Object('autumncapasso-555555', 'file_name.txt')
    txt_data = 'hello world'
    result = object.put(Body=txt_data)
    res = result.get('ResponseMetadata')
    if res.get('HTTPStatusCode') == 200:
        print('File Uploaded Successfully')
    else:
        print('File Not Uploaded')
        
#Deletes previously created object in s3 bucket 
def delete_object():
    session = boto3.session.Session()
    s3 = boto3.resource('s3')
    s3.Object('autumncapasso-555555', 'file_name.txt').delete()
    print('File Deleted Successfully')
    
def copy():
    s3 = boto3.resource('s3')
    copy_source = {
      'Bucket': 'autumncapasso-555555',
      'Key': 'file_name.txt'
    }
    bucket = s3.Bucket('otherbucket555555')
    bucket.copy(copy_source, 'file_name.txt')
  
def download_object():
    s3 = boto3.client('s3')
    s3.download_file('autumncapasso-555555', 'file_name.txt','file_name.txt')

if __name__ == "__main__":
    main()
