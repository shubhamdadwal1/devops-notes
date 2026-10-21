#def shu(name):
 #   print(f'hello,{name}')
#shu('shubham')


#def sum(x,y):
 #   result=x+y
  #  print(result)
#sum(10,5)

#def su(a,b,c,d):
 #   sol=a+b+c+d
  #  print('result',sol)
#u(1,2,3,4)


#def sum(x,y):
 #   return x+y
#x=int(input("enter number:"))
#y=int(input("enter second number:"))
#result=sum(x,y)
#print("result",result)


#def even(num):
 #   return num%2==0
#def odd(num):
 #   return num%2!=0
#def seq(num):
 #   return num**2
#num=int(input("enter the number: "))
#if even(num):
 #   print(f"{num} is even")
#else:
 #   print(f"{num} is odd")
#print(f"{num} is square of {seq(num)}")



#n=int(input("enter the number: "))
#result=n**2
#print(f"{n} is square ",result)


#import math_operation_modules
#a=math_operation_modules.add(2,4)
#print(a)



# import smtplib
# from email.mime.text import MIMEText

# smtp_server='smtp.gmail.com'
# port=587
# send_mail='dadwalshubham096@gmail.com'
# receiver_mail='shubhamdadwal096@gmail.com'
# meassage='hello, shubhu'

# msg=MIMEText(meassage)
# msg['subject']='python automation'
# msg['from']=send_mail
# msg['to']=receiver_mail

# with smtplib.SMTP(smtp_server,port) as server:
#   server.starttls()
#   passwd=input("enter the password: ")
#   server.login(send_mail,passwd)
#   server.sendmail(send_mail, [receiver_mail], msg.as_string())