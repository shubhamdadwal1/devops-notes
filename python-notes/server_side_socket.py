#import socket

#server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# import smtplib
# from email.mime.text import MIMEText

# smtp_server='smtp.gmail.com'
# port=587 #tls(tranport layer securty)
# send_email='shubhamdadwal096@gmail.com'
# reciver_email='dadwalshubham096@gmail.com'
# messsage='hello shubham'

# #object of mail
# msg=MIMEText(messsage)
# msg['subject'] = "python automation"
# msg['from']= send_email 
# msg['to']=reciver_email

# with smtplib.SMTP(smtp_server,port) as server:
    
#     #tls encryption
#     server.starttls()
    
#     #login
#     password=input("enter the password:")
#     server.login(send_email,password)
    
#     #send the mail
#     server.sendmail(send_email, [reciver_email], msg.as_string())


# import os

# dir='C:\Users\ASUS\OneDrive\Desktop\docker files notes\python-notes'
# for filename in os.listdir(dir):
#     if filename.endswith('.txt'):
#         new_name=filename.replace('old_','new_')
#         os.rename(os.path.join(dir,filename), os.path.join(dir,new_name))


#json

# import json
# json_data='{"name":"shubham", "age":22, "city":"hoshiarpur"}'
# data=json.loads(json_data)
# print(data)

# print(data['name'])
# print(data['age'])

# data['city']='punjab'  #change data
# data['country']='india'  #add data
# print(data)

# #convert the python dictonary mode to json format
# json_format=json.dumps(data)
# print(json_format)


# import json
# dir={'name':'shubh','age':22,'city':'hariana','country':'india'}
# with open('object.json','w') as file:
#     json.dump(dir,file)


# import json
# dic={'name':'shubham','age':22,'state':'punjab'}
# json_format=json.dumps(dic)
# print(json_format)

# import json
# with open('object.json','r') as file:
#     data=json.load(file)
# print(data)
# print(type(data))