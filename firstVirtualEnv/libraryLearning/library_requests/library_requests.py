import requests

payload = {'username': 'TNI', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

# with open('comic.png', 'wb') as f:
#     f.write(r.content)

r_dict = r.json()

print(r_dict['form'])
