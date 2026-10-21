# import requests
# reponse=requests.get("https://jsonplaceholder.typicode.com/posts/3")
# if reponse.status_code ==200:
#     print(reponse.json())
# else:
#     print(f"error {reponse.json()}")
    
    

# import requests
# url='https://jsonplaceholder.typicode.com/posts'
# data={'name':'shubham','age':22,'state':'punjab'}
# response=requests.post(url,json=data)
# if response.status_code==201:
#     print(f"sucessgull{response.json()['id']}")
# else:
#     print(f"error {response.status_code}")


# import requests
# response=requests.delete('https://jsonplaceholder.typicode.com/posts/1')
# if response.status_code==200:
#     print("successfully deleted")
# else:
#     print(f"error:  {response.status_code}")