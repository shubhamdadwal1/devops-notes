#list of s3 buckets
# import boto3
# s3=boto3.resource("s3")
# def lists(s3):
#     for buckets in s3.buckets.all():
#         print(buckets.name)
# def creates3(s3):
#     s3.create_bucket(Bucket="shubhambuckets2",
#                      CreateBucketConfiguration={
#                          'LocationConstraint':'ap-south-1',
#                      },)
#     print("successfully bucket is created")
# creates3(s3)
# lists(s3)



# import boto3
# s3=boto3.resource('s3')
# def create(s3):
#     s3.create_bucket(Bucket="shubham86556",
#                      CreateBucketConfiguration={
#                          'LocationConstraint':'ap-south-1'
#                      },)
#     print("sucessfully")
# create(s3)
# def lists(s3):
#     for bucket in s3.buckets.all():
#         print(bucket.name)
# lists(s3)



# import boto3
# s3=boto3.resource('s3')
# bucket=s3.Bucket('shubh1233242')
# bucket.objects.all().delete()
# bucket.delete()
# print('deleted !!')



# import boto3
# s3=boto3.resource('s3')
# def deleted(s3):
#     for bucket in s3.buckets.all():
#         print(f"deleted !! {bucket.name}")
#         bucket.objects.all().delete()
#         bucket.delete()
#     print("successfully")
# deleted(s3)


